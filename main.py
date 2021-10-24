import csv, json, data_functions as df
from datetime import datetime

# Step 1: Open CSV and read
# Step 2: Select first row
# Step 3: Identify if this is a header or a detail
# Step 4: 
# # For a header: 
# # # Clear out previous headers array
# # # Iterate through each field
# # # If this field is "Event", append an auto increment number
# # # Add to a headers array
# # For a detail:
# # # Place all details into an array
# # # Zip details with the previous headers
# # # Turn the new arrays into a dictionary
# # # Add them into a JSON array
# Step 5: Loop through JSON array

# IF field = Id: name lowercase to "id", should I convert unix timestamp?
# IF field = Tz: name to "timezone" (formatting?)
# IF field = From: name to "tracking_start", convert to proper datetime with timezone | option for original, unix timestamp
# IF field = To: name to "tracking_end", convert to proper datetime with timezone | option for original, unix timestamp
# IF field = Sched: name to "alarm_scheduled", convert to proper datetime with timezone | option for original, unix timestamp
# IF field = Hours: name to "tracking_hours"
# IF field = Rating: name lowercase
# IF field = Comment: name lowercase, maybe split into multiple fields as tags, allow for non-tags
# IF field = Framerate: ?
# IF field = Snore: ?
# IF field = Noise: ?
# IF field = Cycles: ?
# IF field = DeepSleep: ? Is this a percent?l
# IF field = LenAdjust: ?
# IF field = Geo: ?
# IF field = digit-type: actigraphy, learn about it and how to display
# IF field = Event #: [Types: DHA, HR, AWAKE_START, LIGHT_START, LUX, AWAKE_END, LIGHT_END, DEEP_START, 
#   DEEP_END, REM_START, REM_END, DEVICE, TRACKING_STOPPED_BY_USER, ALARM_LATEST, ALARM_STARTED, ALARM_DISMISSED, others?]
#       IF type = DHA: event type, timestamp (what is DHA?)
#       IF type = HR: event type, timestamp, value
#       IF type = LUX: event type, timestamp, value
#       IF type = AWAKE_START: event type, timestamp
#       IF type = AWAKE_END: event type, timestamp
#       IF type = LIGHT_START: event type, timestamp
#       IF type = LIGHT_END: event type, timestamp
#       IF type = DEEP_START: event type, timestamp
#       IF type = DEEP_END: event type, timestamp
#       IF type = REM_START: event type, timestamp
#       IF type = REM_END: event type, timestamp
#       IF type = DEVICE: event type, timestamp (what is this?)
#       IF type = TRACKING_STOPPED_BY_USER: event type, timestamp
#       IF type = ALARM_LATEST: event type, timestamp
#       IF type = ALARM_STARTED: event type, timestamp
#       IF type = ALARM_DISMISSED: event type, timestamp
# IF field = any other fields?

def conversion(csv_file):
    first_pass = []

    # read CSV file
    with open(csv_file, encoding='utf-8') as csvf:
        # load CSV file using csv library's dictionary reader
        csv_reader = csv.reader(csvf)

        cols = []
        # convert each row into Python Dict
        for row in csv_reader:
            # add this Python Dict to JSON array
            if row[0] == 'Id':
                headers = []
                i = 0
                for val in row:
                    if val == 'Event':
                        val = val + ' {}'.format(i)
                        i = i + 1

                    headers.append(val)
            else:
                cols = row
                zip_it = zip(headers, cols)
                dictionary = dict(zip_it)
                first_pass.append(dictionary)

    json_array = []
    events = []
    actigraphies = []
    for record in first_pass:
        headers = []
        details = []

        for key in record:
            val = record[key]

            header = df.process_header(key)
            
            if header in ('id', 'tracking_start', 'tracking_end', 'alarm_scheduled'):
                datetime_value = df.process_dates(header, val)

                if header == 'id':
                    id = datetime_value
                else:
                    val = datetime.strftime(datetime_value, '%Y-%m-%d %H:%M')
            
            elif header in ('tracking_hours', 'rating'):
                val = df.process_numbers(header, val)

            elif header.startswith('event'):
                event = df.process_event(val)
                header = 'events'
                events.append(event)
                val = {header: events}
            
            elif header[0].isdigit():
                actigraphy = df.process_actigraphy(header, val, id)
                header = 'actigraphy'
                actigraphies.append(actigraphy)
                val = {header: actigraphies}
            
            headers.append(header)
            details.append(val)
        
        zip_it = zip(headers, details)
        json_array.append(dict(zip_it))

        break

    result = [json.dumps(record) for record in json_array]
    print(result)

    # convert Python json_array to JSON String and write to file
    #with open(r'sleep-export.json', 'w', encoding='utf-8') as jsonf:
        #for d in result:
            #jsonf.write(''.join(d))
            #jsonf.write('\n')

csv_file = r'sleep-export.csv'

conversion(csv_file)
