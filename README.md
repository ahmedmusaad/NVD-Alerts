# NVD-Alerts
A small script that will send you a daily summary of new CVEs based on a list of predefined terms.

## Why?

Part of my daily job is to keep an eye on new vulnerabilities and part of that is sifting through the NIST NVD feeds. Going through those feeds can be exhausting and time-consuming as they contain a lot of information that might not be relevant to our work at all.

I wrote this script to parse the NVD Recent Feed and analyze the information extracted from it to check if a certain CVE is of interest to me or not (based on a list of terms). Once the analysis part is done, the script uses Mailgun services to email me a concise message with CVE IDs which I need to check.

## Requirements

The script has a few requirements, those are:

- Python3
- A mailgun account (Optional in case you want emails)
- wget
- requests

You can install the two python libraries by running the following commands:

```
pip3 install wget
pip3 install requests
```

## Email Configuration

If you wish to receive emails with the results of the script, you need to configure the email section with the following information:

- **key**: Your Mailgun API key.
- **recipient**: The email address where you want to receive the messages.
- **request_url**: A long URL you can find in your Mailgun account. It looks like this: https://api.mailgun.net/v3/Domainname/messages'

The code that sends the email is commented out by default, don't forget to uncomment it before running the script.

## Usage

1. First add the terms you want to monitor to the Terms text file. One term per line.
2. Either fill in the email configuration details and call the function in the main function or leave the code as it is.
3. Run the script using the following command:

```
python3 nvdalerts.py
```

The script will run smoothly if everything is configured correctly. You will get an email within a few minutes with the new CVE IDs that you need to check. 

If you disable emails, uncomment the print() function on **line 44** before running the script and you will get the results in your console.

## Automation

My main goal is to let this script run daily so automating it via cron jobs or any other method would be the next step but I won't get into that, Google cron jobs if you need to do this.

## Important Notice

This is by no means a perfect script, far from it. However, It does the job and I thought someone else might find it useful. Yes, it can be improved in many ways. Yes, the code is very simple. I am very aware of those things and I will work on improving them but for now, it works and I am satisfied with that. Feel free to open issues if something is broken.
