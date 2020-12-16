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
type_table = {}

target_filepath_list = []
target_filepath_list.append('/1/stdout.txt')
target_filepath_list.append('/3/stdout.txt')
for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            lines = file_object.readlines()
            for line in lines:
                if len(line) > 0:
                    params = re.split('^\s*(.*)\s+(REG_\S*)\s+.*$', line)
                    if len(params) == 4:
                        param_key = params[1].strip()
                        param_type = params[2].strip()
                        if param_key == '(Default)':
                            param_key = '(default)'
                        if path_key not in type_table:
                            type_table[path_key] = {}
                        type_table[path_key][param_key] = param_type
                    else:
                        path_key = line.strip()
                        path_key = re.sub('^HKEY_LOCAL_MACHINE', 'HKLM', path_key)
                        path_key = re.sub('^HKEY_CURRENT_USER', 'HKCU', path_key)

target_filepath_list = []
target_filepath_list.append('/0/stdout.txt')
target_filepath_list.append('/2/stdout.txt')
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
                for path_key, path_value in row.items():
                    param_list = []
                    if path_value is not None:
                        for param_key, param_value in path_value.items():
                            param_info = {}
                            param_info['ValueName'] = param_key
                            param_info['ValueType'] = type_table[path_key][param_key]
                            param_info['Value'] = param_value
                            param_list.append(param_info)
                    if len(param_list) > 0:
                        registry_info = {}
                        path_key = re.sub('^HKLM', 'HKLM:', path_key)
                        path_key = re.sub('^HKCU', 'HKCU:', path_key)
                        registry_info['Key'] = path_key
                        registry_info['Values'] = param_list
                        result_filedata_list.append(registry_info)

result = {}
target_parameter_root_key = 'VAR_WIN_SNMPService'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

