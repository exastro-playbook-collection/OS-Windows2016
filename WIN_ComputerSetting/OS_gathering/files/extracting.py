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
result_filedata_table['DomainUser'] = ''
result_filedata_table['DomainPassword'] = ''

target_filepath_list = []
target_filepath_list.append('/1/stdout.txt')
for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            lines = file_object.readlines()
            for line in lines:
                result_filedata_table['Name'] = line.strip()
                break

target_filepath_list = []
target_filepath_list.append('/0/stdout.txt')
target_filepath_list.append('/2/stdout.txt')
target_filepath_list.append('/3/stdout.txt')
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
                    if param_key == 'Description':
                        result_filedata_table['Description'] = param_value
                    elif param_key == 'SyncDomainWithMembership':
                        result_filedata_table['SyncDomainWithMembership'] = param_value
                    elif param_key == 'NV Domain':
                        result_filedata_table['DNSDomainSuffixSearchOrder'] = param_value
                    elif param_key == 'PartOfDomain':
                        result_filedata_table['DomainOrWorkgroup'] = param_value
                    elif param_key == 'Domain':
                        result_filedata_table['DomainOrWorkgroupName'] = param_value

result = {}
target_parameter_root_key = 'VAR_WIN_ComputerSetting'
result[target_parameter_root_key] = result_filedata_table
print(json.dumps(result))

