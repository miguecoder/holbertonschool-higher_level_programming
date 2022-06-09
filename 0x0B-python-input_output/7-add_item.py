#!/usr/bin/python3
"""script that add all arguments to a python list
the save them to a file"""

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    file = load_from_json_file("add_item.json")
except FileNotFoundError:
    file = list()
for item in sys.argv[1:]:
    file.append(item)
save_to_json_file(file, "add_item.json")
