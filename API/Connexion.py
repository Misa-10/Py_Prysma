import pyautogui
from pyautogui import *
from pprint import pprint
import API.Json_API as Json_API
from API.Json_API import *
import pyperclip
import subprocess


Name_config = None
pid = None
Pid_Window = []
Window_state = 0
 
def Connection_Window(string):
 global pid
 global Name_config
 global Window_state
 Read_json()
 Name_config = string
 path = Json_API.Json_data3["Linkdofus"]
 subprocess.Popen([path])
 Window_state = Window_state+1
 print("Dofus Retro Start") 
 
 pid = os.getpid()
 
 Pid_Window.append(pid)
 
 
 
 def Connection_Compte():
     
     while True:
      GetColor = pyautogui.pixelMatchesColor(Json_API.Json_data2["BtnJouer"]["Pos"][0], Json_API.Json_data2["BtnJouer"]["Pos"][1], (Json_API.Json_data2["BtnJouer"]["Color"][0], Json_API.Json_data2["BtnJouer"]["Color"][1], Json_API.Json_data2["BtnJouer"]["Color"][2]), tolerance=10)
      pprint(pyautogui.pixelMatchesColor(Json_API.Json_data2["BtnJouer"]["Pos"][0], Json_API.Json_data2["BtnJouer"]["Pos"][1], (Json_API.Json_data2["BtnJouer"]["Color"][0], Json_API.Json_data2["BtnJouer"]["Color"][1], Json_API.Json_data2["BtnJouer"]["Color"][2]), tolerance=10))
      if GetColor == True:
     
       pyperclip.copy(Json_API.Json_data[Name_config]["data"]["username"][Window_state-1])
       pyautogui.keyDown('ctrl')
       pyautogui.press('v')
       pyautogui.keyUp('ctrl')
       pyautogui.press("tab")
       pyperclip.copy(Json_API.Json_data[Name_config]["data"]["passw"][Window_state-1])
       pyautogui.keyDown('ctrl')
       pyautogui.press('v')
       pyautogui.keyUp('ctrl')      
       pyautogui.press("enter")
       break
   
 def Choose_Server():
     if Json_API.Json_data[Name_config]["numberserver"] == "1":
      print("Serveur 1")
      ServN = "Serv1"
     elif Json_API.Json_data[Name_config]["numberserver"] == "2":
      print("Serveur 2")
      ServN = "Serv2"
     elif Json_API.Json_data[Name_config]["numberserver"] == "3":
      print("Serveur 3")
      ServN = "Serv3"
     elif Json_API.Json_data[Name_config]["numberserver"] == "4":
      print("Serveur 4")
      ServN = "Serv4"
     elif Json_API.Json_data[Name_config]["numberserver"] == "5":
      print("Serveur 5")
      ServN = "Serv5"
     while True:
             GetColor = pyautogui.pixelMatchesColor(Json_API.Json_data2[ServN]["Pos"][0], Json_API.Json_data2[ServN]["Pos"][1], (Json_API.Json_data2[ServN]["Color"][0], Json_API.Json_data2[ServN]["Color"][1], Json_API.Json_data2[ServN]["Color"][2]), tolerance=10)
             pprint(pyautogui.pixelMatchesColor(Json_API.Json_data2[ServN]["Pos"][0], Json_API.Json_data2[ServN]["Pos"][1], (Json_API.Json_data2[ServN]["Color"][0], Json_API.Json_data2[ServN]["Color"][1], Json_API.Json_data2[ServN]["Color"][2]), tolerance=10))
             if GetColor == True:
                 pyautogui.click(Json_API.Json_data2[ServN]["Pos"][0],Json_API.Json_data2[ServN]["Pos"][1],clicks=2)
                 break
             
             
 def Choose_Personnage():
     if Json_API.Json_data[Name_config]["data"]["numberpersonnage"][Window_state-1] == "1":
      print("Personnage 1")
      PersN = "Pers1"
     elif Json_API.Json_data[Name_config]["data"]["numberpersonnage"][Window_state-1] == "2":
      print("Personnage 2")
      PersN = "Pers2"
     elif Json_API.Json_data[Name_config]["data"]["numberpersonnage"][Window_state-1] == "3":
      print("Personnage 3")
      PersN = "Pers3"
     elif Json_API.Json_data[Name_config]["data"]["numberpersonnage"][Window_state-1] == "4":
      print("Personnage 4")
      PersN = "Pers4"
     elif Json_API.Json_data[Name_config]["data"]["numberpersonnage"][Window_state-1] == "5":
      print("Personnage 5")
      PersN = "Pers5"
     while True:
             GetColor = pyautogui.pixelMatchesColor(Json_API.Json_data2[PersN]["Pos"][0], Json_API.Json_data2[PersN]["Pos"][1], (Json_API.Json_data2[PersN]["Color"][0], Json_API.Json_data2[PersN]["Color"][1], Json_API.Json_data2[PersN]["Color"][2]), tolerance=10)
             pprint(pyautogui.pixelMatchesColor(Json_API.Json_data2[PersN]["Pos"][0], Json_API.Json_data2[PersN]["Pos"][1], (Json_API.Json_data2[PersN]["Color"][0], Json_API.Json_data2[PersN]["Color"][1], Json_API.Json_data2[PersN]["Color"][2]), tolerance=10))
             if GetColor == True:
                 pyautogui.click(Json_API.Json_data2[PersN]["Pos"][0],Json_API.Json_data2[PersN]["Pos"][1],clicks=2)
                 break
 
 
 if pid != None:
     
     time.sleep(3)
     pyautogui.keyDown('win')
     pyautogui.press('up')
     pyautogui.keyUp('win')
     time.sleep(3)
     Connection_Compte()
     time.sleep(3)
     Choose_Server()
     time.sleep(3)
     Choose_Personnage()
 if int(Json_API.Json_data[Name_config]["numberaccount"]) == Window_state:
     pprint("Connection fini")
 elif int(Json_API.Json_data[Name_config]["numberaccount"]) > 1:
     time.sleep(3)
     Connection_Window(string)
     
         

  