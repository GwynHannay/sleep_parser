import csv
import json
from utils import csv_parser as cps, data_functions as df
from datetime import datetime


def conversion(csv_file: str):
    """Converts and transforms a CSV file from the Sleep as Android app into a JSON file.

    Parameters
    ----------
    csv_file : str
        Name / location of the CSV file to be processed.
    """
    first_pass = []

    # load CSV file
    with open(csv_file, encoding='utf-8') as csvf:
        csv_reader = csv.reader(csvf)

        # each row is either a header row or a values row
        # if this is a header row, store it in a new array
        # if this is a values row, combine it with the previous row's headers
        for row in csv_reader:
            if row[0] == 'Id':
                headers = []
                headers = cps.csv_headers(row)
            else:
                first_pass.append(cps.combine_record(
                    headers, row))  # type: ignore

    # now that we have a dictionary of headers and values
    # let's identify each part and convert it into
    # something much more useable
    i = 0
    id = 0
    json_array = []
    for record in first_pass:
        headers = []
        details = []
        events = []
        actigraphies = []

        for key in record:
            val = record[key]

            header = df.process_header(key)

            # these headers contain datetimes in various forms, so we want to standardise them
            if header in ('id', 'tracking_start', 'tracking_end', 'alarm_scheduled'):
                datetime_value = df.process_dates(header, val)

                if header == 'id':
                    id = datetime_value
                else:
                    val = datetime.strftime(datetime_value, '%Y-%m-%d %H:%M')

            elif header in ('tracking_hours'):
                val = df.process_numbers(val)

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
            # records[header].append(val)

        zip_it = zip(headers, details)
        # print(dict(zip_it))
        item = dict(zip_it)
        json_array.append(item)
        print("goat")
        i = i + 1
        print(i)
        if i == 30:
            # print(records)
            break

    # print(json_array)
        # break

    result = json.dumps(json_array)
    # print(result)

    # convert Python json_array to JSON String and write to file
    with open(r'sleep-export.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(result)


if __name__ == "__main__":
    """[summary]
    """
    # set the name of our CSV file to be transformed
    csv_file = r'sleep-as-android/csv/sleep-export.csv'

    # pass the filename to the function that will convert it
    try:
        conversion(csv_file)
    except Exception as e:
        Exception(
            "Error sending file to conversion method: {}, {}.".format(csv_file, e))
