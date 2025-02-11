import json


# This function overwrites whatever is in the designated file
# We can control the filename so it is run specific.
# Based on name or random ID?
def org_json_writer(input, file_name):
    """Function specifically to store the organisms.
    It takes a list of class objects and converts each to a dictionary
    then writes them to a file."""
    data = []
    for x in input:
        data.append(x.__dict__)

    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)


def json_reader(file_name):
    """Simple Function to pull and return data from a json file
    Updated to handle case where a file may not exist yet"""
    try:
        with open(file_name, 'r') as f:
            json_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        json_data = None
    return json_data


def sim_json_writer(input, file_name):
    """Function pulls the existing runs that are stored and appends
    the newest version. Updated to create the file if it doesn't exist"""
    sim_data = []
    for x in input:
        for terrain in x:
            sim_data.append(terrain.__dict__)
    with open(file_name, 'w') as f:
        json.dump(sim_data, f, indent=4)
