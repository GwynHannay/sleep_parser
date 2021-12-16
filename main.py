import csv
from utils import csv_parser as cps


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
    i = 0
    for record in first_pass:
        suffix = 'first'
        while suffix != 'done':
            entry = cps.saa_field_parser(record)
            json_array.append(entry)
            i = i + 1
            if i > 500: break
    #print(json_array)
    
    result = cps.build_records(json_array)

    with open(r'sleep-export-new.json', 'w', encoding='utf-8') as jsonf:
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
