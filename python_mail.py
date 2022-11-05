#encoding:utf-8
#!/usr/bin/python
import requests
import urllib

url = "http://api.sendcloud.net/apiv2/mail/send"                         

API_USER = '_Jarvis__test_bJO5SR'
API_KEY = 'f8657d0ca35bfc2bb02b2d84d6353b4c'


params = {                                                                      
    "apiUser": API_USER, # Verification using api_user and api_key
    "apiKey" : API_KEY,                                             
    "to" : mail, # The recipient address,use the correct email address instead, multiple addresses with '; 'delimited
    "from" : "Jarvis@bu3KSTvZIkjR4A4wgHKKrMVVilyMQjYW.sendcloud.org", # The sender, use the correct email address instead
    "fromName" : "Jarvis",                                                    
    "subject" : "mailtext",
    "html" : "南昌: message"
}                                                                               

filename1 = "out.log"
display_filename_1 = "log.txt"

files = {
    "attachments" : (urllib.quote(display_filename_1), open(filename1, 'rb'),'application/octet-stream')
}

r = requests.post(url, files=files, data=params)

print r.text
