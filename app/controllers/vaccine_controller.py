from flask import request, current_app, jsonify
from app.exceptions.exceptions import InvalidCPFError, InvalidKeysError, InvalidTypeError, InvalidUniqueKey
from app.models.vaccine_model import Vaccine


def register_card():
    data = request.get_json()
    try:        
        Vaccine.validate(data)
        formatted_data = {k: v.upper() for k,v in data.items()}
        valid_args = ["cpf", "name", "vaccine_name", "health_unit_name"]    
    
        for i in list(formatted_data.keys()):
            if i not in valid_args:
                del formatted_data[i]

        vaccine = Vaccine(**formatted_data)
        current_app.db.session.add(vaccine)
        current_app.db.session.commit()

        return {
            "cpf": vaccine.cpf,
            "name": vaccine.name.title(),
            "first_shot_date": vaccine.first_shot_date,
            "second_shot_date": vaccine.second_shot_date,
            "vaccine_name": vaccine.vaccine_name.title(),
            "health_unit_name": vaccine.health_unit_name.title()
        }, 201

    except InvalidCPFError:
        return {"message": "CPF inválido. Insira apenas os 11 números."}, 400
    except InvalidKeysError:
        return {"message": "Campos inválidos ou inexistentes"}, 400
    except InvalidTypeError:
        return {"message": "Formato de dados inválido"}, 400
    except InvalidUniqueKey:
        return {"message": "O CPF já existe"}, 409

def get_vaccines():
    return jsonify(Vaccine.query.all()), 200
