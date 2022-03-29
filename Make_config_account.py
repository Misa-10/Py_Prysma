# coding: utf-8

from tkinter import *
from pprint import pprint
import json
from tkinter.ttk import *

app = Tk()

# style of page
app.title("Création de configuration")
app.geometry("800x500")

Username_entry = None
passw_entry = None
nameconfig_entry= None
numberaccount_Combobox = None
config_data = None

account_Data_array = []
x=-1


         


def Page_account():
    global x ; global Username_entry ; global passw_entry ; global nameconfig_entry ; global numberaccount_Combobox
    x=x+1
    pprint(x)
    if x == 0:
         nameconfig_label = Label(app, text='Nom de configuration', font=('calibre', 15, 'bold'))
         nameconfig_label.grid(row=0, column=0, ipady=5, pady=10)

         nameconfig_entry = Entry(app, font=('calibre', 15, 'normal'))
         nameconfig_entry.grid(row=1, column=0, ipady=5, pady=10)
         
         numberaccount_label = Label(app, text='Nombre de compte', font=('calibre', 15, 'bold'))
         numberaccount_label.grid(row=2, column=0, ipady=5, pady=10)
         
         numberaccount_Combobox = Combobox(app,values=["1","2","3","4","5","6","7","8"], font=('calibre', 15, 'bold'))
         numberaccount_Combobox.grid(row=3, column=0, ipady=2, pady=10)
         
         sub_btn = Button(app, text='Suivant',command =lambda:[Get_Data_config(),Clear_page(),Page_account()])
         sub_btn.grid(row=4, column=1, ipady=5, pady=10)
         
         
    elif x == 8:
            Save_btn = Button(app, text='Sauvegarder',command =lambda:[Read_json()])
            Save_btn.grid(row=3, column=2, ipady=5, pady=10)
    else:  
            
        # creating a label for
        # name using widget Label
        Account_label = Label(app, text='Compte '+str(x), font=('calibre', 15, 'bold'))

        #
        # creating a label for
        # name using widget Label
        Username_label = Label(app, text='Username', font=('calibre', 15, 'bold'))

        # creating a entry for input
        # name using widget Entry
        Username_entry = Entry(app, font=('calibre', 15, 'normal'))

        # creating a label for password
        passw_label = Label(app, text='Password', font=('calibre', 15, 'bold'))

        # creating a entry for password
        passw_entry = Entry(app, font=('calibre', 15, 'normal'))

        # creating a button using the widget
        # Button that will call the submit function

        # placing the label and entry in
        # the required position using grid
        # method
        Account_label.grid(row=0, column=3, ipady=5, pady=10)
        Username_label.grid(row=1, column=1, ipady=5, pady=10)
        Username_entry.grid(row=1, column=2, ipady=5, pady=10)
        passw_label.grid(row=2, column=1, ipady=5, pady=10)
        passw_entry.grid(row=2, column=2, ipady=5, pady=10)

        sub_btn = Button(app, text='Suivant',command =lambda:[Get_Data_account(),Page_account()])
        sub_btn.grid(row=3, column=2, ipady=5, pady=10)

def Get_Data_account():
        
      Username_data =  Username_entry.get()
      passw_data =  passw_entry.get()

      account_data = {
              "username":Username_data,
              "passw":passw_data}
      account_Data_array.append(account_data)

      with open('json_data.json', 'w') as outfile:
       json.dump({config_data["nameconfig"]: account_Data_array}, outfile)
       
def Get_Data_config():
      global config_data
        
      nameconfig_data =  nameconfig_entry.get()
      numberaccount_data =  numberaccount_Combobox.get()

      config_data = {
              "nameconfig":nameconfig_data,
              "numberaccount":numberaccount_data}
        
      pprint(config_data)
      
def Clear_page():
        for child in app.winfo_children():
                child.destroy()
      
def Read_json():
         with open('json_data.json', 'r') as readfile:
          test = json.load(readfile)
          pprint(test)
        
Page_account()
app.mainloop()
