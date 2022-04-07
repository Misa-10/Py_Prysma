import pyautogui
from pyautogui import *
from pprint import pprint
import os
from API.Timer import *

Data_Connection = {
    "BtnJouer" : [],
    "Serv1" : [],
    "Serv2" : [],
    "Serv3" : [],
    "Serv4" : [],
    "Serv5" : [],
    "Pers1" : [],
    "Pers2" : [],
    "Pers3" : [],
    "Pers4" : [],
    "Pers5" : [],
}

def GetBtnJouer():
 global Data_Connection
 
 BtnJouer_Pos = pyautogui.position()
 BtnJouer_Screen = pyautogui.screenshot('BtnJouer.png')
 BtnJouer_Color = BtnJouer_Screen.getpixel(BtnJouer_Pos)
 
 Data_Connection["BtnJouer"].extend(BtnJouer_Color)
 Data_Connection["BtnJouer"].extend(BtnJouer_Pos)

 os.remove('BtnJouer.png')
 pprint(Data_Connection)


def GetServ1():
 global Data_Connection
 Serv1_Pos = pyautogui.position()
 Serv1_Screen = pyautogui.screenshot('Serv1.png')
 Serv1_Color = Serv1_Screen.getpixel(Serv1_Pos)
 
 Data_Connection["Serv1"].extend(Serv1_Color)
 Data_Connection["Serv1"].extend(Serv1_Pos)

 os.remove('Serv1.png')
 
 pprint(Data_Connection)



def GetServ2():
 global Data_Connection
 Serv2_Pos = pyautogui.position()
 Serv2_Screen = pyautogui.screenshot('Serv2.png')
 Serv2_Color = Serv2_Screen.getpixel(Serv2_Pos)
 
 Data_Connection["Serv2"].extend(Serv2_Color)
 Data_Connection["Serv2"].extend(Serv2_Pos)

 os.remove('Serv2.png')
 
 pprint(Data_Connection)



def GetServ3():
 global Data_Connection
 Serv3_Pos = pyautogui.position()
 Serv3_Screen = pyautogui.screenshot('Serv3.png')
 Serv3_Color = Serv3_Screen.getpixel(Serv3_Pos)
 
 Data_Connection["Serv3"].extend(Serv3_Color)
 Data_Connection["Serv3"].extend(Serv3_Pos)

 os.remove('Serv3.png')
 
 pprint(Data_Connection)


def GetServ4():
 global Data_Connection
 Serv4_Pos = pyautogui.position()
 Serv4_Screen = pyautogui.screenshot('Serv4.png')
 Serv4_Color = Serv4_Screen.getpixel(Serv4_Pos)
 
 Data_Connection["Serv4"].extend(Serv4_Color)
 Data_Connection["Serv4"].extend(Serv4_Pos)

 os.remove('Serv4.png')
 
 pprint(Data_Connection)



def GetServ5():
 global Data_Connection
 Serv5_Pos = pyautogui.position()
 Serv5_Screen = pyautogui.screenshot('Serv5.png')
 Serv5_Color = Serv5_Screen.getpixel(Serv5_Pos)
 
 Data_Connection["Serv5"].extend(Serv5_Color)
 Data_Connection["Serv5"].extend(Serv5_Pos)

 os.remove('Serv5.png')
 
 pprint(Data_Connection)



def GetPers1():
 global Data_Connection
 Pers1_Pos = pyautogui.position()
 Pers1_Screen = pyautogui.screenshot('Pers1.png')
 Pers1_Color = Pers1_Screen.getpixel(Pers1_Pos)
 
 Data_Connection["Pers1"].extend(Pers1_Color)
 Data_Connection["Pers1"].extend(Pers1_Pos)

 os.remove('Pers1.png')
 
 pprint(Data_Connection)



def GetPers2():
 global Data_Connection
 Pers2_Pos = pyautogui.position()
 Pers2_Screen = pyautogui.screenshot('Pers2.png')
 Pers2_Color = Pers2_Screen.getpixel(Pers2_Pos)
 
 Data_Connection["Pers2"].extend(Pers2_Color)
 Data_Connection["Pers2"].extend(Pers2_Pos)

 os.remove('Pers2.png')
 
 pprint(Data_Connection)


def GetPers3():
 global Data_Connection
 Pers3_Pos = pyautogui.position()
 Pers3_Screen = pyautogui.screenshot('Pers3.png')
 Pers3_Color = Pers3_Screen.getpixel(Pers3_Pos)
 
 Data_Connection["Pers3"].extend(Pers3_Color)
 Data_Connection["Pers3"].extend(Pers3_Pos)

 os.remove('Pers3.png')
 
 pprint(Data_Connection)



def GetPers4():
 global Data_Connection
 Pers4_Pos = pyautogui.position()
 Pers4_Screen = pyautogui.screenshot('Pers4.png')
 Pers4_Color = Pers4_Screen.getpixel(Pers4_Pos)
 
 Data_Connection["Pers4"].extend(Pers4_Color)
 Data_Connection["Pers4"].extend(Pers4_Pos)

 os.remove('Pers4.png')
 
 pprint(Data_Connection)


def GetPers5():
 global Data_Connection
 Pers5_Pos = pyautogui.position()
 Pers5_Screen = pyautogui.screenshot('Pers5.png')
 Pers5_Color = Pers5_Screen.getpixel(Pers5_Pos)
 
 Data_Connection["Pers5"].extend(Pers5_Color)
 Data_Connection["Pers5"].extend(Pers5_Pos)

 os.remove('Pers5.png')
 
 pprint(Data_Connection)
