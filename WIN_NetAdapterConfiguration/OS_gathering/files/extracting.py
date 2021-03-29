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
interface_info = {}

target_filepath_list = []
target_filepath_list.append('/1/stdout.txt')
target_filepath_list.append('/3/stdout.txt')
target_filepath_list.append('/4/stdout.txt')
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
                if 'InterfaceIndex' not in row:
                    continue
                interface_index = row['InterfaceIndex']
                row.pop('InterfaceIndex')
                for param_key, param_value in row.items():
                    if param_key == 'DefaultIPGateway':
                        filedata_table['DefaultIPv6Gateway'] = []
                        filedata_table['DefaultIPv4Gateway'] = []
                        if param_value is not None:
                            for address_value in param_value:
                                if address_value.find(':') != -1:
                                    address_key = 'DefaultIPv6Gateway'
                                else:
                                    address_key = 'DefaultIPv4Gateway'
                                if address_value not in filedata_table[address_key]:
                                    filedata_table[address_key].append(address_value)
                    elif param_key == 'DNSServerSearchOrder':
                        address_key = 'IPv4DNS'
                        filedata_table[address_key] = []
                        if param_value is not None:
                            for address_value in param_value:
                                if address_value.find(':') == -1:
                                    if address_value not in filedata_table[address_key]:
                                        filedata_table[address_key].append(address_value)
                    elif param_key == 'ServerAddresses':
                        address_key = 'IPv6DNS'
                        filedata_table[address_key] = []
                        if param_value is not None:
                            for address_value in param_value:
                                if address_value.find(':') != -1:
                                    if address_value not in filedata_table[address_key]:
                                        filedata_table[address_key].append(address_value)
                    elif param_key == 'TcpipNetbiosOptions':
                        filedata_table['NetBIOSSetting'] = param_value
                    elif param_key == 'Description':
                        filedata_table['ifDesc'] = param_value
                    else:
                        filedata_table[param_key] = param_value
                if len(filedata_table) > 0:
                    if interface_index in interface_info:
                        interface_info[interface_index].update(filedata_table)
                    else:
                        interface_info[interface_index] = filedata_table

target_filepath_list = []
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
                if 'InterfaceIndex' not in row:
                    continue
                interface_index = row['InterfaceIndex']
                row.pop('InterfaceIndex')
                if 'AddressFamily' not in row:
                    continue
                address_family = row['AddressFamily']
                row.pop('AddressFamily')
                for param_key, param_value in row.items():
                    if param_key == 'Dhcp':
                        if address_family == 2:
                            filedata_table['IPv4DHCPEnabled'] = param_value
                        elif address_family == 23:
                            filedata_table['IPv6DHCPEnabled'] = param_value
                    elif param_key == 'NlMtu':
                        if address_family == 2:
                            filedata_table['IPv4MTU'] = param_value
                        elif address_family == 23:
                            filedata_table['IPv6MTU'] = param_value
                if len(filedata_table) > 0:
                    if interface_index in interface_info:
                        interface_info[interface_index].update(filedata_table)
                    else:
                        interface_info[interface_index] = filedata_table

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
                if 'InterfaceIndex' not in row:
                    continue
                interface_index = row['InterfaceIndex']
                row.pop('InterfaceIndex')
                if interface_index in interface_info:
                    filedata_table = interface_info[interface_index]
                else:
                    filedata_table = {}
                for param_key, param_value in row.items():
                    if param_key == 'InterfaceAlias':
                        filedata_table['connection_name'] = param_value
                    else:
                        filedata_table[param_key] = param_value
                if len(filedata_table) > 0:
                    result_filedata_list.append(filedata_table) 

result = {}
target_parameter_root_key = 'VAR_WIN_NetAdapterConfiguration'
result[target_parameter_root_key] = result_filedata_list
print(json.dumps(result))

