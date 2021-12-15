
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
}


def csv_headers(headers):
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


def combine_record(headers, row):
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


def get_instructions(header):
    instruction = saa_fields[header]

    return instruction


def saa_field_parser(header, value):
    data_type = get_instructions(header)
