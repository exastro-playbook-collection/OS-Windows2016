import re
import json
import sys
import os

args = sys.argv
if (len(args) < 2):
    sys.exit(1)

path = args[1]
if(path[-1:] == "/"):
    path = path[:-1]

standby_table = {}
result_filedata_list = []

target_filepath_list = []
target_filepath_list.append('/1/stdout.txt')
for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            reader = json.load(file_object)
            if isinstance(reader, list):
                rows = reader
            else:
                rows = []
                rows.append(reader)
            for row in rows:
                if row['AdministrativeMode'] == 1:
                    standby_table[row['Team']] = row['Name']

target_filepath_list = []
target_filepath_list.append('/0/stdout.txt')
for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            reader = json.load(file_object)
            if isinstance(reader, list):
                rows = reader
            else:
                rows = []
                rows.append(reader)
            for row in rows:
                filedata_table = {}
                for param_key, param_value in row.items():
                    if param_key == 'Name':
                        filedata_table[param_key] = param_value
                        if param_value in standby_table:
                            filedata_table['Standby'] = standby_table[param_value]
                        else:
                            filedata_table['Standby'] = None
                    elif param_key == 'Members':
                        if isinstance(param_value, dict):
                            filedata_table[param_key] = param_value['value']
                        else:
                            filedata_table[param_key] = []
                            filedata_table[param_key].append(param_value)
                    else:
                        filedata_table[param_key] = param_value
                if len(filedata_table) > 0:
                    filedata_table['Action'] = 'present'
                    result_filedata_list.append(filedata_table)

result = {}
target_parameter_root_key = 'VAR_WIN_NICTeaming_Team'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

