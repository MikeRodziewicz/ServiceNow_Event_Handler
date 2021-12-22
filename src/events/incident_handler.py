"""
    Handler functions that tiggers lower-tier functions. 

"""
from events.observer import subscribe
from app.incidents import monitor_for_new_incidents


def handle_new_incident(**data):

    monitor_for_new_incidents(**data)


def setup_incident_listeners():
    """ Enable listening to the events occuring in the ecosystem """
    
    subscribe('new_incidents_received', handle_new_incident)