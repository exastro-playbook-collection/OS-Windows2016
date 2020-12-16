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
                    filedata_table[param_key] = param_value
                filedata_table['Action'] = 'present'
                result_filedata_list_all.append(filedata_table)

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
                group_domain = ''
                group_name = ''
                user_name = ''
                for param_key, param_value in row.items():
                    param_value_list = re.split('^.*Domain="(.*)",Name="(.*)".*$', param_value)
                    if param_key == 'GroupComponent':
                        group_domain = param_value_list[1]
                        group_name = param_value_list[2]
                    elif param_key == 'PartComponent':
                        user_name = param_value_list[2]
                for filedata_table in result_filedata_list_all:
                    if filedata_table['Domain'] == group_domain and filedata_table['Name'] == group_name:
                        if 'user' not in filedata_table:
                            filedata_table['user'] = []
                        filedata_table['user'].append(user_name)
                        break

result = {}
target_parameter_root_key = 'VAR_WIN_Group'
result[target_parameter_root_key] = result_filedata_list_all
print(json.dumps(result))

