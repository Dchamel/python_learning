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

# ---------

# csv - reads and writes table data to csv
# import csv
#
# with open('sw_data.csv', newline='') as csvfile:
#     reader = csv.reader(f1, delimiter=';')
#     headers = next(reader)
#     print(headers)
#
#     for row in reader:
#         print(row)
#
# with open('sw_data.csv', newline='') as csvfile2:
#     reader = csv.DictReader(csvfile2)
#     for row in reader:
#         print(row)
#         print(row['hostname'], row['model'])

# ---------

# pickle - serialization / deserialization of object structure

# pickling - transfiguration objects to bite flow

# import pickle
#
# pickle.DEFAULT_PROTOCOL
# data = {'a': [1, 2.0, 3, 4 + 6j],
#         'b': ('string', u'Unicode string'),
#         'c': None}
#
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
#
# output = open('data.pkl', 'wb')
# pickle.dump(data, output)
#
# pickle.dump(selfref_list, output, 4)
#
# output.close()

# ---

import pprint, pickle

pkl_file = open('data.pkl', 'rb')
data = pickle.load(pkl_file)
pprint.pprint(data, width=60)
print(data)

data = pickle.load(pkl_file)
pprint.pprint(data, width=60)
pkl_file.close()
