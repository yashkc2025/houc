from flask import Blueprint, jsonify, request, abort, make_response
from utils.utils import verifyPayload, getUserID, verifyFormPayload
from typing import Dict, Any
import service.user as userService

userController = Blueprint("user", __name__)


def createUserRoute(slug: str):
    return "/user/" + slug


@userController.route(createUserRoute("admin_login"), methods=["POST"])
@verifyFormPayload(["email", "password"])
def login_admin(payload: Dict[str, Any]):
    return userService.login(**payload, isAdmin=True)


@userController.route(createUserRoute("user_register"), methods=["POST"])
@verifyFormPayload(["name", "email", "password", "address", "pincode", "phone"])
def register_user(payload: Dict[str, Any]):
    return userService.register_user(**payload)

# Tested


@userController.route(createUserRoute("user_login"), methods=["POST"])
@verifyFormPayload(["email", "password"])
def login_user(payload: Dict[str, Any]):
    return userService.login(**payload)


# # TODO : Email to be sent after registration


@userController.route(createUserRoute("professional_register"), methods=["POST"])
@verifyFormPayload(["name", "email", "password", "address", "pincode", "description", "experience", "service_type", "phone"])
def register(payload: Dict[str, Any]):
    file = request.files['proof_document']
    if not file:
        abort(400, description=f"Unauthorized: Missing verification documnet")
    return userService.register_as_professional(**payload, file=file)


@userController.route(createUserRoute("professional_login"), methods=["POST"])
@verifyFormPayload(["email", "password"])
def login(payload: Dict[str, Any]):
    return userService.professional_login(**payload)


@userController.route(createUserRoute("update_profile_user"), methods=["POST"])
@verifyFormPayload(["name", "email", "address", "pincode"])
def update_password(payload: Dict[str, Any]):
    user_id = getUserID()
    return userService.update_profile_user(
        **payload, user_id=user_id
    )


@userController.route(createUserRoute("user_update_password"), methods=["POST"])
@verifyPayload(["new_password", "old_password"])
def update_password_user(payload: Dict[str, Any]):
    user_id = getUserID()
    return userService.update_password(
        user_id, payload["new_password"], payload["old_password"]
    )


# @userController.route(createUserRoute("professional_update_password"), methods=["POST"])
# @verifyPayload(["new_password", "old_password"])
# def update_password(payload: Dict[str, Any]):
#     professional_id = getUserID()
#     return userService.update_password(
#         professional_id, payload["new_password"], payload["old_password"]
#     )


@userController.route(createUserRoute("get_user_details"), methods=["GET"])
def get_user_details():
    user_id = getUserID()

    user = userService.get_user_details(user_id)

    return (
        jsonify(
            {
                "name": user.name,
                "email": user.email,
                "created_at": user.date_created,
                "updated_at": user.date_updated,
                "address": user.address,
                "pincode": user.pincode,
                "role": user.user_type.name,
            }
        ),
        200,
    )


@userController.route(createUserRoute("get_professional_details"), methods=["GET"])
def get_professional_details():
    professional_id = getUserID()

    user = userService.get_professional_details(professional_id)

    return (
        jsonify(
            {
                "name": user.name,
                "email": user.email,
                "created_at": user.date_created,
                "updated_at": user.date_updated,
                "role": user.user_type.name,
            }
        ),
        200,
    )


@userController.route(createUserRoute("logout"), methods=["GET"])
def logout():
    response = make_response(jsonify({"redirect": "/"}))

    for cookie in request.cookies:
        response.delete_cookie(cookie)

    return response
