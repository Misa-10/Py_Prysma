import pyautogui
from pyautogui import *
from pprint import pprint
import os
from API.Timer import *
import API.Json_API as Json_API
from API.Json_API import *




def GetBtnJouer():

 BtnJouer_Pos = pyautogui.position()
 BtnJouer_Color = pyautogui.pixel(BtnJouer_Pos[0],BtnJouer_Pos[1])

 Dict = { "BtnJouer" : {"Pos" :[BtnJouer_Pos[0],BtnJouer_Pos[1]], "Color" : [BtnJouer_Color[0],BtnJouer_Color[1],BtnJouer_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()

   


def GetServ1():
    
 Serv1_Pos = pyautogui.position()
 Serv1_Color = pyautogui.pixel(Serv1_Pos[0],Serv1_Pos[1])

 Dict = { "Serv1" : {"Pos" :[Serv1_Pos[0],Serv1_Pos[1]], "Color" : [Serv1_Color[0],Serv1_Color[1],Serv1_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()



def GetServ2():
 Serv2_Pos = pyautogui.position()
 Serv2_Color = pyautogui.pixel(Serv2_Pos[0],Serv2_Pos[1])

 Dict = { "Serv2" : {"Pos" :[Serv2_Pos[0],Serv2_Pos[1]], "Color" : [Serv2_Color[0],Serv2_Color[1],Serv2_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()



def GetServ3():
 Serv3_Pos = pyautogui.position()
 Serv3_Color = pyautogui.pixel(Serv3_Pos[0],Serv3_Pos[1])

 Dict = { "Serv3" : {"Pos" :[Serv3_Pos[0],Serv3_Pos[1]], "Color" : [Serv3_Color[0],Serv3_Color[1],Serv3_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()


def GetServ4():
 Serv4_Pos = pyautogui.position()
 Serv4_Color = pyautogui.pixel(Serv4_Pos[0],Serv4_Pos[1])

 Dict = { "Serv4" : {"Pos" :[Serv4_Pos[0],Serv4_Pos[1]], "Color" : [Serv4_Color[0],Serv4_Color[1],Serv4_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()



def GetServ5():
 Serv5_Pos = pyautogui.position()
 Serv5_Color = pyautogui.pixel(Serv5_Pos[0],Serv5_Pos[1])

 Dict = { "Serv5" : {"Pos" :[Serv5_Pos[0],Serv5_Pos[1]], "Color" : [Serv5_Color[0],Serv5_Color[1],Serv5_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()



def GetPers1():
 Pers1_Pos = pyautogui.position()
 Pers1_Color = pyautogui.pixel(Pers1_Pos[0],Pers1_Pos[1])

 Dict = { "Pers1" : {"Pos" :[Pers1_Pos[0],Pers1_Pos[1]], "Color" : [Pers1_Color[0],Pers1_Color[1],Pers1_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()



def GetPers2():
 Pers2_Pos = pyautogui.position()
 Pers2_Color = pyautogui.pixel(Pers2_Pos[0],Pers2_Pos[1])

 Dict = { "Pers2" : {"Pos" :[Pers2_Pos[0],Pers2_Pos[1]], "Color" : [Pers2_Color[0],Pers2_Color[1],Pers2_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()


def GetPers3():
 Pers3_Pos = pyautogui.position()
 Pers3_Color = pyautogui.pixel(Pers3_Pos[0],Pers3_Pos[1])

 Dict = { "Pers3" : {"Pos" :[Pers3_Pos[0],Pers3_Pos[1]], "Color" : [Pers3_Color[0],Pers3_Color[1],Pers3_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()



def GetPers4():
 Pers4_Pos = pyautogui.position()
 Pers4_Color = pyautogui.pixel(Pers4_Pos[0],Pers4_Pos[1])

 Dict = { "Pers4" : {"Pos" :[Pers4_Pos[0],Pers4_Pos[1]], "Color" : [Pers4_Color[0],Pers4_Color[1],Pers4_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()


def GetPers5():
 Pers5_Pos = pyautogui.position()
 Pers5_Color = pyautogui.pixel(Pers5_Pos[0],Pers5_Pos[1])

 Dict = { "Pers5" : {"Pos" :[Pers5_Pos[0],Pers5_Pos[1]], "Color" : [Pers5_Color[0],Pers5_Color[1],Pers5_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()
 
def GetBtnPret():

 BtnPret_Pos = pyautogui.position()
 BtnPret_Color = pyautogui.pixel(BtnPret_Pos[0],BtnPret_Pos[1])

 Dict = { "BtnPret" : {"Pos" :[BtnPret_Pos[0],BtnPret_Pos[1]], "Color" : [BtnPret_Color[0],BtnPret_Color[1],BtnPret_Color[2]]} }
 Read_json()
 if Json_API.Json_data2 == None:
             Json_API.Json_data2 = Dict
 else:
  Json_API.Json_data2.update(Dict)
  
 Json_API.Write_json_Config_Pixel_Connection()

