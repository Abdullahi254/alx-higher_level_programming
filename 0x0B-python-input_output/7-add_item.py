#!/usr/bin/python3
"""
import modules and sys function
"""
from sys import argv
import json
 save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file =\
    __import__('6-load_from_json_file').load_from_json_file


def add_arguments_to_list(args: List[str]) -> None:
    """adds argument to list"""
    filename = 'add_item.json'
    my_list = []

    if exists(filename):
        my_list = load_from_json_file(filename)

    my_list.extend(args)
    save_to_json_file(my_list, filename)

if __name__ == '__main__':
    arguments = sys.argv[1:]
    add_arguments_to_list(arguments)
