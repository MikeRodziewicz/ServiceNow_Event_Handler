from dataclasses import dataclass

from pony.orm import *


@dataclass
class NewIncident:
    sys_id: str
    number: str

    def __repr__(self) -> str:
        return f'this is {self.number}'


db = Database()

class NewIncidentDB(db.Entity):
    sys_id = Required(str)
    number = Required(str)


db.bind(provider='sqlite', filename='../database.sqlite', create_db=True)
db.generate_mapping(create_tables=True)