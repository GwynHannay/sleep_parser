from datetime import datetime
import json
from utils import data_functions as df, globals


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
    if header.startswith('Event'):
        datatype = get_instructions('Event')

    elif header[0].isdigit():
        datatype = get_instructions('Actigraphy')

    else:
        datatype = get_instructions(header)

    entry = follow_instructions(header, value, datatype)

    return entry


def get_instructions(header) -> dict:
    instruction = globals.saa_fields[header]

    return instruction


def follow_instructions(header, value, datatype):
    entry = ()
    field_name = datatype['name']
    d_type = datatype['type']

    if d_type == 'pk':
        pk_value = df.process_pk(value)
        entry = (field_name, pk_value)

    elif d_type == 'datetime':
        dt_value = df.process_dates(value)
        entry = (field_name, dt_value)

    elif d_type == 'float':
        f_value = df.process_float(value)
        entry = (field_name, f_value)

    elif d_type == 'integer':
        i_value = df.process_integer(value)
        entry = (field_name, i_value)

    elif d_type == 'string':
        entry = (field_name, value)

    elif d_type == 'array':
        if field_name == 'actigraphy':
            act = df.process_actigraphy(header, value, globals.start_time)
            entry = (field_name, act)

        elif field_name == 'events':
            event = df.process_event(value)
            entry = (field_name, event)

    return entry
