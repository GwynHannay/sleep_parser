import json
from datetime import datetime, timedelta
from utils import globals

globals.init()


def process_suffix(pk) -> str:
    """Transforms a datetime field into a string of 'year-month'

    Parameters
    ----------
    pk : datetime
        Datetime of the first sleep session in this batch.

    Returns
    -------
    str
        Year and month of the datetime, in format 'year-month'.
    """
    suffix = datetime.strftime(pk, '%Y-%m')

    return suffix


def process_pk(key: str) -> int:
    """Handles the primary key from Sleep as Android, which is the session
    start Unix timestamp. It is assigned to the global variable 'start_time'
    and then transformed for primary key purposes.

    Parameters
    ----------
    key : str
        The Unix timestamp from the 'Id' field in the CSV file.

    Returns
    -------
    int
        Original Unix timestamp in integer form.
    """
    datetime_value = datetime.fromtimestamp(int(key)/1000)

    globals.start_time = datetime_value

    value = process_integer(key)
    return value


def process_dates(detail: str) -> str:
    """Parses a string datetime from one format, then returns it as a string
    in a better format.

    Parameters
    ----------
    detail : str
        Original datetime string: day. month. year hour:minute

    Returns
    -------
    str
        New datetime string: year-month-day hour:minute
    """
    datetime_value = datetime.strptime(detail, '%d. %m. %Y %H:%M')
    datetime_string = datetime.strftime(datetime_value, '%Y-%m-%d %H:%M')

    return datetime_string


def process_float(detail: str) -> float:
    """Receives a string and returns a float.

    Parameters
    ----------
    detail : str
        String field.

    Returns
    -------
    float
        Field as a float.
    """
    value = float(detail)

    return value


def process_integer(detail: str) -> int:
    """Receives a string and returns an integer.

    Parameters
    ----------
    detail : str
        String field.

    Returns
    -------
    int
        Field as an integer.
    """
    value = int(detail)

    return value


def process_event(event: str) -> dict:
    """Specifically handles 'Event' fields from Sleep as Android.
    This involves splitting the event type, the Unix timestamp, and
    the event's value if it has one.

    Parameters
    ----------
    event : str
        String with event information separated by hyphens.

    Returns
    -------
    dict
        Completed dictionary with event split into type, datetime, and value (if
        exists).
    """
    event_parts = event.split('-', 2)

    event_type = event_parts[0]

    timestamp = datetime.fromtimestamp(int(event_parts[1])/1000)
    # we want milliseconds, because the DHA event occurs every 1 millisecond
    # until you fall asleep
    event_time = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')

    if len(event_parts) > 2:
        if event_type == 'HR':
            event_value = float(event_parts[2])
        else:
            event_value = event_parts[2]

        event_dict = {
            'event_type': event_type,
            'event_time': event_time,
            'event_value': event_value
        }
    else:
        event_value = None

        event_dict = {
            'event_type': event_type,
            'event_time': event_time
        }

    return event_dict


def process_actigraphy(time: str, value: str, start_time) -> dict[str, str]:
    """Specifically handles actigraphic events from Sleep as Android.
    The header fields for these are made of the time (not including date)
    of the data recorded, so we want to get the global start time and
    use this to add a timestamp to each data point.

    Parameters
    ----------
    time : str
        Hour and minute in string format.
    value : str
        Actigraphic value.
    start_time : datetime
        Global start time of this sleep record.

    Returns
    -------
    dict[str, str]
        Completed dictionary of actigraphic event, ready to be inserted into the
        record.
    """
    act_time_part = datetime.strptime(time, '%H:%M').time()
    start_time_part = start_time.time()
    start_time_date = start_time.date()
    next_day_date = start_time_date + timedelta(days=1)

    # the date isn't included in the actigraphic header, so once the time
    # recorded is greater than the time that this sleep session started, we
    # can assume it's the next day
    if act_time_part > start_time_part:
        act_datetime = datetime.combine(start_time_date, act_time_part)
    else:
        act_datetime = datetime.combine(next_day_date, act_time_part)

    act_dict = {
        'actigraphic_time': act_datetime.strftime('%Y-%m-%d %H:%M'),
        'actigraphic_value': value
    }

    return act_dict


def process_array(records: list) -> str:
    """Receives an array and converts it into a JSON string.

    Parameters
    ----------
    records : list
        An array of records.

    Returns
    -------
    str
        A JSON string.
    """
    json_string = json.dumps(records)

    return json_string
