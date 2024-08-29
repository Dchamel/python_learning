# ---
# json

import json

with open('data.json', 'w') as write_file:
    json.dump(data, write_file, indent=4)

json_string = json.dumps(data)

with open('data.json', 'r') as read_file:
    data = json.load(read_file)
data = json.loads(json_string)

# ---
