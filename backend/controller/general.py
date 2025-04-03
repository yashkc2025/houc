from flask import Blueprint, jsonify, request
from utils.utils import verifyPayload, getUserID, token_required_customer, getQuery, token_required_professional
import service.general as generalService
from typing import Dict, Any

generalController = Blueprint("general", __name__)


def createRoute(slug: str):
    return "/general/" + slug


@generalController.route(createRoute("get_service_types"), methods=['GET'])
def get_service_types():
    return generalService.get_service_types()


@token_required_customer
@generalController.route(createRoute("get_services"), methods=['GET'])
def get_services():
    query = getQuery(request)
    return generalService.get_services(**query)


@token_required_customer
@generalController.route(createRoute("book_service"), methods=['POST'])
@verifyPayload(["professional_id", "service_id"])
def book_service(payload: Dict[str, Any]):
    user_id = getUserID()
    return generalService.book_service(**payload, user_id=user_id)


@token_required_customer
@generalController.route(createRoute("close_request"), methods=["POST"])
@verifyPayload(['request_id', 'rating', 'review_text'])
def close_request(payload: Dict[str, Any]):
    user_id = getUserID()
    return generalService.close_service_request(**payload, user_id=user_id)


@token_required_customer
@generalController.route(createRoute("get_history"), methods=["GET"])
def service_history():
    user_id = getUserID()
    return generalService.get_service_history(user_id=user_id)


@token_required_professional
@generalController.route(createRoute("get_requests"), methods=['GET'])
def get_requests():
    professional_id = getUserID()
    return generalService.get_requests(professional_id=professional_id)


@generalController.route(createRoute("accept_request"), methods=["POST"])
@token_required_professional
@verifyPayload(["service_id"])
def accept_request(payload):
    return generalService.accept_request(**payload)


@generalController.route(createRoute("reject_request"), methods=["POST"])
@verifyPayload(["service_id"])
def reject_request(payload):
    user_id = getUserID()
    # return user_id
    return generalService.reject_request(**payload)


@generalController.route(createRoute("professional_summary"), methods=["GET"])
@token_required_professional
def professional_summary():
    prof_id = getUserID()
    return generalService.professional_summary(prof_id)
