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
                adapter_name = ''
                for param_key, param_value in row.items():
                    if param_key == 'ifDesc':
                        adapter_name = param_value
                    elif param_key == 'DisplayName':
                        property_name = param_value
                    elif param_key == 'DisplayValue':
                        property_value = param_value
                if len(adapter_name) > 0:
                    if adapter_name not in result_filedata_table:
                        result_filedata_table[adapter_name] = {}
                    result_filedata_table[adapter_name][property_name] = property_value

result = {}
target_parameter_root_key = 'VAR_WIN_NetAdapterAdvancedProperty'
result[target_parameter_root_key] = result_filedata_table
print(json.dumps(result))

