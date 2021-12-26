"""
    Handler functions that tiggers lower-tier functions. 

"""
from events.observer import subscribe
from app.incidents import do_something_with_inc


def handle_new_incident(**data):

    do_something_with_inc(**data)


def setup_incident_listeners():
    """ Enable listening to the events occuring in the ecosystem """
    
    subscribe('new_incidents_received', handle_new_incident)