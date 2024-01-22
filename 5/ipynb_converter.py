import re
import sys, json
from functools import reduce


def get_new_file_name(file_name: str) -> str:
    arr = file_name.split('.')
    arr.insert(-1, 'czysty')
    return '.'.join(arr)


def remove_output(cell):
    if cell["cell_type"] == "code":
        cell["outputs"] = []
    return cell


def remove_exercise_code(acc, cell):
    if cell["cell_type"] == "markdown":
        if re.match(r"^#+\s*Ćwiczenie", cell["source"][0]):
            acc["exercise-just-before"] = True
    elif cell["cell_type"] == "code" and acc["exercise-just-before"]:
        cell["source"] = []
        acc["exercise-just-before"] = False
    acc["cells"].append(cell)
    return acc


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No file name given.")
        exit(1)

    # Load
    file_name = sys.argv[1]
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
    except Exception as e:
        print("Error opening the file \'" + file_name + "\'." + str(e))
        exit(1)
    print("Loaded file \'" + file_name + "\'")

    # Process
    json_data['cells'] = list(map(remove_output, json_data['cells']))
    result = reduce(remove_exercise_code, json_data['cells'], {"cells": [], "exercise-just-before": False})
    json_data['cells'] = result['cells']

    # Save
    new_file_name = get_new_file_name(file_name)
    with open(new_file_name, 'w+') as file:
        json.dump(json_data, file)
    print("Saved output file \'" + new_file_name + "\'.")
