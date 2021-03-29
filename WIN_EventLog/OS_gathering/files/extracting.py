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
registry_info = {}

target_filepath_list = []
target_filepath_list.append('/1/stdout.txt')
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
                child_name = ''
                for path_key, path_value in row.items():
                    filedata_table = {}
                    for param_key, param_value in path_value.items():
                        if param_key == 'logFileName':
                            filedata_table['LogPath'] = param_value
                        elif param_key == 'retention':
                            if param_value.lower() == 'true':
                                filedata_table['Retention'] = True
                            else:
                                filedata_table['Retention'] = False
                        elif param_key == 'autoBackup':
                            if param_value.lower() == 'true':
                                filedata_table['AutoBackup'] = True
                            else:
                                filedata_table['AutoBackup'] = False
                        else:
                            filedata_table[param_key] = param_value
                    if len(filedata_table) > 0:
                        registry_info[path_key] = filedata_table


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
                filedata_table = {}
                for param_key, param_value in row.items():
                    if param_key == 'OverflowAction':
                        if param_value == -1:
                            filedata_table[param_key] = 'DoNotOverwrite'
                        elif param_value == 0:
                            filedata_table[param_key] = 'OverwriteAsNeeded'
                        elif param_value == 1:
                            filedata_table[param_key] = 'OverwriteOlder'
                    elif param_key == 'LogName':
                        filedata_table['Log'] = param_value
                    elif param_key == 'MaximumSizeInBytes':
                        filedata_table['MaximumKilobytes'] = int(param_value / 1024)
                    else:
                        filedata_table[param_key] = param_value
                    if param_key == 'Log' or param_key == 'LogName':
                        if param_value in registry_info:
                            filedata_table.update(registry_info[param_value])
                if len(filedata_table) > 0:
                    result_filedata_list.append(filedata_table)

result = {}
target_parameter_root_key = 'VAR_WIN_EventLog'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

