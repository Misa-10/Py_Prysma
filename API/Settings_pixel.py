from tkinter import *
from pprint import pprint
from tkinter.ttk import *
from API.GetPixel_API import *
from API.Timer import *
import tkinter.filedialog
import API.Json_API as Json_API
from API.Json_API import *


def Launch_Settings_Pixel(string):
    app_settings_pixel = Toplevel(string)

    # style of page
    app_settings_pixel.title("Création de configuration")
    app_settings_pixel.geometry("800x500")
    
    BtnJouer_btn = Button(
    app_settings_pixel, text='Bouton Jouer', command=lambda: [Timer_app(app_settings_pixel),GetBtnJouer()]).grid(row=0, column=0, ipady=5, pady=10)
    
    Serv1_btn = Button(
    app_settings_pixel, text='Serveur 1', command=lambda: [Timer_app(app_settings_pixel),GetServ1()]).grid(row=1, column=0, ipady=5, pady=10)
    
    Serv2_btn = Button(
    app_settings_pixel, text='Serveur 2', command=lambda: [Timer_app(app_settings_pixel),GetServ2()]).grid(row=2, column=0, ipady=5, pady=10)
    
    Serv3_btn = Button(
    app_settings_pixel, text='Serveur 3', command=lambda: [Timer_app(app_settings_pixel),GetServ3()]).grid(row=3, column=0, ipady=5, pady=10)
    
    Serv4_btn = Button(
    app_settings_pixel, text='Serveur 4', command=lambda: [Timer_app(app_settings_pixel),GetServ4()]).grid(row=4, column=0, ipady=5, pady=10)
    
    Serv5_btn = Button(
    app_settings_pixel, text='Serveur 5', command=lambda: [Timer_app(app_settings_pixel),GetServ5()]).grid(row=5, column=0, ipady=5, pady=10)
    
    Pers1_btn = Button(
    app_settings_pixel, text='Personnage 1', command=lambda: [Timer_app(app_settings_pixel),GetPers1()]).grid(row=0, column=1, ipady=5, pady=10)
    
    Pers2_btn = Button(
    app_settings_pixel, text='Personnage 2', command=lambda: [Timer_app(app_settings_pixel),GetPers2()]).grid(row=1, column=1, ipady=5, pady=10)
    
    Pers3_btn = Button(
    app_settings_pixel, text='Personnage 3', command=lambda: [Timer_app(app_settings_pixel),GetPers3()]).grid(row=2, column=1, ipady=5, pady=10)
    
    Pers4_btn = Button(
    app_settings_pixel, text='Personnage 4', command=lambda: [Timer_app(app_settings_pixel),GetPers4()]).grid(row=3, column=1, ipady=5, pady=10)
    
    Pers5_btn = Button(
    app_settings_pixel, text='Personnage 5', command=lambda: [Timer_app(app_settings_pixel),GetPers5()]).grid(row=4, column=1, ipady=5, pady=10)

    LinkDofus_btn = Button(
    app_settings_pixel, text='LinkDofus', command=lambda: [Change_pathdofus()]).grid(row=5, column=1, ipady=5, pady=10)
    
    
    def Change_pathdofus():
      kfichier = tkinter.filedialog.askopenfilename ( title = "Sélectionnez un fichier ...")
    #   kfichier = kfichier.replace(" ","\ ")
      print (kfichier)
      Dict = { "Linkdofus" : kfichier }
      if Json_API.Json_data3 == None:
             Json_API.Json_data3 = Dict
      else:
        Json_API.Json_data3.update(Dict)
      Json_API.Write_json_Config_other()

