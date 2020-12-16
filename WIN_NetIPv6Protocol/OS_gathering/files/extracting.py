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

result_filedata_table = {}

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
                for param_key, param_value in row.items():
                    if isinstance(param_value, dict):
                        timestr = ""
                        if param_value['Days'] > 0:
                            timestr = str(param_value['Days']) + "."
                        timestr += "{0:02d}:{1:02d}:{2:02d}".format(param_value['Hours'], param_value['Minutes'], param_value['Seconds'])
                        result_filedata_table[param_key] = timestr
                    else:
                        result_filedata_table[param_key] = param_value

result = {}
target_parameter_root_key = 'VAR_WIN_NetIPv6Protocol'
result[target_parameter_root_key] = result_filedata_table
print(json.dumps(result))

