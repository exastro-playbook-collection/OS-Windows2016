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

count = 0
while True:
    # Decectory exist check
    dirpath = path + '/command/' + str(count)
    if os.path.isdir(dirpath):
        count +=1
    else:
        break

    filepath = dirpath + '/stdout.txt'
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        with open(filepath) as file_object:
            reader = json.load(file_object)
            if isinstance(reader, list):
                rows = reader
            else:
                rows = []
                rows.append(reader)
            for row in rows:
                if count % 2 == 1:
                    encrypt_table = {}
                    for param_key, param_value in row.items():
                        encrypt_table[param_key] = param_value
                else:
                    filedata_table = {}
                    for param_key, param_value in row.items():
                        if param_key == 'Path':
                            index = param_value.find('::')
                            if index != -1:
                                param_value = param_value[(index + 2):].strip()
                            if param_value in encrypt_table:
                                filedata_table['Encrypt'] = encrypt_table[param_value]
                            filedata_table['Name'] = param_value
                        elif param_key == 'AccessToString':
                            filedata_table[param_key] = param_value.split('\n')
                        else:
                            filedata_table[param_key] = param_value
                    if len(filedata_table) > 0:
                        filedata_table['Action'] = 'file'
                        result_filedata_list.append(filedata_table)

result = {}
target_parameter_root_key = 'VAR_WIN_FileProtectionSetting'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))
