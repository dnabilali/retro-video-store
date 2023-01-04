from app import db
from app.models.customer import Customer
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


def validate_id(customer_id):
    try:
        int(customer_id)
    except:
        abort(make_response({"message": f"{customer_id} is an invalid customer id"}, 400))

    customer = Customer.query.get(customer_id)

    if not customer:
        abort(make_response({"message": f"Customer {customer_id} was not found"}, 404))
    
    return customer


@customers_bp.route("/<customer_id>", methods=["GET"])
def get_one_customer(customer_id):
    customer = validate_id(customer_id)
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

    for attr in required_attributes:
        if attr not in request_body:
            abort(make_response(jsonify({"details": f"Request body must include {attr}."}), 400))

    new_customer = Customer(name=request_body["name"], 
            postal_code=request_body["postal_code"],
            phone=request_body["phone"])

    db.session.add(new_customer)
    db.session.commit()
    db.session.refresh(new_customer, ["id"])

    return make_response(jsonify({"id":new_customer.id}), 201)


@customers_bp.route("/<customer_id>", methods=["DELETE"])
def delete_one_customer(customer_id):
    customer = validate_id(customer_id)
    db.session.delete(customer)
    db.session.commit()
    
    return make_response(jsonify({"id":int(customer_id)}), 200)


@customers_bp.route("/<customer_id>", methods=["PUT"])
def update_one_customer(customer_id):
    customer = validate_id(customer_id)
    request_body = request.get_json()
    required_attributes = ["name", "phone", "postal_code"]

    for attr in required_attributes:
        if attr not in request_body or type(request_body[attr]) is not str:
            abort(make_response(jsonify({"message":f"{attr} is necessary to update a customer"}), 400))

    customer.name = request_body["name"]
    customer.phone = request_body["phone"]
    customer.postal_code = request_body["postal_code"]
    db.session.commit()
    response_body = request_body
    response_body['registered_at'] = customer.registered_at

    return make_response(jsonify(response_body), 200)