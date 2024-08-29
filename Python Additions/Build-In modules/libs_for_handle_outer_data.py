# ---

# json

# import json
#
# with open('data.json', 'w') as write_file:
#     json.dump(data, write_file, indent=4)
#
# json_string = json.dumps(data)
#
# with open('data.json', 'r') as read_file:
#     data = json.load(read_file)
# data = json.loads(json_string)

# ---

# csv - reads and writes table data to csv
import csv

with open('sw_data.csv', newline='') as csvfile:
    reader = csv.reader(f1, delimiter=';')
    headers = next(reader)
    print(headers)

    for row in reader:
        print(row)

with open('sw_data.csv', newline='') as csvfile2:
    reader = csv.DictReader(csvfile2)
    for row in reader:
        print(row)
        print(row['hostname'], row['model'])
