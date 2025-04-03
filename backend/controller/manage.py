from flask import Blueprint, jsonify, request
from utils.utils import verifyPayload, verifyFormPayload, getQuery, adminOnlyRoute
import service.manage as manageService
from typing import Dict, Any

adminController = Blueprint("manage", __name__)


def createRoute(slug: str):
    return "/manage/" + slug


@adminController.route(createRoute("create_service"), methods=['POST'])
@adminOnlyRoute
@verifyFormPayload(["name", "price", "time_required", "description", "service_type"])
def create_service(payload: Dict[str, Any]):
    return manageService.create_service(**payload)


@adminController.route(createRoute("delete_service"), methods=['POST'])
@adminOnlyRoute
@verifyPayload(["service_id"])
def delete_service(payload: Dict[str, Any]):
    return manageService.delete_service(**payload)


@adminController.route(createRoute("update_service"), methods=['UPDATE'])
@adminOnlyRoute
@verifyPayload(["name", "price", "time_required", "description", "service_id"])
def update_service(payload: Dict[str, Any]):
    return manageService.update_service(**payload)


@adminController.route(createRoute("list_customers"), methods=['GET'])
@adminOnlyRoute
def list_customers():
    query = getQuery(request)
    return manageService.list_customers(**query)


@adminController.route(createRoute("list_professionals"), methods=['GET'])
def list_professionals():
    query = getQuery(request)
    return manageService.list_professionals(**query)


@adminController.route(createRoute("get_summary"), methods=['GET'])
@adminOnlyRoute
def get_summary():
    return manageService.get_summary()


@adminController.route(createRoute("block_user"), methods=['POST'])
@adminOnlyRoute
@verifyPayload(['user_id'])
def block_user(payload):
    return manageService.block_customer(**payload)


@adminController.route(createRoute("block_professional"), methods=['POST'])
@adminOnlyRoute
@verifyPayload(['professional_id'])
def block_professional(payload):
    return manageService.block_professional(**payload)


@adminController.route(createRoute("unblock_user"), methods=['POST'])
@adminOnlyRoute
@verifyPayload(['user_id'])
def unblock_user(payload):
    return manageService.unblock_customer(**payload)


@adminController.route(createRoute("unblock_professional"), methods=['POST'])
@adminOnlyRoute
@verifyPayload(['professional_id'])
def unblock_professional(payload):
    return manageService.unblock_professional(**payload)


@adminController.route(createRoute("approve_professional"), methods=['POST'])
@adminOnlyRoute
@verifyPayload(['prof_id'])
def approve_professional(payload):
    return manageService.approve_professional(**payload)


@adminController.route(createRoute("get_doc"), methods=['GET'])
# @adminOnlyRoute
def get_doc():
    query = getQuery(request)
    return manageService.get_doc(**query)


@adminController.route(createRoute("get_requests"), methods=['GET'])
@adminOnlyRoute
def get_requests():
    return manageService.get_requests()
