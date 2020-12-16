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

ifdec_table = {}
result_filedata_list = []

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
                if_desc = ''
                if_index = -1
                for param_key, param_value in row.items():
                    if param_key == 'ifDesc':
                        if_desc = param_value
                    elif param_key == 'InterfaceIndex':
                        if_index = param_value
                if if_index >= 0:
                    ifdec_table[if_index] = if_desc

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
                if_index = -1
                filedata_table = {}
                for param_key, param_value in row.items():
                    if param_key == 'InterfaceIndex':
                        if_index = param_value
                    elif param_key == 'Store':
                        filedata_table['PolicyStore'] = param_value
                    elif param_key == 'PrefixLength':
                        filedata_table['prefix'] = param_value
                    elif param_key == 'IPAddress':
                        filedata_table['ipaddr'] = param_value
                    else:
                        filedata_table[param_key] = param_value
                if len(filedata_table) > 0:
                    if if_index in ifdec_table:
                        filedata_table['ifDesc'] = ifdec_table[if_index]
                        filedata_table['Action'] = 'present'
                        result_filedata_list.append(filedata_table)

result = {}
target_parameter_root_key = 'VAR_WIN_NetIpAddress'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

