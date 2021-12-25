from utils import data_functions as df, globals


def csv_headers(headers: list[str]) -> list[str]:
    """Processes header rows in the CSV document.
    Specifically, we want to append a number to the 'Event' fields so
    a dictionary doesn't overwrite each with the next one.

    Parameters
    ----------
    headers : list[str]
        The row of headers from the CSV file.

    Returns
    -------
    list[str]
        The row of headers now processed.
    """
    processed, i = [], 0
    for header in headers:
        if header == 'Event':
            header = header + ' {}'.format(i)
            i = i + 1

        processed.append(header)

    return processed


def combine_record(headers: list[str], row: list[str]) -> dict[str, str]:
    """Quick function that takes two lists and joins them together
    into a dictionary.

    Parameters
    ----------
    headers : list[str]
        The list of headers from the CSV file.
    row : list[str]
        The list of values from the CSV file.

    Returns
    -------
    dict[str, str]
        A dictionary where each header is matched with its value.
    """
    zip_it = zip(headers, row)
    record = dict(zip_it)

    return record


def saa_field_parser(record: dict[str, str]) -> dict[str, str]:
    """Handles the processing of all records from the CSV file.

    Parameters
    ----------
    record : dict[str, str]
        A single record from the CSV file, i.e. a single sleep session.

    Returns
    -------
    dict[str, str]
        The completely processed record, ready to be written into the JSON file.
    """
    headers, entries, actigraphies, events = [], [], [], []

    for key in record:
        header = key
        value = record[key]

        if header.startswith('Event'):
            datatype = get_instructions('Event')
            result = follow_instructions(header, value, datatype)
            events.append(result[1])

        elif header[0].isdigit():
            datatype = get_instructions('Actigraphy')
            result = follow_instructions(header, value, datatype)
            actigraphies.append(result[1])

        else:
            datatype = get_instructions(header)
            result = follow_instructions(header, value, datatype)
            headers.append(result[0])
            entries.append(result[1])

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
    from the global dictionary defining each field.

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


def follow_instructions(header: str, value: str, datatype: dict) -> tuple:
    """Renames each field and handles its contents based on the information
    sent with the header and value in the dictionary.

    Parameters
    ----------
    header : str
        Original field name from the CSV file.
    value : str
        Value accompanying the field name.
    datatype : dict
        'Instructions', i.e. new field name and end data type.

    Returns
    -------
    tuple
        Completed 'entry' for the record: processed field name and value.
    """
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
