import os
from dotenv import load_dotenv

import unittest
from src.app.incidents import incident_to_model, monitor_for_new_incidents
from src.app.connector import BasicSnowConnection
from pony.orm import *
from src.app.models import NewIncidentDB




class IncidentTestCase(unittest.TestCase):
    """Testing functionalities related to handling incidents"""

    def setUp(self) -> None:
        load_dotenv()
        self.base_url = os.getenv('SNOW_URL')
        self.snow_usr = os.getenv('SNOW_USR')
        self.snow_pwd = os.getenv('SNOW_PWD')
        self.connection = BasicSnowConnection(self.base_url, self.snow_usr, self.snow_pwd)
        os.environ['CONFIG'] = 'TEST'
    

    def test_creation_connection_obj(self):
        self.assertIsInstance(self.connection,BasicSnowConnection)


    def test_getting_single_incident(self):
        test_inc_number = 'INC0008111'
        response = self.connection.get_single_incident(test_inc_number)

        self.assertNotEqual(response['result'], [])
        self.assertIn(test_inc_number,response['result'][0]['number'])


    def test_getting_multiple_incidents(self):
        response = self.connection.get_multiple_incident(sysparm_limit=5)
        incident_one = response['result'][0]
        incident_two = response['result'][1]
        
        self.assertEqual(len(response['result']), 5)
        self.assertIn('incident', response['result'][0]['sys_class_name'])
        self.assertNotEqual(incident_one, incident_two)


    def test_monitor_for_new_incidents(self):
        test_query = 'state=1'
        test_query_two = 'state=11'

        resp = monitor_for_new_incidents(connection=self.connection, query=test_query)
        self.assertEqual(resp, "New Incidents")

        resp_two = monitor_for_new_incidents(connection=self.connection, query=test_query_two)
        self.assertEqual(resp_two, "No Incidents")


    def test_incident_to_model(self):
        test_new_incidents = self.connection.get_multiple_incident(sysparm_limit=5)
        resp = incident_to_model(new_incidents=test_new_incidents)
        
        self.assertIsInstance(resp, NewIncidentDB)
        self.assertTrue(hasattr(resp, 'sys_id'))
        self.assertTrue(hasattr(resp, 'number'))
        self.assertFalse(hasattr(resp, 'size'))
        