#encoding:utf-8
#!/usr/bin/python
import requests
import urllib

url = "http://api.sendcloud.net/apiv2/mail/send"                         

API_USER = '****************'
API_KEY = '****************'


params = {                                                                      
    "apiUser": API_USER, # Verification using api_user and api_key
    "apiKey" : API_KEY,                                             
    "to" : mail, # The recipient address,use the correct email address instead, multiple addresses with '; 'delimited
    "from" : "***************", # The sender, use the correct email address instead
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
