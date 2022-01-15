import json
from zoneinfo import ZoneInfo
from datetime import datetime, timedelta
from utils import globals

globals.init()


def set_start_time():
    """Using the global variables 'pk' (Unix timestamp) and 'time_zone' from
    the Sleep as Android file, sets the start time of the sleep session.

    This is used for actigraphy and events.
    """
    starting = int(globals.pk)
    time_zone = str(globals.time_zone)

    datetime_value = datetime.fromtimestamp(starting/1000, ZoneInfo(time_zone))

    globals.start_time = datetime_value


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
    start Unix timestamp. It is assigned to the global variable 'pk'
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
    globals.pk = key

    value = process_integer(key)
    return value


def process_tz(tz: str) -> str:
    """Handles the time zone from Sleep as Android, assigning it to a global
    variable 'time_zone' which is later used to correctly transform the Unix
    timestamps for the session start and events.

    Parameters
    ----------
    tz : str
        The time zone string, e.g. 'Australia/Perth'

    Returns
    -------
    str
        The same time zone string.
    """
    globals.time_zone = tz

    set_start_time()

    return tz


def process_dates(detail: str) -> str:
    """Receives a datetime string in one format, then returns it as a string
    in another format which is easier read and understood internationally.

    Parameters
    ----------
    detail : str
        Original datetime string: 'day. month. year hour:minute'

    Returns
    -------
    str
        New datetime string: 'year-month-day hour:minute'
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
        String field converted into a float.
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
        String field converted into an integer.
    """
    value = int(detail)

    return value


def process_actigraphy(time: str, value: str, start_time) -> dict:
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
    dict
        Completed dictionary of actigraphic event with the datetime recorded and value
        recorded.
    """
    act_time_part = datetime.strptime(time, '%H:%M').time()
    start_time_part = start_time.time()
    start_time_date = start_time.date()
    next_day_date = start_time_date + timedelta(days=1)

    # The date isn't included in the actigraphic header, so if the time
    # recorded is greater than the time that this sleep session started, we
    # can assume that this is the next day.

    # TODO: Handle edge case for a sleep session that can pass over 2
    # days. This can be done by adding 1 day to the start date every time we
    # cross over midnight.
    if act_time_part > start_time_part:
        act_datetime = datetime.combine(start_time_date, act_time_part)
    else:
        act_datetime = datetime.combine(next_day_date, act_time_part)

    act_dict = {
        'actigraphic_time': act_datetime.strftime('%Y-%m-%d %H:%M'),
        'actigraphic_value': value
    }

    return act_dict


def process_event(event: str) -> dict:
    """Specifically handles 'Event' fields from Sleep as Android.
    This involves splitting the event type, the Unix timestamp, and the event's 
    value if it has one.

    Parameters
    ----------
    event : str
        String with event information separated by hyphens.

    Returns
    -------
    dict
        Completed dictionary with event split into event type, datetime, and value 
        (if one exists).
    """
    event_parts = event.split('-', 2)

    event_type = event_parts[0]

    timestamp = datetime.fromtimestamp(
        int(event_parts[1])/1000, ZoneInfo(str(globals.time_zone)))
    # We want the event time in milliseconds, because the DHA event occurs every 1
    # millisecond until you fall asleep.
    event_time = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    # Some events have a second hyphen if there is data to be included in it. Include
    # an event value if this is the case, otherwise set it to none and don't include
    # a field for it at all.

    # Additionally, we know that HR events are heart rates with a float value, so let's
    # convert that.

    # TODO: Detect and transform various value data types.
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


def process_array(records: list) -> str:
    """Receives an array and converts it into a JSON string.

    Parameters
    ----------
    records : list
        An array of records.

    Returns
    -------
    str
        The records now converted into a JSON string.
    """
    json_string = json.dumps(records)

    return json_string
