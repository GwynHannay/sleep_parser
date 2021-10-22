import json

def read_it(json_path):
    json_array = []

    with open(json_path) as f:
        contents = json.load(f)
        
    entries = {}
    d = {}
    for record in contents:
        j = 0
        for key in record:
            if j == 0:
                id = record[key]
            else:
                entries[j-1] = {'key': key, 'val': record[key]}

            j = j + 1

        d = {'id': id, 'entries': entries}
        json_array.append(d)

    result = [json.dumps(record) for record in json_array]

    with open(output_path, 'w', encoding='utf-8') as jsonf:
        for item in result:
            jsonf.write(''.join(item))
            jsonf.write('\n')

json_path = r'sleep-as-android/json/2021-08-10_sleep-export.json'
output_path = r'sleep-as-android/json/sleep-key-val.json'

read_it(json_path)