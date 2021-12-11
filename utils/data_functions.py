from datetime import datetime, timedelta


def process_header(header: str) -> str:
    """[summary]

    Parameters
    ----------
    header : str
        [description]

    Returns
    -------
    str
        [description]

    Raises
    ------
    Exception
        [description]
    """
    # convert all headers to lowercase
    header = header.lower()

    # rename some of the headings to be a bit more descriptive
    try:
        if header == 'tz':
            header = 'timezone'
        elif header == 'from':
            header = 'tracking_start'
        elif header == 'to':
            header = 'tracking_end'
        elif header == 'sched':
            header = 'alarm_scheduled'
        elif header == 'hours':
            header = 'tracking_hours'
    except Exception as e:
        raise Exception(
            "An error occurred processing header '{}': {}".format(header, e))

    return header


def process_dates(header, detail):
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
    if header == 'id':
        datetime_value = datetime.fromtimestamp(int(detail)/1000)
    else:
        datetime_value = datetime.strptime(detail, '%d. %m. %Y %H:%M')

    return datetime_value


def process_numbers(header, detail):
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
    detail = float(detail)

    return detail


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
