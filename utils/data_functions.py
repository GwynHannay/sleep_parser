import json
from datetime import datetime, timedelta
from utils import globals

globals.init()


def process_pk(key: str) -> int:
    datetime_value = datetime.fromtimestamp(int(key)/1000)

    globals.start_time = datetime_value

    value = process_integer(key)
    return value


def process_dates(detail: str) -> str:
    """[summary]

    Parameters
    ----------
    header : str
        [description]
    detail : str
        [description]

    Returns
    -------
    datetime
        [description]
    """
    datetime_value = datetime.strptime(detail, '%d. %m. %Y %H:%M')
    datetime_string = datetime.strftime(datetime_value, '%Y-%m-%d %H:%M')

    return datetime_string


def process_float(detail: str) -> float:
    """[summary]

    Parameters
    ----------
    header : [type]
        [description]
    detail : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    value = float(detail)

    return value


def process_integer(detail: str) -> int:
    value = int(detail)

    return value


def process_event(event):
    """[summary]

    Parameters
    ----------
    event : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    event_parts = event.split('-', 2)

    event_type = event_parts[0]

    timestamp = datetime.fromtimestamp(int(event_parts[1])/1000)
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


def process_actigraphy(time, value, start_time):
    """[summary]

    Parameters
    ----------
    time : [type]
        [description]
    value : [type]
        [description]
    start_time : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    act_time_part = datetime.strptime(time, '%H:%M').time()
    start_time_part = start_time.time()
    start_time_date = start_time.date()
    next_day_date = start_time_date + timedelta(days=1)

    if act_time_part > start_time_part:
        act_datetime = datetime.combine(start_time_date, act_time_part)
    else:
        act_datetime = datetime.combine(next_day_date, act_time_part)

    act_dict = {
        'actigraphic_time': act_datetime.strftime('%Y-%m-%d %H:%M'),
        'actigraphic_value': value
    }

    return act_dict


def process_array(records):
    json_string = json.dumps(records)

    return json_string
