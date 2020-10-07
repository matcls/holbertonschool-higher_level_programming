#!/usr/bin/python3
"""Script that adds all arguments to a Python list."""
import sys

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filename = 'add_item.json'
try:
    py_list = load_from_json_file(filename)
except Exception:
    py_list = []
finally:
    for i in sys.argv[1:]:
        py_list.append(i)
    save_to_json_file(py_list, filename)
