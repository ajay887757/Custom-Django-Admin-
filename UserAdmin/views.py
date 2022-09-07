from django.shortcuts import render
import random
from django.core.signing import Signer

singer=Signer()
real_value="Ajay Mandal"
encripted_Value=singer.sign(real_value)
print(encripted_Value)   #Ajay Mandal:njC-FR3naxXivozAwytJ8M1o2B6CwC3aMQk1VWxFECs

decrepted_value=singer.unsign(encripted_Value)
print(decrepted_value)


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


