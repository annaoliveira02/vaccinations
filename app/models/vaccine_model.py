from datetime import datetime, timedelta
from sqlalchemy import Column, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.configs.database import db
from app.exceptions.exceptions import InvalidCPFError, InvalidKeysError, InvalidTypeError, InvalidUniqueKey
from dataclasses import dataclass

@dataclass
class Vaccine(db.Model):
    cpf: str
    name: str
    first_shot_date: int
    second_shot_date: int
    vaccine_name:str
    health_unit_name:str

    date = datetime.utcnow()
    days = timedelta(days=90)

    __tablename__ = "vaccine_cards"

    cpf = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    first_shot_date = Column(TIMESTAMP, default=datetime.utcnow())
    second_shot_date = Column(TIMESTAMP, default=days+date)
    vaccine_name = Column(String, nullable=False)
    health_unit_name = Column(String)

    @staticmethod
    def validate(data):

        valid_args = ["cpf", "name", "vaccine_name", "health_unit_name"]

        for item in valid_args:
            if item not in data.keys():
                raise InvalidKeysError
        
        for item in data.values():
            if type(item) is not str:
                raise InvalidTypeError

        if len(data["cpf"]) != 11:
            raise InvalidCPFError

        unique_key = (
            Vaccine
            .query
            .filter(Vaccine.cpf==data["cpf"])
            .one_or_none()
        )

        if unique_key is not None:
            raise InvalidUniqueKey
        

                


        