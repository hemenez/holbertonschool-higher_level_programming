#!/usr/bin/python3
import sys
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


filename = "add_item.json"

load_from_json_file(filename)

with open("add_item.json", "a+", encoding="utf-8") as my_file:
    my_list = []
    index = 0
    for i in sys.argv:
        if sys.argv[index] == 0:
            pass
        else:
            my_list.append(sys.argv[index])
        index = index + 1
    save_to_json_file(my_list, filename)
