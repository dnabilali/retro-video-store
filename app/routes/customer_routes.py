from app import db
from app.models.customer import Customer
from app.routes.helpers import validate_model, validate_request_body
from flask import Blueprint, jsonify, request, make_response, abort
import datetime


customers_bp = Blueprint("customers_bp", __name__, url_prefix="/customers")


@customers_bp.route("", methods=["GET"])
def get_all_customers():
    customers = Customer.query.all()
    customers_response = []

    for customer in customers:
        customers_response.append({
            "id": customer.id,
            "name": customer.name,
            "postal_code": customer.postal_code,
            "phone": customer.phone,
            "registered_at": customer.registered_at,
            "videos_checked_out_count": customer.videos_checked_out_count
        })

    return make_response(jsonify(customers_response), 200)


@customers_bp.route("/<customer_id>", methods=["GET"])
def get_one_customer(customer_id):
    customer = validate_model(Customer, customer_id)
    customer_data = {
            "id": customer.id,
            "name": customer.name,
            "postal_code": customer.postal_code,
            "phone": customer.phone,
            "registered_at": customer.registered_at,
            "videos_checked_out_count": customer.videos_checked_out_count
    }

    return make_response(jsonify(customer_data), 200)


@customers_bp.route("", methods=["POST"])
def add_one_customer():
    request_body = request.get_json()
    required_attributes = ["name", "postal_code", "phone"]

    validate_request_body(request_body, required_attributes)
    
    new_customer = Customer(name=request_body["name"], 
            postal_code=request_body["postal_code"],
            phone=request_body["phone"])

    db.session.add(new_customer)
    db.session.commit()
    db.session.refresh(new_customer, ["id"])

    return make_response(jsonify({"id":new_customer.id}), 201)


@customers_bp.route("/<customer_id>", methods=["DELETE"])
def delete_one_customer(customer_id):
    customer = validate_model(Customer, customer_id)
    db.session.delete(customer)
    db.session.commit()
    
    return make_response(jsonify({"id":int(customer_id)}), 200)


@customers_bp.route("/<customer_id>", methods=["PUT"])
def update_one_customer(customer_id):
    customer = validate_model(Customer, customer_id)
    request_body = request.get_json()
    required_attributes = ["name", "phone", "postal_code"]

    validate_request_body(request_body, required_attributes)
    
    customer.name = request_body["name"]
    customer.phone = request_body["phone"]
    customer.postal_code = request_body["postal_code"]
    db.session.commit()
    response_body = request_body
    response_body['registered_at'] = customer.registered_at

    return make_response(jsonify(response_body), 200)