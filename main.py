import csv, json
from helpers import csv_parser as cps, data_functions as df
from datetime import datetime
from collections import defaultdict

def conversion(csv_file):
    first_pass = []

    # read CSV file
    with open(csv_file, encoding='utf-8') as csvf:
        # load CSV file using csv library's dictionary reader
        csv_reader = csv.reader(csvf)

        # convert each row into Python Dict
        for row in csv_reader:
            # add this Python Dict to JSON array
            if row[0] == 'Id':
                headers = []
                headers = cps.csv_headers(row)
            else:
                first_pass.append(cps.combine_record(headers, row))
    
    i = 0
    json_array = []
    records = defaultdict(list)
    for record in first_pass:
        headers = []
        details = []
        events = []
        actigraphies = []

        for key in record:
            val = record[key]

            header = df.process_header(key)
            
            if header in ('id', 'tracking_start', 'tracking_end', 'alarm_scheduled'):
                datetime_value = df.process_dates(header, val)

                if header == 'id':
                    id = datetime_value
                else:
                    val = datetime.strftime(datetime_value, '%Y-%m-%d %H:%M')
            
            elif header in ('tracking_hours'):
                val = df.process_numbers(header, val)

            elif header.startswith('event'):
                event = df.process_event(val)
                header = 'events'
                events.append(event)
                val = events
            
            elif header[0].isdigit():
                actigraphy = df.process_actigraphy(header, val, id)
                header = 'actigraphy'
                actigraphies.append(actigraphy)
                val = actigraphies
            
            headers.append(header)
            details.append(val)
            #records[header].append(val)
        
        zip_it = zip(headers, details)
        #print(dict(zip_it))
        item = dict(zip_it)
        json_array.append(item)
        print("goat")
        i = i + 1
        print(i)
        if i == 30:
            #print(records)
            break

    #print(json_array)
        #break

    result = json.dumps(json_array)
    #print(result)

    # convert Python json_array to JSON String and write to file
    with open(r'sleep-export.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(result)

if __name__ == "__main__":
    # set the name of our CSV file to be transformed
    csv_file = r'sleep-export.csv'

    # pass the filename to the function that will convert it
    try:
        conversion(csv_file)
    except Exception as e:
        Exception("Error sending file to conversion method: {}, {}.".format(csv_file, e))
