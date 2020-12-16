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

result_filedata_list = []

target_filepath_list = []
target_filepath_list.append('/0/stdout.txt')

for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            lines = file_object.readlines()
            for line in lines:
                result_filedata_list.append(line.strip())

result = {}
target_parameter_root_key = 'VAR_WIN_InstallPP'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

