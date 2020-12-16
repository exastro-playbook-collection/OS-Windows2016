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

target_data_list = []
target_data = {}
target_data['key'] = 'HKLM:\\SYSTEM\\CurrentControlSet\\services\W32Time\\TimeProviders\\NtpClient'
target_data['value_file'] = '/0/stdout.txt'
target_data['type_file'] = '/1/stdout.txt'
target_data_list.append(target_data)
target_data = {}
target_data['key'] = 'HKLM:\\SYSTEM\\CurrentControlSet\\services\\W32Time\\Parameters'
target_data['value_file'] = '/2/stdout.txt'
target_data['type_file'] = '/3/stdout.txt'
target_data_list.append(target_data)
target_data = {}
target_data['key'] = 'HKLM:\\SYSTEM\\CurrentControlSet\\Services\\W32Time\\Config'
target_data['value_file'] = '/4/stdout.txt'
target_data['type_file'] = '/5/stdout.txt'
target_data_list.append(target_data)
for target_data in target_data_list:
    filedata_table = {}
    filedata_table['Key'] = target_data['key']
    value_table = {}
    filepath = path + '/command' + target_data['value_file']
    if os.path.isfile(filepath):
        with open(filepath) as file_object:
            reader = json.load(file_object)
            if isinstance(reader, list):
                rows = reader
            else:
                rows = []
                rows.append(reader)
            for row in rows:
                for param_key, param_value in row.items():
                    value_table[param_key]= param_value
    registry_list = []
    filepath = path + '/command' + target_data['type_file']
    if os.path.isfile(filepath):
        with open(filepath) as file_object:
            lines = file_object.readlines()
            for line in lines:
                params = re.split('^\s*(.*)\s+(REG_\S*)\s+.*$', line)
                if len(params) == 4:
                    param_key = params[1].strip()
                    param_type = params[2].strip()
                    registry_data = {}
                    registry_data['ValueName'] = param_key
                    registry_data['ValueType'] = param_type
                    registry_data['Value'] = value_table[param_key]
                    registry_list.append(registry_data)
            filedata_table['Values'] = registry_list
    result_filedata_list.append(filedata_table)

result = {}
target_parameter_root_key = 'VAR_WIN_NtpClientSetting'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

