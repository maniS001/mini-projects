import random
from math import *
from smtplib import *
s = SMTP("smtp.gmail.com" , 587)  # 587 is a port number
# start TLS for E-mail security 
s.starttls()
# Log in to your gmail account
s.login("mkingdom209@gmail.com" , "+919688453632")
otp = random.randint(1000, 9999)
otp = str(otp)
receiver_email='roughid001@gmail.com'
s.sendmail("manimani" , receiver_email , otp)
print("OTP sent succesfully..")
# close smtp session
s.quit()