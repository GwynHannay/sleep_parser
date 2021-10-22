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
                d = {}
                headers = []
                i = 0
                for val in row:
                    if val[0].isdigit():
                        val = 'act_{}'.format(val)
                    if val == 'Event':
                        val = 'event_{}'.format(i)
                        i = i + 1

                    val = val.replace(':', '_').lower()
                    headers.append(val)
            else:
                cols = row
                zip_it = zip(headers, cols)
                dictionary = dict(zip_it)
                json_array.append(dictionary)

    result = [json.dumps(record) for record in json_array]
    print(d)
    # convert Python json_array to JSON String and write to file
    #with open(json_path, 'w', encoding='utf-8') as jsonf:
        #for d in result:
            #jsonf.write(''.join(d))
            #jsonf.write('\n')

csv_path = r'sleep-as-android/csv/2021-08-10_sleep-export.csv'
json_path = r'sleep-as-android/json/2021-09-26_key-val.json'

conversion(csv_path, json_path)