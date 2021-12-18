"""
    Module that takes case of acions related to the Email record in ServiceNow. 

"""
from events.observer import post_event


def monitor_for_new_emails(connection=None, **kwargs):
    """ Function to GET new incidens at regular intervals """
    frequency = kwargs['frequency']
    search_query = kwargs['query']

    resp = connection.get_multiple_emails(search_query)

    if resp['result'] != []:
        print('New emails detected...', flush=True)
        post_event('new_emails_received', connection=connection, new_incidents=resp)
    else:
        print('No new emails...')