#!bin/python
import json
import sys

with open('data.json', 'r+') as f:
    data = json.load(f)
    data["status"].append(sys.argv[1])
    json.dump(data, f)
