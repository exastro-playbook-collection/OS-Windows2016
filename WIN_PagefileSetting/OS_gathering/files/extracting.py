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

filedata_table = {}
result_filedata_table_all = {}

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
                    filedata_table[param_key] = param_value
result_filedata_table_all['AutomaticManagedPagefileSetting'] = filedata_table

if not filedata_table['AutomaticManagedPagefile']:
    device_id_table = {}
    filepath = path + '/command' + '/1/stdout.txt'
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
                    device_id_table[param_value.lower()] = {}
    filepath = path + '/command' + '/2/stdout.txt'
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            reader = json.load(file_object)
            if isinstance(reader, list):
                rows = reader
            else:
                rows = []
                rows.append(reader)
            for row in rows:
                device_id = ''
                device_detail = {}
                for param_key, param_value in row.items():
                    if param_key == 'SettingID':
                        index = param_value.rfind(' ')
                        if index != -1:
                            device_id = param_value[(index + 1):].strip()
                    else:
                        device_detail[param_key] = param_value
                if len(device_detail) > 0:
                    device_id_table[device_id] = device_detail
    filedata_list = []
    for device_id, device_detail in device_id_table.items():
        filedata_table = {}
        filedata_table['DriveName'] = device_id
        if len(device_detail) > 0:
            filedata_table['Name'] = device_detail['Name']
            filedata_table['InitialSize'] = device_detail['InitialSize']
            filedata_table['MaximumSize'] = device_detail['MaximumSize']
            if filedata_table['InitialSize'] == 0 and filedata_table['MaximumSize'] == 0:
                filedata_table['PageFileSettingType'] = 'SystemManagedSize'
            else:
                filedata_table['PageFileSettingType'] = 'CustomSize'
        else:
            filedata_table['PageFileSettingType'] = 'NoPagingfile'
        filedata_list.append(filedata_table)
    result_filedata_table_all['Drive'] = filedata_list
                        
result = {}
target_parameter_root_key = 'VAR_WIN_PagefileSetting'
result[target_parameter_root_key] = result_filedata_table_all
print(json.dumps(result))

