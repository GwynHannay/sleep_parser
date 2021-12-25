from datetime import datetime


def init():
    """Contains global variables.
    """    
    global start_time
    global saa_fields

    # this is the start datetime of the sleep session which is set
    # at the beginning of each new sleep record
    start_time = datetime

    # these are the fields we've identified in the Sleep as Android
    # output, and this dictionary details how we handle each one
    saa_fields = {
        'Id': {
            'name': 'id',
            'type': 'pk'
        },
        'Tz': {
            'name': 'timezone',
            'type': 'string'
        },
        'From': {
            'name': 'tracking_start',
            'type': 'datetime'
        },
        'To': {
            'name': 'tracking_end',
            'type': 'datetime'
        },
        'Sched': {
            'name': 'alarm_scheduled',
            'type': 'datetime'
        },
        'Hours': {
            'name': 'hours_tracked',
            'type': 'float'
        },
        'Rating': {
            'name': 'rating',
            'type': 'float'
        },
        'Comment': {
            'name': 'comment',
            'type': 'string'
        },
        'Framerate': {
            'name': 'framerate',
            'type': 'integer'
        },
        'Snore': {
            'name': 'snore',
            'type': 'integer'
        },
        'Noise': {
            'name': 'noise',
            'type': 'float'
        },
        'Cycles': {
            'name': 'cycles',
            'type': 'integer'
        },
        'DeepSleep': {
            'name': 'deepsleep',
            'type': 'float'
        },
        'LenAdjust': {
            'name': 'lenadjust',
            'type': 'integer'
        },
        'Geo': {
            'name': 'geo',
            'type': 'string'
        },
        'Actigraphy': {
            'name': 'actigraphy',
            'type': 'array'
        },
        'Event': {
            'name': 'events',
            'type': 'array'
        }
    }
