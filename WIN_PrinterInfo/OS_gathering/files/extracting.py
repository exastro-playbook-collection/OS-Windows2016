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

tcp_table = {}
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
                tcp_name = ''
                filedata_table = {}
                for param_key, param_value in row.items():
                    if param_key == 'Name':
                        tcp_name = param_value
                    elif param_key == 'PortNumber':
                        filedata_table['RawPortNumber'] = param_value
                    elif param_key == 'Queue':
                        filedata_table['LPRQueue'] = param_value
                    else:
                        filedata_table[param_key] = param_value
                if len(tcp_name) > 0:
                    tcp_table[tcp_name] = filedata_table

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
                filedata_table = {}
                detail_utilizationTime = None
                start_time = None
                until_time = None
                if 'Detail_UtilizationTime' in row:
                    detail_utilizationTime = row['Detail_UtilizationTime']
                    row.pop('Detail_UtilizationTime')
                if 'StartTime' in row:
                    start_time = row['StartTime']
                    row.pop('StartTime')
                if 'UntilTime' in row:
                    until_time = row['UntilTime']
                    row.pop('UntilTime')
                if detail_utilizationTime is not None:
                    filedata_table['Detail_UtilizationTime'] = detail_utilizationTime
                elif start_time is None and start_time is None:
                    filedata_table['Detail_UtilizationTime'] = 'always available'
                else:
                    filedata_table['Detail_UtilizationTime'] = start_time[9:10] + ':' + start_time[11:12] + '-' + until_time[9:10] + ':' + until_time[11:12]
                for param_key, param_value in row.items():
                    if param_key == 'PortName':
                        filedata_table[param_key] = param_value
                        if  param_value in tcp_table:
                            filedata_table.update(tcp_table[param_value])
                    elif param_key == 'Priority':
                        filedata_table['Detail_Priority'] = param_value
                    elif param_key == 'DriverName':
                        filedata_table['Detail_DriverName'] = param_value
                    elif param_key == 'SpoolEnabled':
                        filedata_table['Detail_SpoolEnabled'] = param_value
                    elif param_key == 'Queued':
                        filedata_table['Detail_Queued'] = param_value
                    elif param_key == 'EnableDevQueryPrint':
                        filedata_table['Detail_EnableDevQueryPrint'] = param_value
                    elif param_key == 'DoCompleteFirst':
                        filedata_table['Detail_DoCompleteFirst'] = param_value
                    elif param_key == 'KeepPrintedJobs':
                        filedata_table['Detail_KeepPrintedJobs'] = param_value
                    elif param_key == 'RawOnly':
                        filedata_table['Detail_RawOnly'] = param_value
                    else:
                        filedata_table[param_key] = param_value
                if len(filedata_table) > 0:
                    result_filedata_list.append(filedata_table)

result = {}
target_parameter_root_key = 'VAR_WIN_PrinterInfo'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

