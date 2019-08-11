# NVD Alerting Script
# Version 1.0
# Author: Ahmed Musaad

import json
import datetime
import requests
import wget
import os

# Download the JSON file
url = 'https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-recent.json.zip'
wget.download(url)
command = 'unzip -o nvdcve-1.0-recent.json.zip'
os.system(command)
print('File Downloaded Successfully')

# Load the list of vendors
with open('vendors.txt', 'r') as v:
    vendors = v.readlines()
    v.close()

# Load the NVD Json file
with open('nvdcve-1.0-recent.json', 'r') as f:
    cve_dict = json.load(f)
    f.close()

# Define Important variables
loop_counter = cve_dict['CVE_Items']
cve_counter = 0
num_of_cves = 0
Email_message = ''

for x in loop_counter:

    # Extract information from the json
    cve_id = cve_dict['CVE_Items'][cve_counter]['cve']['CVE_data_meta']['ID']
    cve_description = cve_dict['CVE_Items'][cve_counter]['cve']['description']['description_data'][0]['value']

    # Look only for relevant CVEs using the vendor names from the file
    for line in vendors:
        for vendor in line.split():
            if cve_description.find(vendor) != -1:
                #print(cve_id + ' -- ' + vendor)
                Email_message = Email_message + cve_id + ' -- ' + vendor + '\n'

    # Increment Counters
    num_of_cves = num_of_cves + 1
    cve_counter = cve_counter + 1

# Tell us how many CVEs were included in this file.
print(num_of_cves)

# Email the list of CVEs using Mailgun service
now = datetime.datetime.now().strftime("%m%d%y")
key = 'key-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
recipient = "Put an email address here"
request_url = 'https://api.mailgun.net/v3/xxxxxxxxxxxx/messages'

#request = requests.post(request_url, auth=('api', key), data={
#    'from': 'your sending email address',
#    'to': recipient,
#    'subject': 'New CVEs '+now,
#    'text': 'Here are the new CVEs for Today: \n\n\n' + Email_message
#})
print('Email Sent Successfully')
print('Script Completed Successfully')
