from datetime import datetime

def process_header(header):
    header = header.lower()

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
    
    return header

def process_detail(header, detail):

    if header in ('tracking_start', 'tracking_end', 'alarm_scheduled'):
        detail = datetime.strptime(detail, '%d. %m. %Y %H:%M').strftime('%Y-%m-%d %H:%M')
    
    return detail

def process_event(event):
    event_parts = event.split('-')

    event_type = event_parts[0]

    timestamp = datetime.fromtimestamp(int(event_parts[1])/1000)
    event_time = timestamp.strftime('%Y-%m-%d %H:%M')

    if len(event_parts) > 2:
        event_value = event_parts[2]
    else:
        event_value = None
    
    event_dict = {
        'event_type': event_type,
        'event_time': event_time,
        'event_value': event_value
    }

    return event_dict