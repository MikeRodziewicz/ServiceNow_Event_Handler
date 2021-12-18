"""
    Handler functions that tiggers lower-tier functions. 

"""
from observer import subscribe


def handle_new_incident(**data):
    pass


def setup_incident_listeners():
    """ Enable listening to the events occuring in the ecosystem """
    
    subscribe('new_incidents_received', handle_new_incident)