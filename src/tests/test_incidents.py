import os
from dotenv import load_dotenv

import unittest
from src.app.incidents import incident_to_model, monitor_for_new_incidents
from src.app.connector import BasicSnowConnection

class IncidentTestCase(unittest.TestCase):
    """Testing functionalities related to handling incidents"""

    def setUp(self) -> None:
        load_dotenv()
        self.base_url = os.getenv('SNOW_URL')
        self.snow_usr = os.getenv('SNOW_USR')
        self.snow_pwd = os.getenv('SNOW_PWD')
        self.connection = BasicSnowConnection(self.base_url, self.snow_usr, self.snow_pwd)

    def test_creation_connection_obj(self):
        self.assertIsInstance(self.connection,BasicSnowConnection)

    def test_getting_single_incident(self):
        test_inc_number = 'INC0008111'
        response = self.connection.get_single_incident(test_inc_number)

        self.assertNotEqual(response['result'], [])
        self.assertIn(test_inc_number,response['result'][0]['number'])

    def test_getting_multiple_incidents(self):
        response = self.connection.get_multiple_emails(sysparm_limit=5)
        pass