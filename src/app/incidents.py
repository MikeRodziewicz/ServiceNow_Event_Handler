"""
    Module that takes case of acions related to the Incident record in ServiceNow. 

"""
from events.observer import post_event
from app.models import NewIncident, NewIncidentDB



def monitor_for_new_incidents(connection=None, **kwargs):
    """ Function to GET new incidens at regular intervals """

    search_query = kwargs['query']

    resp = connection.get_multiple_incident(sysparm_query=search_query)
    print(resp)
    result = resp['result']


    if len(result) != 0:
        print('New incidents detected...', flush=True)
        post_event('new_incidents_received', connection=connection, new_incidents=resp)
    else:
        print('No new incidents...')



def incident_to_model(**kwargs):
    
    incident_list = kwargs['new_incidents']['result']

    for item in incident_list:
        # incident = NewIncident(item['sys_id'], item['number'])
        incident = NewIncidentDB(item['sys_id'], item['number'])
        return incident
    