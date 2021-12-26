"""
    Handler functions that tiggers lower-tier functions. 

"""
from events.observer import subscribe
from app.incidents import incident_to_model


def handle_new_incident(**data):

    incident_to_model(**data)


def setup_incident_listeners():
    """ Enable listening to the events occuring in the ecosystem """
    
    subscribe('new_incidents_received', handle_new_incident)