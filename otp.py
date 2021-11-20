
import random
import requests
import json
pn='9042288986'
otp=str(random.randint(1000,9999))
# mention url 
url = "https://www.fast2sms.com/dev/bulk"
# create a dictionary 
my_data = { 
    # Your default Sender ID 
    'sender_id': 'FSTSMS', 
    
    # Put your message here! 
    'message': otp, 
    
    'language': 'english', 
    'route': 'p', 
    
    # You can send sms to multiple numbers 
    # separated by comma. 
    'numbers':pn    
} 

# create a dictionary 
headers = { 
    'authorization': 'KHJ1gZ5oXTBpGEAMSvCzhb4r39Dcta26QfmniWRxYjI7PLV8OwVjg43kpmeSMKT1fiqQ8rEXNohU0csG', 
    'Content-Type': "application/x-www-form-urlencoded", 
    'Cache-Control': "no-cache"
}

# make a post request 
response = requests.request("POST",url,data = my_data,headers = headers) 

returned_msg = json.loads(response.text) 

# print the send message 
print(returned_msg['message'])

