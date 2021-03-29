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
failure_info = {}

target_filepath_list = []
target_filepath_list.append('/2/stdout.txt')
for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            lines = file_object.readlines()
            service_name = ''
            filedata_table = {}
            param_key = ''
            for line in lines:
                index = line.find(':')
                if index != -1:
                    param_key = line[:index].strip()
                    param_value = line[(index + 1):].strip()
                    if param_key == 'SERVICE_NAME':
                        service_name = param_value
                    elif param_key == 'RESET_PERIOD (in seconds)':
                        filedata_table['ResetPeriod(sec)'] = param_value
                    elif param_key == 'REBOOT_MESSAGE':
                        filedata_table['RebootMessage'] = param_value
                    elif param_key == 'COMMAND_LINE':
                        filedata_table['CmdLine'] = param_value
                    elif param_key == 'FAILURE_ACTIONS':
                        param_value_list = param_value.split()
                        failure_action_no = 1
                        if param_value_list[3] == '=':
                            filedata_table['FailureAction' + str(failure_action_no)] = param_value_list[0]
                            filedata_table['Delay' + str(failure_action_no) + '(msec)'] = param_value_list[4]
                        else:
                            filedata_table['FailureAction' + str(failure_action_no)] = param_value_list[0] + ' ' + param_value_list[1]
                            filedata_table['Delay' + str(failure_action_no) + '(msec)'] = param_value_list[5]
                elif param_key == 'FAILURE_ACTIONS' and len(line.strip()) > 0:
                    param_value = line.strip()
                    param_value_list = param_value.split()
                    if failure_action_no < 3:
                        failure_action_no += 1
                        if param_value_list[3] == '=':
                            filedata_table['FailureAction' + str(failure_action_no)] = param_value_list[0]
                            filedata_table['Delay' + str(failure_action_no) + '(msec)'] = param_value_list[4]
                        else:
                            filedata_table['FailureAction' + str(failure_action_no)] = param_value_list[0] + ' ' + param_value_list[1]
                            filedata_table['Delay' + str(failure_action_no) + '(msec)'] = param_value_list[5]
                else:
                    if len(service_name) > 0 and len(filedata_table) > 0:
                        failure_info[service_name] = filedata_table
                        service_name = ''
                        filedata_table = {}
                        param_key = ''

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
                    if param_key == 'Name':
                        filedata_table[param_key] = param_value
                        if param_value in failure_info:
                            filedata_table.update(failure_info[param_value])
                    elif param_key == 'StartMode':
                        filedata_table['StartType'] = param_value
                    elif param_key == 'State':
                        filedata_table['Status'] = param_value
                    else:
                        filedata_table[param_key] = param_value
                if len(filedata_table) > 0:
                    result_filedata_list.append(filedata_table)

result = {}
target_parameter_root_key = 'VAR_WIN_Services'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

