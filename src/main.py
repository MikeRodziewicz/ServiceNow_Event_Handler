import os 
import time 
from dotenv import load_dotenv

from events import setup_incident_listeners
from app.connector import BasicSnowConnection
from app.incidents import monitor_for_new_incidents

# enable looking for env variables in the .env file 
load_dotenv()


SNOW_URL = os.getenv('SNOW_URL')
SNOW_USER = os.getenv('SNOW_USR')
SNOW_PWD =os.getenv('SNOW_PWD')


# Initialize connections
snow_connection = BasicSnowConnection(SNOW_URL, SNOW_USER, SNOW_PWD)


# Setup event listeners as required. 
setup_incident_listeners()



def main(connection=snow_connection):
    """main func in which you enable/disable handling records"""
    query_inc = 'state=1'

    monitor_for_new_incidents(connection=connection, query=query_inc)


if __name__ == '__main__':
    print('starting up...', flush=True)
    while True: 
        main()
        time.sleep(30)