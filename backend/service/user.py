from flask import jsonify, g, abort, make_response, redirect
from sqlalchemy import and_
import jwt
import os
from database.models import User, ServiceProfessional, UserTypes, ServiceType, Tokens
from bcrypt import checkpw, hashpw, gensalt
from utils import utils
from nanoid import generate


def create_jwt(id: str, isProfessional: bool = False, isAdmin: bool = False):
    if isProfessional:
        user_details = {
            "userType": "professional",
            "id": id,
        }
    elif isAdmin:
        user_details = {
            "userType": "admin",
            "id": id,
        }
    else:
        user_details = {
            "userType": "user",
            "id": id
        }

    jwt_token = jwt.encode(user_details, os.getenv(
        'SECRET_KEY'), algorithm="HS256")
    return jwt_token


def login(email: str, password: str, isAdmin: bool = False):
    if isAdmin:
        user = g.db_session.query(User).filter(
            and_(User.email == email, User.user_type == UserTypes.ADMIN)).first()
        if not user:
            return utils.abort_request(401, "Invalid details")

    else:
        user = g.db_session.query(User).filter(
            and_(User.email == email, User.user_type == UserTypes.USER)).first()

        if not user:
            return jsonify({"error": "User not found"}), 404

    if checkpw(password.encode("utf-8"), user.password):
        token = create_jwt(
            user.id) if not isAdmin else create_jwt(user.id, isAdmin=True)
        if (isAdmin):
            response = make_response(jsonify({
                "message": "Welcome Admin",
                "redirect": utils.getFrontendURL("admin")
            }), 201)
            # response = make_response(redirect(utils.getFrontendURL("")))
            response.set_cookie("auth_token", token,
                                httponly=True, samesite="Lax")
            return response
        else:
            response = make_response(jsonify({
                "message": "Successfully logged in",
                "redirect": utils.getFrontendURL("")
            }), 201)
            # response = make_response(redirect(utils.getFrontendURL("")))
            response.set_cookie("auth_token", token,
                                httponly=True, samesite="Lax")
            return response

    return jsonify({"error": "Invalid credentials"}), 401


def professional_login(email: str, password: str):
    user = (
        g.db_session.query(ServiceProfessional)
        .filter(ServiceProfessional.email == email)
        .first()
    )

    if not user:
        return jsonify({"error": "User not found"}), 404

    if checkpw(password.encode("utf-8"), user.password):
        token = create_jwt(user.id, True)
        response = make_response(jsonify({
            "message": "Successfully logged in",
            "redirect": utils.getFrontendURL("professional/")
        }), 201)
        response.set_cookie("auth_token", token, httponly=True, samesite="Lax")
        return response

    return jsonify({"error": "Invalid credentials"}), 401


def register_user(name: str, password: str, phone: str, email: str, address: str, pincode: int):
    if len(pincode) != 6:
        return utils.abort_request(400, "Pincode should be 6 digits")

    if len(phone) != 10:
        return utils.abort_request(400, "Phone number should be 10 digits")

    if not (utils.checkPassword(password) and utils.checkEmail(email)):
        return utils.abort_request(400, "Invalid email or password format")

    existing_user = g.db_session.query(User).filter_by(
        email=email).first()

    if existing_user:
        return jsonify({"error": "User already exist"}), 400
    salt = gensalt()
    user = User(
        name=name, email=email, password=hashpw(password.encode("utf-8"), salt), pincode=pincode, address=address, phone=phone
    )
    g.db_session.add(user)
    g.db_session.commit()
    return jsonify({
        "message": "User created successfully, Please login",
        "redirect": utils.getFrontendURL("auth/login")
    }), 201


def register_as_professional(
    name: str,
    password: str,
    email: str,
    address: str,
    pincode: int,
    description: str,
    experience: int,
    service_type: str,
    file: str,
    phone: str
):
    if len(pincode) != 6:
        return utils.abort_request(400, "Pincode should be 6 digits")

    if len(phone) != 10:
        return utils.abort_request(400, "Phone number should be 10 digits")

    # TODO: validation not working as expected
    if not (utils.checkPassword(password) and utils.checkEmail(email)):
        return utils.abort_request(400, "Invalid email or password format")

    sType = g.db_session.query(ServiceType).filter_by(id=service_type).first()

    if not sType:
        abort(400, "Service Category doesn;t exist")
    salt = gensalt()

    original_extension = os.path.splitext(file.filename)[1]
    new_filename = generate() + original_extension
    file_path = os.path.join("./files/", new_filename)
    file.save(file_path)

    user = ServiceProfessional(
        name=name,
        email=email,
        password=hashpw(password.encode("utf-8"), salt),
        address=address,
        pincode=pincode,
        proof_document=new_filename,
        description=description,
        experience=experience,
        service_type=sType,
        phone=phone
    )

    g.db_session.add(user)
    g.db_session.commit()
    return jsonify({
        "message": "Service Professional created successfully, Please login",
        "redirect": utils.getFrontendURL("auth/professional/login")
    }), 201


def update_password(
    user_id: str, new_password: str, old_password: str, isProfessional: bool = False
):

    if isProfessional:
        user = g.db_session.query(ServiceProfessional).get(user_id)
    else:
        user = g.db_session.query(User).get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not checkpw(old_password.encode("utf-8"), user.password):
        return jsonify({"error": "Invalid old password"}), 401

    if not utils.checkPassword(new_password):
        return jsonify({"error": "Invalid new password"}), 400

    user.password = hashpw(new_password.encode("utf-8"), gensalt())
    g.db_session.commit()
    return jsonify({"message": "Password updated successfully"}), 200


def get_user_details(user_id: str):
    user = g.db_session.query(User).get(user_id)

    if not user:
        abort(404, description="User not found")

    return user


def get_professional_details(user_id: str):
    user = g.db_session.query(ServiceProfessional).get(user_id)

    if not user:
        abort(404, description="User not found")

    return user


def update_profile_user(name: str, email: str, address: str, pincode: str, user_id: str):
    user = g.db_session.query(User).get(user_id)
    user.name = name
    user.email = email
    user.address = address
    user.pincode = pincode
    g.db_session.commit()

    return jsonify({"message": "profile updated successfully"}), 201


def forgot_password(owner_id: str, user_type: str):
    token = Tokens(owner_id=owner_id)

    if user_type == "user":
        user = g.db_session.query(User).filter(User.id == owner_id).first()
    else:
        user = g.db_session.query(ServiceProfessional).filter(
            ServiceProfessional.id == owner_id).first()

    utils.send_forgot_mail(user.email, user.name, token.id)
    g.db_session.commit()
