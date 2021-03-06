# coding: utf-8

from tkinter import *
from pprint import pprint
from tkinter.ttk import *
from tkinter import messagebox

# Import of api
import API.Json_API as Json_API
from API.Json_API import *


Username_entry = None
passw_entry = None
numberaccount_Combobox = None
numberserver_Combobox = None
numberpersonnage_Combobox = None
config_data = None
nameconfig_data = None
nameconfig_entry = None
numberaccount_data = "10000"


account_Data_array = []

# pprint(app)
x = -1


def launch_app_config_account(string):
    global nameconfig_entry

   
    
    app_config_account = Toplevel(string)

    # style of page
    app_config_account.title("Création de configuration")
    app_config_account.geometry("800x500")

    def Page_account():
        global x
        global Username_entry
        global passw_entry
        global nameconfig_entry
        global numberaccount_Combobox
        global numberserver_Combobox
        global numberpersonnage_Combobox
        x = x+1
        pprint(x)
        pprint(int(numberaccount_data))
        if x == 0:
            nameconfig_label = Label(
                app_config_account, text='Nom de configuration', font=('calibre', 15, 'bold')).grid(row=0, column=0, ipady=5, pady=10)

            nameconfig_entry = Entry(
                app_config_account, font=('calibre', 15, 'normal'))
            nameconfig_entry.grid(row=1, column=0, ipady=5, pady=10)

            numberaccount_label = Label(
                app_config_account, text='Nombre de compte', font=('calibre', 15, 'bold')).grid(row=2, column=0, ipady=5, pady=10)

            numberaccount_Combobox = Combobox(
                app_config_account, values=["1", "2", "3", "4", "5", "6", "7", "8"], font=('calibre', 15, 'bold'))
            numberaccount_Combobox.grid(row=3, column=0, ipady=2, pady=10)
            
            numberserver_label = Label(
                app_config_account, text='Numéro de votre serveur (gauche à droite)', font=('calibre', 15, 'bold')).grid(row=4, column=0, ipady=5, pady=10)

            numberserver_Combobox = Combobox(
                app_config_account, values=["1", "2", "3", "4", "5"], font=('calibre', 15, 'bold'))
            numberserver_Combobox.grid(row=5, column=0, ipady=2, pady=10)


            sub_btn = Button(app_config_account, text='Suivant', command=lambda: [
                             Check_input_filled()]).grid(row=7, column=1, ipady=5, pady=10)
            

        elif x == int(numberaccount_data):
            Account_label = Label(app_config_account, text='Compte '+str(x),
                                  font=('calibre', 15, 'bold')).grid(row=0, column=3, ipady=5, pady=10)
            Username_label = Label(app_config_account, text='Username',
                                   font=('calibre', 15, 'bold')).grid(row=1, column=1, ipady=5, pady=10)
            Username_entry = Entry(
                app_config_account, font=('calibre', 15, 'normal'))
            Username_entry.grid(row=1, column=2, ipady=5, pady=10)
            passw_label = Label(app_config_account,
                                text='Password', font=('calibre', 15, 'bold')).grid(row=2, column=1, ipady=5, pady=10)
            passw_entry = Entry(app_config_account,
                                font=('calibre', 15, 'normal'))
            passw_entry.grid(row=2, column=2, ipady=5, pady=10)
            
            numberpersonnage_label = Label(
                app_config_account, text='Numéro de votre personnage (gauche à droite)', font=('calibre', 15, 'bold')).grid(row=3, column=1, ipady=5, pady=10)

            numberpersonnage_Combobox = Combobox(
                app_config_account, values=["1", "2", "3", "4", "5"], font=('calibre', 15, 'bold'))
            numberpersonnage_Combobox.grid(row=3, column=2, ipady=2, pady=10)

            Save_btn = Button(app_config_account, text='Sauvegarder', command=lambda: [
                              Check_input_filled()]).grid(row=4, column=2, ipady=5, pady=10)
        else:

            Account_label = Label(app_config_account, text='Compte '+str(x),
                                  font=('calibre', 15, 'bold')).grid(row=0, column=3, ipady=5, pady=10)

            Username_label = Label(app_config_account, text='Username',
                                   font=('calibre', 15, 'bold')).grid(row=1, column=1, ipady=5, pady=10)

            Username_entry = Entry(
                app_config_account, font=('calibre', 15, 'normal'))
            Username_entry.grid(row=1, column=2, ipady=5, pady=10)

            passw_label = Label(app_config_account,
                                text='Password', font=('calibre', 15, 'bold')).grid(row=2, column=1, ipady=5, pady=10)

            passw_entry = Entry(app_config_account,
                                font=('calibre', 15, 'normal'))
            passw_entry.grid(row=2, column=2, ipady=5, pady=10)
            
            numberpersonnage_label = Label(
                app_config_account, text='Numéro de votre personnage (gauche à droite)', font=('calibre', 15, 'bold')).grid(row=3, column=1, ipady=5, pady=10)

            numberpersonnage_Combobox = Combobox(
                app_config_account, values=["1", "2", "3", "4", "5"], font=('calibre', 15, 'bold'))
            numberpersonnage_Combobox.grid(row=3, column=2, ipady=2, pady=10)

            sub_btn = Button(app_config_account, text='Suivant', command=lambda: [
                             Check_input_filled()]).grid(row=4, column=2, ipady=5, pady=10)

    def Get_Data_account():

        Username_data = Username_entry.get()
        passw_data = passw_entry.get()
        numberpersonnage_data = numberpersonnage_Combobox.get()

        pprint(Username_data)
        config_data[nameconfig_data]['data']['username'].append(Username_data)
        config_data[nameconfig_data]['data']['passw'].append(passw_data)
        config_data[nameconfig_data]['data']['numberpersonnage'].append(numberpersonnage_data)
        pprint(config_data[nameconfig_data]['data']['username'])


    def Get_Data_config():
        global config_data
        global nameconfig_data
        global numberaccount_data
        
        
        pprint(nameconfig_entry)

        nameconfig_data = nameconfig_entry.get()
        numberaccount_data = numberaccount_Combobox.get()
        numberserver_data = numberserver_Combobox.get()

        config_data = {
            nameconfig_data: {
                "nameconfig": nameconfig_data,
                "numberaccount": numberaccount_data,
                "numberserver": numberserver_data,
                "data": {
                    "username": [],
                    "passw": [],
                    "numberpersonnage": []}

            }
        }

    def Clear_page():
        for child in app_config_account.winfo_children():
            child.destroy()

    def Check_input_filled():
        y = 0
        for child in app_config_account.winfo_children():

            if child.winfo_class() == "TEntry":
                if child.get() == "":
                    y = y+1

        if y > 0:
            messagebox.showerror(
                "Erreur", "Vous devez remplir tout les champs")
        elif x == 0:
            Get_Data_config()
            Clear_page()
            Page_account()
        elif x == int(numberaccount_data):
            Get_Data_account()
            Read_json()
            if Json_API.Json_data == None:
             Json_API.Json_data = config_data
            else:
             Json_API.Json_data.update(config_data)
            Write_json()
            app_config_account.destroy()
        else:
            Get_Data_account()
            Page_account()

    Page_account()
    app_config_account.mainloop()
