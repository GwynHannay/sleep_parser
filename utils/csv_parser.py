import logging
from utils import data_functions as df, globals


logger = logging.getLogger(__name__)

def csv_headers(headers: list) -> list:
    """Processes header rows in the CSV document.
    Specifically, we want to append an incrementing integer to the 'Event' 
    fields so that a dictionary doesn't overwrite each event with the next one.

    Parameters
    ----------
    headers : list
        The row of headers from the CSV file.

    Returns
    -------
    list
        The modified list of headers which can now be easily merged with its details row.
    """
    processed, i = [], 0
    for header in headers:
        if header == 'Event':
            header = header + ' {}'.format(i)
            i = i + 1

        processed.append(header)

    return processed


def combine_record(headers: list, row: list) -> dict:
    """Quick function that takes two lists and joins them together
    into a dictionary.

    Parameters
    ----------
    headers : list
        The list of headers from the CSV file.
    row : list
        The list of values from the CSV file.

    Returns
    -------
    dict
        A dictionary where each header is matched with its value.
    """
    zip_it = zip(headers, row)
    record = dict(zip_it)

    return record


def saa_field_parser(record: dict) -> dict:
    """Processes a single record from the CSV file, retrieving instructions
    on how to handle each field and sending them off to be transformed before
    returning a fully formatted record.

    Parameters
    ----------
    record : dict
        A record of headers and values from the CSV file, i.e. a single sleep session.

    Returns
    -------
    dict
        The completely processed record, ready to be written into the JSON file.
    """
    headers, entries, actigraphies, events = [], [], [], []

    for key in record:
        header = key
        value = record[key]

        if header.startswith('Event'):
            instructions = get_instructions('Event')
            result = follow_instructions(header, value, instructions)
            events.append(result[1])

        elif header[0].isdigit():
            instructions = get_instructions('Actigraphy')
            result = follow_instructions(header, value, instructions)
            actigraphies.append(result[1])

        else:
            instructions = get_instructions(header)
            result = follow_instructions(header, value, instructions)
            headers.append(result[0])
            entries.append(result[1])

    # Actigraphic data and event data will be nested, so add them
    # under a single header.
    if len(actigraphies) > 0:
        headers.append('actigraphy')
        entries.append(actigraphies)

    if len(events) > 0:
        headers.append('events')
        entries.append(events)

    entry = combine_record(headers, entries)

    return entry


def get_instructions(header: str) -> dict:
    """Receives a field name and returns with a dictionary of instructions
    from the global variable that defines each field.

    Parameters
    ----------
    header : str
        The field name.

    Returns
    -------
    dict
        Instructions for how to handle this field based on the name.
    """
    instruction = globals.saa_fields[header]

    return instruction


def follow_instructions(header: str, value: str, field_details: dict) -> tuple:
    """Receives a field name, value, and instructions on how to handle this
    field, then follows them accordingly.

    Parameters
    ----------
    header : str
        Original field name from the CSV file.
    value : str
        Value accompanying the field name.
    field_details : dict
        'Instructions', i.e. new field name and end data type.

    Returns
    -------
    tuple
        Processed header and value for the record.
    """
    field = ()
    field_name = field_details['name']
    d_type = field_details['type']

    if d_type == 'pk':
        pk_value = df.process_pk(value)
        field = (field_name, pk_value)

    elif d_type == 'tz':
        tz_value = df.process_tz(value)
        field = (field_name, tz_value)

    elif d_type == 'datetime':
        dt_value = df.process_dates(value)
        field = (field_name, dt_value)

    elif d_type == 'float':
        f_value = df.process_float(value)
        field = (field_name, f_value)

    elif d_type == 'integer':
        i_value = df.process_integer(value)
        field = (field_name, i_value)

    elif d_type == 'string':
        field = (field_name, value)

    elif d_type == 'array':
        if field_name == 'actigraphy':
            act = df.process_actigraphy(header, value, globals.start_time)
            field = (field_name, act)

        elif field_name == 'events':
            event = df.process_event(value)
            field = (field_name, event)

    return field


def build_records(records: list) -> str:
    """Transforms a series of sleep sessions into a JSON string.

    Parameters
    ----------
    records : list
        All records to be written into a JSON file.

    Returns
    -------
    str
        JSON string to be written into the JSON file.
    """
    json_string = df.process_array(records)

    return json_string


def get_suffix() -> str:
    """Retrieves the suffix for this JSON file based on the start date of the
    first sleep session.

    Returns
    -------
    str
        Suffix for the JSON file in the form of 'year-month'.
    """
    suffix = df.process_suffix(globals.start_time)

    return suffix
