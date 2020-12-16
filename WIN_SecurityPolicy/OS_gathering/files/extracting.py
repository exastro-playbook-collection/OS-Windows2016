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

target_filepath_list = []
target_filepath_list.append('/1/stdout.txt')
for target_filepath in target_filepath_list:
    filepath = path + '/command' + target_filepath
    if os.path.isfile(filepath) and os.path.getsize(filepath) > 0:
        result_filedata_table = {}
        with open(filepath) as file_object:
            section_dataset_table = {}
            section_data_table_list = []
            lines = file_object.readlines()
            section_name = ''
            for line in lines:
                if line[0]=="#":
                    continue
                # section serach
                search_result = re.search('^\\s*\\[(.+)\\]\\s*$', line)
                if search_result:
                    if section_name !='':
                        section_dataset_table['Section'] = section_name
                        section_dataset_table['Properties'] = section_data_table_list
                        result_filedata_list.append(section_dataset_table)
                        section_dataset_table = {}
                        section_data_table_list = []
                    section_name = search_result.group(1)
                else:
                    index = line.find('=')
                    if index != -1:
                        param_key = line[:index].strip()
                        param_value = line[(index + 1):].strip()
                        search_result = re.search('^".*"$', param_value)
                        if search_result:
                            param_value = re.sub('^"', '', param_value)
                            param_value = re.sub('"$', '', param_value)
                        section_data_table = {}
                        section_data_table['Key'] = param_key
                        section_data_table['Value'] = param_value
                        section_data_table_list.append(section_data_table)
            if section_name !='' and len(section_data_table_list) > 0:
                section_dataset_table['Section'] = section_name
                section_dataset_table['Properties'] = section_data_table_list
                result_filedata_list.append(section_dataset_table)

result = {}
target_parameter_root_key = 'VAR_WIN_SecurityPolicy'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

