import time 
import os 
from dotenv import load_dotenv

from events import setup_incident_listeners
from app.connector import BasicSnowConnection 

load_dotenv()

snow_url = os.getenv('SNOW_URL')
snow_user = os.getenv('SNOW_USR')
snow_pwd =os.getenv('SNOW_PWD')

snow_connection = BasicSnowConnection(snow_url, snow_user, snow_pwd)

response = snow_connection.get_single_incident('INC0008111')

print(response)