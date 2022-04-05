import pyautogui
from pyautogui import *
from pprint import pprint
import os
import API.Json_API as Json_API
from API.Json_API import *
pid = None
Pid_Window = []
qwerty = str.maketrans('azerty','qwerty')

path = "/Applications/Ankama/Retro/Dofus\ Retro.app"
os.system(f"open {path}")

print("Dofus Retro Start") 

pid = os.getpid()

Pid_Window.append(pid)






# qwerty = str.maketrans('azerty','qwerty')
# print('hello world!'.translate(qwerty))

def Connection_Compte():
    time.sleep(8)
    Read_json()
    pyautogui.write(Json_API.Json_data["a"]["data"]["username"][0].translate(qwerty))
    pyautogui.press("tab")
    pyautogui.write(Json_API.Json_data["a"]["data"]["passw"][0].translate(qwerty))
    pyautogui.press("enter")

def Choose_Server():
    time.sleep(8)
    while True:
     GetColor = pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))
     if GetColor == True:
         pyautogui.click(100, 200)
         break
    
    
     

if pid != None:
    time.sleep(5)
    print("PID is in locals")
    pyautogui.keyDown('command')
    pyautogui.press('f')
    pyautogui.keyUp('command')
    Connection_Compte()