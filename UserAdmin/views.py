from math import sin
from django.shortcuts import render
import random
from django.core.signing import Signer
from django.core import signing
from django.conf import settings

settings.configure()

singer=Signer()
real_value="Ajay Mandal"
encripted_Value=singer.sign(real_value)
print(encripted_Value)   #Ajay Mandal:njC-FR3naxXivozAwytJ8M1o2B6CwC3aMQk1VWxFECs

decrepted_value=singer.unsign(encripted_Value)
print(decrepted_value)


# how to signobject

objectData={"id":2,"name":"Ajay"}
encripted_Object_Value=singer.sign_object(objectData)
print(encripted_Object_Value)    #eyJpZCI6MiwibmFtZSI6IkFqYXkifQ:X6veZq0rm8WkPNBtdAq7rGebWe-kWn1N0qVsYPPNPxQ

try:
    decreted_object_value=singer.unsign_object(encripted_Object_Value)  #if Signature not mached than its throw django.core.signing.BadSignature excpetion
except signing.BadSignature:
    print("BadSignature")
print(decreted_object_value)



# importing the function from utils
from django.core.management.utils import get_random_secret_key

# generating and printing the SECRET_KEY
print(get_random_secret_key())



# import pyautogui
# import time
# breakTime=2
# while True:
#     try:

#         randomNumber1=random.randrange(-100,100)
#         randomNumber2=random.randrange(-100,100)
#         pyautogui.doubleClick()   
#         print(randomNumber1)
#         print(randomNumber2)
#         pyautogui.moveRel(randomNumber1, randomNumber2)
#         pyautogui.doubleClick()   
#         # time.sleep(2)
#         if breakTime:
#             time.sleep(breakTime)
    
#     except Exception as e:
#         pyautogui.moveRel(1, 10)

# pyautogui.moveRel(-20, 10)


