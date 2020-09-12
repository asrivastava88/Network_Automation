# To convert Username:password into Base64 encoded value for "Authorization" header.
import base64
# To do HTTP requests - like GET, POST, DELETE, etc.
import requests
# To convert JSON dictionary to Python objects and vice versa.
import json
# To print the dictionary/object data in structured way.
from pprint import pprint
# To take input from user without echoing.
import getpass
# Python Warning related functions - to ignore warnings coming out during code execution
import warnings

####################################################################################
## GET Login Details from User - Target Device IP, Username, Password ##############
####################################################################################
get_ip = input(str("Please type IP or Hostname of the target device: "))
get_user = input(str("Please enter your username: "))
passwd = getpass.getpass("Password: ")

####################################################################################
## Convert Username & Password to Base64 encoded value to supply as header #########
####################################################################################

auth_header = str(f"{get_user}:{passwd}")

base64_encode = base64.b64encode(auth_header.encode("utf-8"))
auth_header_value = str(base64_encode, "utf-8")

####################################################################################
## Collecting all information in one code block ####################################
####################################################################################
user = str.upper(get_user)
print(f"\nConnecting to the Target Device {get_ip} via username {user}.")

rtr = {"ip": get_ip, "port": "9443"}

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
    'Authorization': f"Basic {auth_header_value}"}

url = str(
    f"https://{rtr['ip']}:{rtr['port']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces")

####################################################################################
## This will suppress warnings coming out during code execution ####################
####################################################################################

warnings.filterwarnings("ignore")

####################################################################################
## Defining action that needs to be performed ######################################
####################################################################################

pull_response = requests.get(url, headers=headers, verify=False)

api_data = pull_response.json()

counter = 0
inf_count = len(
    api_data['Cisco-IOS-XE-interfaces-oper:interfaces']['interface'])
print(inf_count)

while counter < inf_count:
    inf_status = api_data['Cisco-IOS-XE-interfaces-oper:interfaces']['interface'][counter]['admin-status']
    inf_name = api_data['Cisco-IOS-XE-interfaces-oper:interfaces']['interface'][counter]['name']
    if api_data['Cisco-IOS-XE-interfaces-oper:interfaces']['interface'][counter]['admin-status'] == 'if-state-up':
        print(f"Interface {inf_name} is UP!")
    else:
        print(f"Interface {inf_name} is DOWN!")
    counter += 1
