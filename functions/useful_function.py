import json
import os.path
from pathlib import Path
from re import search

file_types = {'.json', '.svg', '.png', '.gif', }


def create_file(dir_name, file_name, file_extension):
    """
    function that take dir_name, file_name & file_type
    if dir not exist, create it
    if file not exist, create it
    if file exist, delete it
    """

    # if file_extension not in file_types raise exception
    if file_extension not in file_types:
        raise Exception('file_extension not in file_types')

    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    file_name = file_name + file_extension
    current_path = Path.cwd()
    full_path = os.path.join(os.path.sep, current_path, dir_name, file_name)

    if os.path.isfile(full_path):
        os.remove(full_path)

    if not os.path.exists(full_path):
        with open(full_path, 'w') as f:
            pass

    return full_path


def map_to_value(keys, values):
    """
    take two lists
    [x,y,z] -> key
    [a,b,c,] till N number map each value to key in 3 
    """
    # if len of value  is not perfect divisibility by len(key) then raise exception
    if len(values) % len(keys) != 0:
        raise Exception('len(value) % len(key)!= 0')

    # number of column
    no_columns = len(keys)
    # number of rows
    no_rows = int(len(values) / no_columns)
    # start of slice
    start_of_slice = 0
    # create a dictionary
    list_of_maps = []
    for row_index in range(no_rows):
        values_list = values[start_of_slice:start_of_slice + no_columns]
        each_map = {}
        for column_index in range(no_columns):
            each_map[keys[column_index]] = values_list[column_index].strip()
            start_of_slice += 1
        list_of_maps.append(each_map)
    return list_of_maps


def dump_json(data: dict, file_path: str):
    """
    take dictionary and same it
    """
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=2)
    return 1


def load_json(file_path: str):
    """
    take filepath & check if exist or not if exist then load json and return
    """
    if os.path.exists(file_path):
        with open(file_path) as infile:
            data = json.load(infile)
            return data


def substitute_word_from_list(list_to_check, match_word, substitute_word):
    """
    This function take list of string, loop over it.
    Then if match_word exist in string then replace
    that word from list with substitute_word
    """
    new_list = []
    for each_word in list_to_check:
        if search(match_word, each_word):
            new_list.append(substitute_word)
        else:
            new_list.append(each_word)
    return new_list
