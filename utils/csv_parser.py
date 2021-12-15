from utils import data_functions as df


saa_fields = {
    'Id': {
        'name': 'id',
        'type': 'unix timestamp'
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


def csv_headers(headers) -> list[str]:
    """[summary]

    Parameters
    ----------
    headers : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    processed = []
    i = 0
    for header in headers:
        if header == 'Event':
            header = header + ' {}'.format(i)
            i = i + 1

        processed.append(header)

    return processed


def combine_record(headers, row) -> dict[str, str]:
    """[summary]

    Parameters
    ----------
    headers : [type]
        [description]
    row : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    zip_it = zip(headers, row)
    record = dict(zip_it)

    return record


def saa_field_parser(header, value):
    if header.startswith('event'):
        datatype = get_instructions('Event')
    elif header[0].isdigit():
        datatype = get_instructions('Actigraphy')
    else:
        datatype = get_instructions(header)
    
    follow_instructions(header, value, datatype)


def get_instructions(header) -> dict:
    instruction = saa_fields[header]

    return instruction


def follow_instructions(header, value, datatype):
    header = datatype['name']
    
    if datatype['type'] in ('datetime', 'unix timestamp'):
        dt_value = df.process_dates(value, datatype['type'])

    print("header: {}, value: {}".format(header, dt_value))
