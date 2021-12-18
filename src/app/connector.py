"""
    Module to handle connection to the ServiceNow instance. 
    It provides a Connection class, that can be instantiatied with required credentials. 

"""

import requests


class BasicSnowConnection():

    def __init__(self, snow_url, user, password) -> None:
        """ make an instance of the connection object """
        self.snow_url = snow_url
        self.user = user
        self.password = password
        self.payload = None
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }


    def _make_connection(self, method, url, **kwargs):
        """ Func to send the request to the API """
        
        try: 
            self.response = requests.request(auth=(self.user, self.password), 
                                            method=method, 
                                            url=url, 
                                            headers=self.headers, 
                                            json=self.payload, 
                                            **kwargs)
            if self.response.raise_for_status() == None:
                response = self.response.json()
            else:
                response = self.response.raise_for_status()
            return response
        except Exception as errh:
            print(f'Error detected: {errh}')


    def get_single_incident(self, inc_number: str):
        method = "GET"
        url = f"{self.baseUrl}/api/now/table/incident?sysparm_query=number={inc_number}"
        return self._make_connection(method, url)


    def get_multiple_incident(self, sysparm_limit="1", sysparm_query=None):
        method = "GET"
        url = f"{self.baseUrl}/api/now/table/incident?sysparm_limit={sysparm_limit}&sysparm_query={sysparm_query}"
        return self._make_connection(method, url)


    def get_single_email(self, sys_id:str):
        method = "GET"
        url = f"{self.baseUrl}/api/now/v1/email/{sys_id}"
        return self._make_connection(method, url)    


    def get_multiple_emails(self, sysparm_limit="1", sysparm_query=None):
        method = "GET"
        url = f"{self.baseUrl}/api/now/table/sys_email?sysparm_limit={sysparm_limit}&sysparm_query={sysparm_query}"
        return self._make_connection(method, url)
        
   