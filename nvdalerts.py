# NVD-Alerts Script
# Version 1.0
# Author: Ahmed Musaad

import json
import datetime
import requests
import wget
import os


def download_feed():
    # Download the JSON file
    url = 'https://nvd.nist.gov/feeds/json/cve/1.0/nvdcve-1.0-recent.json.zip'
    wget.download(url)
    command = 'unzip -o nvdcve-1.0-recent.json.zip'
    os.system(command)
    print('File Downloaded Successfully')


def read_terms():
    # Load the list of vendors
    with open('terms.txt', 'r') as v:
        terms = v.readlines()
        return terms


def load_json():
    # Load the NVD Json file
    with open('nvdcve-1.0-recent.json', 'r') as f:
        cve_dict = json.load(f)
        return cve_dict


def parse_feed_json(cve_dict, terms):
    # Define Important variables
    loop_counter = cve_dict['CVE_Items']
    cve_counter = 0
    num_of_cves = 0
    result = ''

    for x in loop_counter:
        # Extract information from the json
        cve_id = cve_dict['CVE_Items'][cve_counter]['cve']['CVE_data_meta']['ID']
        cve_description = cve_dict['CVE_Items'][cve_counter]['cve']['description']['description_data'][0]['value']

        # Look only for relevant CVEs using the terms from the file
        for line in terms:
            for term in line.split():
                if cve_description.find(term) != -1:
                    result = result + cve_id + ' -- ' + term + '\n'

        # Increment Counters
        num_of_cves = num_of_cves + 1
        cve_counter = cve_counter + 1

    result = result + '\n' + 'Total Number of Recent CVEs: ' + str(num_of_cves) + '\n'
    return result


def send_email(message):
    # Email the list of CVEs using Mailgun service
    now = datetime.datetime.now().strftime("%m%d%y")
    key = 'key-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    recipient = "Put an email address here"
    request_url = 'https://api.mailgun.net/v3/xxxxxxxxxxxx/messages'

    request = requests.post(request_url, auth=('api', key), data={
        'from': 'your sending email address',
        'to': recipient,
        'subject': 'New CVEs ' + now,
        'text': 'Here are the new CVEs for Today: \n\n\n' + message
    })

    print('Email Sent Successfully')


def main():
    print("NVD Alerts\nVersion 1.2\n\n")
    # download_feed()
    result = parse_feed_json(load_json(), read_terms())
    print(result)
    print('Script Completed Successfully')


if __name__ == '__main__':
    main()
