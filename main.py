import csv
import json
from utils import csv_parser as cps
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
        entries = []
        events = []
        actigraphies = []

        for key in record:
            result = cps.saa_field_parser(key, record[key])
            
            field_name = result[0]
            entry = result[1]

            if field_name == 'actigraphy':
                actigraphies.append(entry)
            elif field_name == 'events':
                events.append(entry)
            else:
                headers.append(field_name)
                entries.append(entry)
            
        if len(actigraphies) > 0:
            headers.append('actigraphy')
            entries.append(actigraphies)
        
        if len(events) > 0:
            headers.append('events')
            entries.append(events)

        zip_it = zip(headers, entries)
        item = dict(zip_it)
        print(item)
        break
            


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
