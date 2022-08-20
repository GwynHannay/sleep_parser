import logging
from datetime import datetime


logger = logging.getLogger(__name__)

def init():
    """Contains global variables.
    """
    global pk
    global start_time
    global time_zone
    global saa_fields

    # This is the primary key of a sleep record from Sleep as
    # Android, which is a Unix timestamp. It is set at the
    # beginning of each new sleep record.
    pk = int

    # This is the start datetime of the sleep session which is set
    # at the beginning of each new sleep record.
    start_time = datetime

    # This is a text representation of the time zone recorded by
    # Sleep as Android and is set at the beginning of each new sleep
    # record.
    time_zone = str

    # These are the fields we've identified in the Sleep as Android
    # output, and this dictionary details how we handle each one.
    saa_fields = {
        'Id': {
            'name': 'id',
            'type': 'pk'
        },
        'Tz': {
            'name': 'timezone',
            'type': 'tz'
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
    logger.debug('Globals initialised, and Sleep as Android fields are: %s', saa_fields)


def get_current_datetime():
    datetime_value = datetime.strftime(datetime.now(), '%Y-%m-%d')
    return datetime_value
    
