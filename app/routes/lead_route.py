from flask import Blueprint, Flask
from app.controllers import lead_controller

bp = Blueprint("leads", __name__, url_prefix="/leads")

bp.get("")(lead_controller.get_leads)
bp.post("")(lead_controller.post_lead)
bp.patch("")(lead_controller.update_lead)
bp.delete("")(lead_controller.delete_lead)