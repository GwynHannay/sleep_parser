import csv
import logging
from utils import csv_parser as cps, globals

globals.init()

logger = logging.getLogger('main')


def main(csv_file: str):
    """Converts and transforms a CSV file from the Sleep as Android app into a JSON file.

    Parameters
    ----------
    csv_file : str
        Name and location of the CSV file to be processed.
    """
    first_pass, headers, json_array = [], [], []

    # Load CSV file.
    try:
        with open(csv_file, encoding='utf-8') as csvf:
            csv_reader = csv.reader(csvf)

            # Each row is either a header row, a values row, or a noise recording row.
            # If this is a header row, store it in a new array to be merged with its values.
            # If this is a values row, combine it with the previous row's headers.
            # If this is a noise recording row, skip it. We don't process these in this version.
            for row in csv_reader:
                if row[0] == 'Id':
                    headers = cps.csv_headers(row)
                elif row[0].isdigit():
                    first_pass.append(cps.combine_record(
                        headers, row))
                else:
                    continue

        # Now that we have a dictionary of headers and values, let's identify each part and 
        # convert it into something much more useable.
        # Process each record in the dictionary and write it into a JSON file every time the
        # month changes.
        suffix, previous_suffix = 'append', 'append'
        i, records = 0, len(first_pass)

        while suffix != 'done':
            for record in first_pass:
                entry = cps.saa_field_parser(record)
                suffix = cps.get_suffix()

                if suffix != previous_suffix and previous_suffix != 'append':
                    # Since the Sleep as Android data is stored with the most recent record at
                    # the top, once we have a completed month we should reverse the order so it starts
                    # at day one.
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
        logger.exception("Problem opening CSV file. {}".format(e))


if __name__ == "__main__":
    # Set our CSV filename and send it to our main function.
    csv_file = r'sleep-as-android/csv/sleep-export.csv'

    main(csv_file)
