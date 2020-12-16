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

target_data_table = {}
target_data_table['User'] = '/0/stdout.txt'
target_data_table['Machine'] = '/1/stdout.txt'
for key, target_filepath in target_data_table.items():
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            env_list = []
            lines = file_object.readlines()
            for line in lines:
                params = re.split('^\s*(.*)\s+REG_\S*\s+(.*)$', line)
                if len(params) == 4:
                    env_info = {}
                    env_info['Name'] = params[1].strip()
                    env_info['Value'] = params[2].strip()
                    env_info['Action'] = 'present'
                    env_list.append(env_info)
            result_filedata_table[key] = env_list

result = {}
target_parameter_root_key = 'VAR_WIN_EnvSetting'
result[target_parameter_root_key] = result_filedata_table
print(json.dumps(result))

