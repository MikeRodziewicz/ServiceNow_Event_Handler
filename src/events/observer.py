"""
    Module that forms the basis of the Observer design pattern. 
    It provides two main funtions - subscribe and post events.
    This allows for creation of event listeners to trigger other functions. 
"""

subscribers = dict()


def subscribe(event_type: str, fn):
    """ Map events with the handler functions """

    if not event_type in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(fn)


def post_event(event_type: str, **data):
    """ Trigger a handler function """

    if not event_type in subscribers:
        return 
    for fn in subscribers[event_type]:
        fn(**data)

    