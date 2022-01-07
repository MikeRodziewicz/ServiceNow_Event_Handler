import os
from dataclasses import dataclass

from dotenv import load_dotenv
from pony.orm import *


# enable looking for DB env variables in the .env file
load_dotenv()
CONFIG = os.getenv("CONFIG")
# DB_USER = os.getenv("MYSQL_ROOT_PASSWORD")
DB_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")


@dataclass
class NewIncident:
    sys_id: str
    number: str

    def __repr__(self) -> str:
        return f"this is {self.number}"


# DB - Initialize DB connection and return db object.
db = Database()


# Declaration of a model for new incidents
class NewIncidentDB(db.Entity):
    sys_id = Required(str)
    number = Required(str)


# Bind, create DB and tables depending on the config in use
if CONFIG == "PROD":
    print("this would have been a prod config")
    db.bind(
        provider="mysql",
        host="mysqldb",
        user="root",
        passwd=DB_PASSWORD,
        db="mysql",
    )
    db.generate_mapping(create_tables=True)
elif CONFIG == "DEV":
    db.bind(provider="sqlite", filename="../database.sqlite", create_db=True)
    db.generate_mapping(create_tables=True)
elif CONFIG == "TEST":
    db.bind(provider="sqlite", filename=":memory:")
    db.generate_mapping(create_tables=True)
