# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:56:39 2022

@author: devan
"""

import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " This is your Random otp test for a python programming ."
msg= otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("devanandrana168@gmail.com", "rgwtqtbgxpleymcy")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")