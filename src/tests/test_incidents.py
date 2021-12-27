import os
from dotenv import load_dotenv

import unittest
from src.app.incidents import incident_to_model, monitor_for_new_incidents
from src.app.connector import BasicSnowConnection

class IncidentTestCase(unittest.TestCase):
    """Testing functionalities related to handling incidents"""

    def setUp(self) -> None:
        load_dotenv()
        self.base_url = os.getenv('BASE_URL')
        self.snow_usr = os.getenv('SNOW_USR')
        self.snow_pwd = os.getenv('SNOW_PWD')
        self.connection = BasicSnowConnection(self.base_url, self.snow_usr, self.snow_pwd)

    def test_creation_connection_obj(self):
        self.assertIsInstance(self.connection,BasicSnowConnection)