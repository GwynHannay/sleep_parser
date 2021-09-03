import json

def read_it(json_path):
    with open(json_path) as f:
        contents = json.load(f)
        
    i = 0
    for record in contents:
        if i == 0:
            for key in record:
                print("lerlll {}".format(key))
                print("brrr {}".format(record[key]))
        else:
            break

        i = 1

json_path = r'sleep-as-android/json/2021-08-10_sleep-export.json'

read_it(json_path)