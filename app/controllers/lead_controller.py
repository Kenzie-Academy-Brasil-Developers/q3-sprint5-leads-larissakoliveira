from itsdangerous import json
from sqlalchemy import desc
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session
from http import HTTPStatus
from flask import jsonify, request
from app.configs.database import db
from app.models.lead_model import Lead
from sqlalchemy.exc import IntegrityError
import re


#PATCH
#DELETE

def get_leads():

    session: Session = db.session
    base_query = session.query(Lead)

    leads = base_query.order_by(desc(Lead.visits)).all()

    if len(leads) == 0:
        return {"error": "No result found"}, HTTPStatus.NOT_FOUND
    
    return jsonify({"LEADS": leads}), HTTPStatus.OK


def post_lead():
    valid_keys = {"name", "email", "phone"}
    data = request.get_json()
    body_keys = set(data.keys())
    missing_keys = valid_keys.difference(body_keys)

    try:

        if re.fullmatch(r"^\([1-9]{2}\)[0-9]{5}-[0-9]{4}$", data["phone"]) == None:
            return {"error": "phone number format is wrong!"}

        if len(data) != 3 or missing_keys:
            raise KeyError

        for value in data.values():
            if type(value) != str:
                return {"error": "values must be string!"}

        lead = Lead(**data)
        db.session.add(lead)
        db.session.commit()

    except IntegrityError:
        return {"error": "email or/and phone already exists"}, HTTPStatus.CONFLICT
    except KeyError:
        return {"error": "the keys must be name, email and phone"}, HTTPStatus.BAD_REQUEST

    return jsonify(lead), HTTPStatus.CREATED

def update_lead():
    session: Session = db.session
    base_query = session.query(Lead)

    data = request.get_json()

    lead = base_query.filter_by(email = data).first()

    return jsonify(lead)

    # record = session.query(CallRecord).filter(CallRecord.id == call_record_id).first()
    # record = session.query(CallRecord).get(call_record_id)
    # record = base_query.filter_by(id=call_record_id).first()
    # record = base_query.filter_by(source=111111113).all()


def delete_lead():
    ...
