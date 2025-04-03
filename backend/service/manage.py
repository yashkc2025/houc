from flask import jsonify, g, abort, send_file, make_response
from database.models import Service, User, ServiceProfessional, ServiceType, UserTypes, ServiceRequest, RequestStatus
from sqlalchemy import update, delete, select, or_, func, and_
from sqlalchemy.future import select
from utils import utils
import os


# create, update and delete service
# block accounts
# view all user and professional
# approve service professional

def create_service(name: str, price: int, time_required: int, description: str, service_type: str):
    sType = g.db_session.query(ServiceType).filter_by(id=service_type).first()

    if not sType:
        abort(400, "Service Category doesn;t exist")
    new_service = Service(
        name=name, price=price, time_required=time_required, description=description, service_type=sType
    )
    g.db_session.add(new_service)
    g.db_session.commit()

    return jsonify({"message": "Service created successfully", "redirect": "services"}), 201


def delete_service(service_id: str):
    try:
        service = g.db_session.query(Service).get(service_id)
        service.is_active = False

        g.db_session.commit()
        return jsonify({"message": "Service deleted successfully"}), 201
    except Exception as e:
        g.db_session.rollback()
        g.db_session.close()

        return jsonify({"message": e}), 500


def update_service(name: str, price: float, time_required: int, description: str, service_id: str):
    service = g.db_session.query(Service).get(service_id)

    if name:
        service.name = name
    if price:
        service.price = price
    if time_required:
        service.time_required = time_required
    if description:
        service.description = description

    g.db_session.commit()
    return jsonify({"message": "Service updated successfully"}), 200

# TODO


def list_customers(search_text: str = None):
    if search_text:
        customers = g.db_session.query(User).filter(
            or_(
                User.name.ilike(f'%{search_text}%'),
                User.email.ilike(f'%{search_text}%'),
                User.pincode == search_text,
                User.id == search_text,
                User.address.ilike(f'%{search_text}%')
            )).all()
    else:
        customers = g.db_session.query(User).filter(
            User.user_type != UserTypes.ADMIN).all()

    print("******")
    print(customers)
    return utils.serialize(customers)

# TODO


def list_professionals(search_text: str = None, category: str = None):
    if search_text:
        professionals = g.db_session.query(ServiceProfessional).filter(
            or_(
                ServiceProfessional.name.ilike(f'%{search_text}%'),
                ServiceProfessional.email.ilike(f'%{search_text}%'),
                ServiceProfessional.address.ilike(f'%{search_text}%'),
                ServiceProfessional.pincode == search_text,
                ServiceProfessional.id == search_text,
            )).all()
    elif (category):
        professionals = g.db_session.query(ServiceProfessional).join(ServiceType,
                                                                     ServiceProfessional.service_type_id == ServiceType.id).filter(ServiceType.name == category).all()
    else:
        professionals = g.db_session.query(ServiceProfessional).all()

    print("***")
    print(professionals)

    return utils.serialize(professionals, re=True)


def block_customer(user_id: str):
    try:
        g.db_session.execute(
            update(User).where(User.id == user_id).values(is_blocked=True)
        )

        g.db_session.commit()

    except Exception as e:
        g.db_session.rollback()

    g.db_session.close()
    return jsonify({
        "message": "User blocked successfully"
    }), 201


def block_professional(professional_id: str):
    try:
        g.db_session.execute(
            update(ServiceProfessional)
            .where(ServiceProfessional.id == professional_id)
            .values(is_blocked=True)
        )

        g.db_session.commit()

    except Exception as e:
        g.db_session.rollback()

    g.db_session.close()
    return jsonify({
        "message": "Professional blocked successfully"
    }), 201


def unblock_customer(user_id: str):
    try:
        g.db_session.execute(
            update(User).where(User.id == user_id).values(is_blocked=False)
        )

        g.db_session.commit()

    except Exception as e:
        g.db_session.rollback()

    g.db_session.close()
    return jsonify({
        "message": "User unblocked successfully"
    }), 201


def unblock_professional(professional_id: str):
    try:
        g.db_session.execute(
            update(ServiceProfessional)
            .where(ServiceProfessional.id == professional_id)
            .values(is_blocked=False)
        )

        g.db_session.commit()

    except Exception as e:
        g.db_session.rollback()

    g.db_session.close()
    return jsonify({
        "message": "Professional unblocked successfully"
    }), 201


def list_unverified_professionals():
    unverified_professionals = (
        g.db_session.query(ServiceProfessional)
        .filter(ServiceProfessional.is_approved == False)
        .order_by(ServiceProfessional.name)
    )

    return unverified_professionals


def approve_professional(id: str):
    try:
        g.db_session.execute(
            update(ServiceProfessional)
            .where(ServiceProfessional.id == id)
            .values(is_approved=True)
        )

        g.db_session.commit()

    except Exception as e:
        g.db_session.rollback()

    g.db_session.close()


def get_summary():
    service = g.db_session.execute(select(func.count(Service.id))).scalar()
    pending_requests = g.db_session.execute(
        select(func.count(ServiceRequest.id)).where(
            or_(
                ServiceRequest.request_status == RequestStatus.ACCEPTED,
                ServiceRequest.request_status == RequestStatus.REQUESTED
            )
        )
    ).scalar()
    completed_requests = g.db_session.execute(
        select(func.count(ServiceRequest.id)).where(
            ServiceRequest.request_status == RequestStatus.COMPLETED
        )
    ).scalar()
    customers = g.db_session.execute(
        select(func.count(User.id)).where(
            User.user_type == UserTypes.USER
        )
    ).scalar()
    verified_professionals = g.db_session.execute(
        select(func.count(ServiceProfessional.id)).where(
            ServiceProfessional.is_approved == True
        )
    ).scalar()
    unverified_professionals = g.db_session.execute(
        select(func.count(ServiceProfessional.id)).where(
            ServiceProfessional.is_approved == False
        )
    ).scalar()

    return {
        "Services": service,
        "Pending Requests": pending_requests,
        "Completed Requests": completed_requests,
        "Users": customers,
        "Verified Professionals": verified_professionals,
        "Unverified Professionals": unverified_professionals
    }


def get_requests():
    s_req = g.db_session.query(ServiceRequest).filter().all()
    data = utils.serialize(s_req, re=True, raw=True)

    return [{
        "date_created": x['date_created'],
        "date_completed": x['date_completed'],
        "id": x['id'],
        "status": x["request_status"],
        "name": x['service']['name'],
        'price': x['service']['price'],
        "professional_email": x['service_professional']['email'],
        "user_email": x['user']['email'],

    } for x in data]


def approve_professional(prof_id: str):

    g.db_session.execute(
        update(ServiceProfessional).where(
            ServiceProfessional.id == prof_id).values(is_approved=True)
    )

    g.db_session.commit()

    return jsonify({
        "message": "Professional approved successfully"
    }), 201


def get_doc(prof_id: str):
    prof = g.db_session.query(ServiceProfessional).filter(
        ServiceProfessional.id == prof_id).first()

    file_path = os.path.join("./files/", prof.proof_document)

    response = make_response(send_file(file_path, as_attachment=True))
    response.headers['Access-Control-Expose-Headers'] = "Content-Disposition"
    return response
