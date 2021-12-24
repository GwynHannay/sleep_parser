import csv, logging
from utils import csv_parser as cps, globals

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
    try:
        with open(csv_file, encoding='utf-8') as csvf:
            csv_reader = csv.reader(csvf)

            # each row is either a header row, a values row, or a noise recording row
            # if this is a header row, store it in a new array
            # if this is a values row, combine it with the previous row's headers
            # if this is a noise recording row, skip it
            for row in csv_reader:
                if row[0] == 'Id':
                    headers = cps.csv_headers(row)
                elif row[0].isdigit():
                    first_pass.append(cps.combine_record(
                        headers, row))
                else:
                    continue

        # now that we have a dictionary of headers and values
        # let's identify each part and convert it into
        # something much more useable
        suffix, previous_suffix = 'append', 'append'
        i, records = 0, len(first_pass)

        while suffix != 'done':
            for record in first_pass:
                entry = cps.saa_field_parser(record)
                suffix = cps.get_suffix()

                if suffix != previous_suffix and previous_suffix != 'append':
                    json_array.reverse()
                    result = cps.build_records(json_array)

                    with open(r'sleep-export-' + previous_suffix + r'.json', 'w', encoding='utf-8') as jsonf:
                        jsonf.write(result)

                    json_array = []

                json_array.append(entry)

                previous_suffix = suffix

                i = i + 1
                if i > records:
                    suffix = 'done'
    except Exception as e:
        logging.exception("Problem opening CSV file. {}".format(e))


if __name__ == "__main__":
    # set the name of our CSV file to be transformed
    csv_file = r'sleep-as-android/csv/sleep-export--.csv'

    try:
        conversion(csv_file)
    except Exception as e:
        logging.exception("Error sending file to conversion method: {}, {}.".format(csv_file, e))
