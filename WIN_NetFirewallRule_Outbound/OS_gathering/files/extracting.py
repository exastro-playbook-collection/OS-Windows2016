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
interface_info = {}

target_filepath_list = []
target_filepath_list.append('/1/stdout.txt')
target_filepath_list.append('/2/stdout.txt')
target_filepath_list.append('/3/stdout.txt')
target_filepath_list.append('/4/stdout.txt')
target_filepath_list.append('/5/stdout.txt')
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
                if 'InstanceID' not in row:
                    continue
                interface_index = row['InstanceID']
                row.pop('InstanceID')
                for param_key, param_value in row.items():
                    if param_key == 'LocalAddress' or \
                       param_key == 'RemoteAddress' or \
                       param_key == 'LocalPort' or \
                       param_key == 'RemotePort':
                        if isinstance(param_value, dict):
                            filedata_table[param_key] = param_value['value']
                        else:
                            filedata_table[param_key] = []
                            filedata_table[param_key].append(param_value)
                    else:
                        filedata_table[param_key] = param_value
                if len(filedata_table) > 0:
                    if interface_index in interface_info:
                        interface_info[interface_index].update(filedata_table)
                    else:
                        interface_info[interface_index] = filedata_table

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
                if 'InstanceID' not in row:
                    continue
                filedata_table = interface_info[row['InstanceID']]
                row.pop('InstanceID')
                for param_key, param_value in row.items():
                    if param_key == 'Action':
                        filedata_table['FirewallAction'] = param_value
                    elif param_key == 'Description':
                        filedata_table['RuleDescription'] = param_value
                    else:
                        filedata_table[param_key] = param_value
                if len(filedata_table) > 0:
                    filedata_table['Action'] = 'present'
                    result_filedata_list.append(filedata_table) 

result = {}
target_parameter_root_key = 'VAR_WIN_NetFirewallRule_Outbound'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

