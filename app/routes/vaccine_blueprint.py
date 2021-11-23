from flask import Blueprint
from app.controllers.vaccine_controller import get_vaccines, register_card

bp_vaccine = Blueprint("bp_vaccine", __name__)

bp_vaccine.post("/vaccinations")(register_card)
bp_vaccine.get("/vaccinations")(get_vaccines)