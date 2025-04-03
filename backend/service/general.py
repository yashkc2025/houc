from flask import jsonify, g
from database.models import Service, ServiceRequest, User, RequestStatus, Review, ServiceType, ServiceProfessional
from datetime import datetime
from utils import utils
from sqlalchemy import and_, func, select, or_
# list and search services
# book and edit a service request
# mark service as completed
# service history


def get_service_types():
    service_types = g.db_session.query(ServiceType).all()
    return utils.serialize(service_types, re=True)


def get_services(search_text: str = None, category: str = None):
    if (search_text):
        services = g.db_session.query(Service).filter(
            and_(
                Service.name.ilike(f'%{search_text}%'),
                Service.is_active == True
            )).all()
    elif (category):
        services = g.db_session.query(Service).join(ServiceType,
                                                    Service.service_type_id == ServiceType.id).filter(and_(
                                                        ServiceType.name == category,
                                                        Service.is_active == True
                                                    )).all()
    else:
        services = g.db_session.query(Service).filter(
            Service.is_active == True
        ).all()
    return utils.serialize(services, re=True)


def book_service(professional_id: str, user_id: str, service_id: str):
    prof = g.db_session.query(ServiceProfessional).filter(
        ServiceProfessional.id == professional_id).first()
    user = g.db_session.query(User).filter(User.id == user_id).first()
    service = g.db_session.query(Service).filter(
        Service.id == service_id).first()
    request = ServiceRequest(
        service_professional=prof,
        service=service,
        user=user
    )

    g.db_session.add(request)
    g.db_session.commit()

    return jsonify({"message": "Service booked successfully"}), 201


def close_service_request(request_id: str, rating: int, review_text: str, user_id: str):
    request = g.db_session.query(ServiceRequest).get(request_id)
    request.request_status = RequestStatus.COMPLETED
    request.date_completed = datetime.now()

    user = g.db_session.query(User).get(user_id)
    professional = g.db_session.query(ServiceProfessional).get(
        request.service_professional_id)
    review = Review(rating=rating, review=review_text, user=user,
                    request=request, service_professional=professional)
    g.db_session.add(review)
    g.db_session.commit()

    g.db_session.close()
    return jsonify({"message": "Service closed successfully"}), 201


def get_service_history(user_id: str):
    services = g.db_session.query(ServiceRequest).filter(
        ServiceRequest.user_id == user_id
    ).all()

    return utils.serialize(services, re=True)


def get_requests(professional_id: str):
    s_req = g.db_session.query(ServiceRequest).filter(
        ServiceRequest.service_professional_id == professional_id).all()

    return utils.serialize(s_req, re=True)


def accept_request(service_id: str):
    s_req = g.db_session.query(ServiceRequest).filter(
        ServiceRequest.id == service_id).first()

    s_req.request_status = RequestStatus.ACCEPTED
    g.db_session.commit()
    return jsonify({"message": "Request accepted successfully"}), 200


def reject_request(service_id: str):
    s_req = g.db_session.query(ServiceRequest).filter(
        ServiceRequest.id == service_id).first()

    print("$$$")
    print(s_req)
    s_req.request_status = RequestStatus.REJECTED
    g.db_session.commit()
    return jsonify({"message": "Request rejected successfully"}), 200


def professional_summary(prof_id: str):
    pending_requests = g.db_session.execute(
        select(func.count(ServiceRequest.id)).where(
            and_(
                or_(
                    ServiceRequest.request_status == RequestStatus.ACCEPTED,
                    ServiceRequest.request_status == RequestStatus.REQUESTED
                ),
                ServiceRequest.service_professional_id == prof_id
            )
        )
    ).scalar()
    completed_requests = g.db_session.execute(
        select(func.count(ServiceRequest.id)).where(
            ServiceRequest.request_status == RequestStatus.COMPLETED,
            ServiceRequest.service_professional_id == prof_id
        )
    ).scalar()

    rejected_requests = g.db_session.execute(
        select(func.count(ServiceRequest.id)).where(
            ServiceRequest.request_status == RequestStatus.REJECTED,
            ServiceRequest.service_professional_id == prof_id
        )
    ).scalar()

    return {
        "Pending Requests": pending_requests,
        "Completed Requests": completed_requests,
        "Rejected Requests": rejected_requests,
    }
