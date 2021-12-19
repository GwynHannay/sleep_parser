import csv
import json
from utils import csv_parser as cps
from utils import globals

globals.init()


def conversion(csv_file: str):
    """Converts and transforms a CSV file from the Sleep as Android app into a JSON file.

    Parameters
    ----------
    csv_file : str
        Name / location of the CSV file to be processed.
    """
    first_pass, headers, json_array = [], [], []

    # load CSV file
    with open(csv_file, encoding='utf-8') as csvf:
        csv_reader = csv.reader(csvf)

        # each row is either a header row or a values row
        # if this is a header row, store it in a new array
        # if this is a values row, combine it with the previous row's headers
        for row in csv_reader:
            if row[0] == 'Id':
                headers = cps.csv_headers(row)
            else:
                first_pass.append(cps.combine_record(
                    headers, row))

    # now that we have a dictionary of headers and values
    # let's identify each part and convert it into
    # something much more useable
    suffix, previous_suffix = 'append', 'append'
    i, records = 0, len(first_pass)
    #print(first_pass[records-1])
    while suffix != 'done':
        for record in first_pass:
            entry = cps.saa_field_parser(record)
            suffix = cps.get_suffix()

            if suffix != previous_suffix and previous_suffix != 'append':
                json_array.reverse()
                result = cps.build_records(json_array)

                # with open(r'sleep-export-' + previous_suffix + r'.json', 'w', encoding='utf-8') as jsonf:
                #     jsonf.write(result)
                
                json_array = []
            
            json_array.append(entry)
        
            previous_suffix = suffix
            if i == 451:
                print(record)

            i = i + 1
            if i > records:
                suffix = 'done'

            


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
