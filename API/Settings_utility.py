from tkinter import *
from pprint import pprint
from tkinter.ttk import *
from API.GetPixel_API import *
from API.Timer import *
import tkinter.filedialog
import API.Json_API as Json_API
from API.Json_API import *


def Launch_Settings_Utility(string):
    app_settings_utility = Toplevel(string)

    # style of page
    app_settings_utility.title("Création de configuration")
    app_settings_utility.geometry("800x500")
    
    BtnPret_btn = Button(
    app_settings_utility, text='Bouton Pret', command=lambda: [Timer_app(app_settings_utility),GetBtnJouer()]).grid(row=0, column=0, ipady=5, pady=10)
    
    Serv1_btn = Button(
    app_settings_utility, text='Serveur 1', command=lambda: [Timer_app(app_settings_utility),GetServ1()]).grid(row=1, column=0, ipady=5, pady=10)
    
    
    
