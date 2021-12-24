from datetime import datetime


def init():
    global start_time
    global saa_fields

    start_time = datetime

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
