import time 
import os 
from dotenv import load_dotenv

from events import setup_incident_listeners
from app.connector import BasicSnowConnection
from app.incidents import monitor_for_new_incidents

load_dotenv()

snow_url = os.getenv('SNOW_URL')
snow_user = os.getenv('SNOW_USR')
snow_pwd =os.getenv('SNOW_PWD')

snow_connection = BasicSnowConnection(snow_url, snow_user, snow_pwd)

setup_incident_listeners()



def main(connection=snow_connection):
    monitor_for_new_incidents(connection=connection)


if __name__ == '__main__':
    print('starting up...', flush=True)
    while True: 
        main()
        time.sleep(30)