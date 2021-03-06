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

result_filedata_list_all = []

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
                    elif param_key == 'DisplayName':
                        filedata_table['parameter'] = param_value
                    elif param_key == 'Enabled':
                        filedata_table['Value'] = param_value
                if len(filedata_table) > 0:
                    result_filedata_list_all.append(filedata_table)

result = {}
target_parameter_root_key = 'VAR_WIN_NetAdapterBinding'
result[target_parameter_root_key] = result_filedata_list_all
print(json.dumps(result))

