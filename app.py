from tkinter import *
from pprint import pprint
from tkinter.ttk import *


# Import of api
from API.Json_API import * 
from API.App_config_account import *
from API.Modif_config_account import *
from API.delete_config_account import *
import API.Json_API 
from API.Settings_pixel import *
import API.Connexion as Connexion
from API.Connexion import *

rowCheck = 0
columnCheck = 0
Json_data = {}
Config_radio = None
Number_radio =0


app = Tk()

# style of page
app.title("Main")
app.geometry("1500x500")

config_accoun_btn = Button(
    app, text='Créer une configuration comptes', command=lambda: [launch_app_config_account(app)]).grid(row=0, column=0, ipady=5, pady=10)

modif_config_account_btn = Button(
    app, text='Modifier la configuration', command=lambda: [launch_modif_config_account(app,Config_radio)]).grid(row=0, column=1, ipady=5, pady=10)

delete_config_account_btn = Button(
    app, text='Supprimer la configuration', command=lambda: [Delete_config(Config_radio)]).grid(row=0, column=2, ipady=5, pady=10)

Settings_connection_btn = Button(
    app, text='Paramètres pixel de connection', command=lambda: [Launch_Settings_Pixel(app)]).grid(row=0, column=3, ipady=5, pady=10)

StartDofus_btn = Button(
    app, text='Lancer Dofus', command=lambda: [Get_TheRadioChoosers(),Connection_Window(Number_radio)]).grid(row=0, column=4, ipady=5, pady=10)



def Generate_Checkbox():
    global rowCheck
    global columnCheck
    global Config_radio
   
    Config_radio = StringVar(app,"1")
    for x in Json_API.Json_data.keys():
        if rowCheck == 4:
            rowCheck = 1
            columnCheck = columnCheck + 1
        else:
            rowCheck = rowCheck + 1

        
       
        Radiobutton(app, text=x,
                    variable=Config_radio,
                    value=x).grid(row=rowCheck, column=columnCheck, ipady=5, pady=10)
 
def Get_TheRadioChoosers():
    global Config_radio
    global Number_radio
    Number_radio = Config_radio.get()
        
        





Read_json()
if Json_API.Json_data != None:
   Generate_Checkbox()

    
app.mainloop()

