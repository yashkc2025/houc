from typing import Callable, List
from functools import wraps
from flask import request, abort, jsonify, Request, make_response
import re
import jwt
import os
import service.user as userService
from database.models import UserTypes
import requests


frontend_url = "http://localhost:5173"


def len_checker(prop, length: int):
    if len(prop) != length:
        return abort_request(400, prop + "should be " + length + " digits")
    else:
        pass


def verifyPayload(required: List[str]) -> Callable:
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def decorated(*args, **kwargs):
            payload = request.get_json()

            print("***")
            print(payload)

            if not all(prop in payload for prop in required):
                abort(400, description="Unauthorized: Missing required properties")

            return f(payload, *args, **kwargs)

        return decorated

    return decorator


def verifyFormPayload(required: List[str]) -> Callable:
    def decorator(f: Callable) -> Callable:
        @wraps(f)
        def decorated(*args, **kwargs):
            payload = {}
            for key, value in request.form.lists():
                if key in required:
                    payload[key] = value[0]

            # Find which required keys are missing in the payload
            missing_keys = [key for key in required if key not in payload]

            if missing_keys:
                # Join missing keys into a comma-separated string for the error message
                missing_keys_str = ", ".join(missing_keys)
                abort(
                    400,
                    description=f"Unauthorized: Missing required properties: {missing_keys_str}",
                )

            return f(payload, *args, **kwargs)

        return decorated

    return decorator


def checkPassword(password: str):
    # should contain at least one number, one letter and be 8 character long
    pattern = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
    return bool(pattern.match(password))


def checkEmail(email: str):
    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(pattern.match(email))


def token_required_customer(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("auth_token")

        if token is not None:
            try:
                user_details = jwt.decode(
                    token, os.getenv("SECRET_KEY"), algorithms=["HS256"]
                )

                # TODO : Check if the user exists in the database

                print(user_details["id"])

                # checking if user_id is valid
                userService.get_user_details(user_details["id"])

                # If the token is valid, proceed to call the original function
                return f(*args, **kwargs)

            except jwt.InvalidTokenError:
                # If the token is invalid, return a 401 Unauthorized error
                return jsonify({"error": "Invalid token"}), 401

        else:
            # If the Authorization header is missing, return a 401 Unauthorized error
            return jsonify({"error": "Missing token"}), 401

    return decorated


def token_required_professional(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get("auth_token")

        if token is not None:
            try:
                user_details = jwt.decode(
                    token, os.getenv("SECRET_KEY"), algorithms=["HS256"]
                )

                # TODO : Check if the user exists in the database

                print(user_details["id"])

                # checking if user_id is valid
                userService.get_professional_details(user_details["id"])

                # If the token is valid, proceed to call the original function
                return f(*args, **kwargs)

            except jwt.InvalidTokenError:
                # If the token is invalid, return a 401 Unauthorized error
                return jsonify({"error": "Invalid token"}), 401

        else:
            # If the Authorization header is missing, return a 401 Unauthorized error
            return jsonify({"error": "Missing token"}), 401

    return decorated


def getUserID() -> str:
    token = request.cookies.get("auth_token")

    if token is not None:
        try:
            print(token)
            user_details = jwt.decode(
                token, os.getenv("SECRET_KEY"), algorithms=["HS256"]
            )

            return user_details["id"]

        except jwt.InvalidTokenError:
            return None
    else:
        abort(401, description="Unauthorized: Missing token")


def adminOnlyRoute(f: Callable) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):
        user_id = getUserID()
        user = userService.get_user_details(user_id)

        print(user)

        if user.user_type != UserTypes.ADMIN:
            abort(401, description="Unauthorized: Admin only route")

        return f(*args, **kwargs)

    return decorated


def getFrontendURL(slug):
    return os.getenv("FRONTEND_URL") + slug


def serialize(t, re=False, raw=False):
    t_dict = [i.to_dict(r=re) for i in t]
    if raw:
        return t_dict
    return jsonify(t_dict)


def getQuery(req: Request):
    return req.args


def abort_request(err_code: int, msg: str):
    response = make_response(jsonify({"message": msg}), err_code)
    return response


def send_forgot_mail(address, name, token):
    link = frontend_url + "/reset/" + token
    email = {
        "from": {
            "name": "Houc",
            "email": "support@household.yashkc.com",
        },
        "recipients": [
            {
                "name": name,
                "email": address,
            }
        ],
        "content": {
            "subject": "Reset your password",
            "text_body": "Click the link to reset your password " + link,
            "html_body": "Click the link to reset your password " + link,
        },
    }
    headers = {"X-Api-Key": app.config["API_KEY"], "Content-Type": "application/json"}
    r = requests.post(
        "https://api.ahasend.com/v1/email/send", json=email, headers=headers
    )
