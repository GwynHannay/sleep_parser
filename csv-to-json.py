import csv, json

def conversion(csv_path, json_path):
    json_array = []

    # read CSV file
    with open(csv_path, encoding='utf-8') as csvf:
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
                        val = 'Event {}'.format(i)
                        i = i + 1
                    headers.append(val)
            else:
                cols = row
                zip_it = zip(headers, cols)
                dictionary = dict(zip_it)
                json_array.append(dictionary)

    # convert Python json_array to JSON String and write to file
    with open(json_path, 'w', encoding='utf-8') as jsonf:
        json_string = json.dumps(json_array, indent=4)
        jsonf.write(json_string)

csv_path = r'csv/2021-08-10_sleep-export.csv'
json_path = r'json/2021-08-10_sleep-export.json'

conversion(csv_path, json_path)