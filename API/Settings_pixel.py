from tkinter import *
from pprint import pprint
from tkinter.ttk import *
from API.GetPixel_API import *
from API.Timer import *

def Launch_Settings_Pixel(string):
    app_settings_pixel = Toplevel(string)

    # style of page
    app_settings_pixel.title("Création de configuration")
    app_settings_pixel.geometry("800x500")
    
    BtnJouer_btn = Button(
    app_settings_pixel, text='Bouton Jouer', command=lambda: [Timer_app(app_settings_pixel),GetBtnJouer()]).grid(row=0, column=0, ipady=5, pady=10)
    
    Serv1_btn = Button(
    app_settings_pixel, text='Serveur 1', command=lambda: []).grid(row=1, column=0, ipady=5, pady=10)
    
    Serv2_btn = Button(
    app_settings_pixel, text='Serveur 2', command=lambda: []).grid(row=2, column=0, ipady=5, pady=10)
    
    Serv3_btn = Button(
    app_settings_pixel, text='Serveur 3', command=lambda: []).grid(row=3, column=0, ipady=5, pady=10)
    
    Serv4_btn = Button(
    app_settings_pixel, text='Serveur 4', command=lambda: []).grid(row=4, column=0, ipady=5, pady=10)
    
    Serv5_btn = Button(
    app_settings_pixel, text='Serveur 5', command=lambda: []).grid(row=5, column=0, ipady=5, pady=10)
    
    Pers1_btn = Button(
    app_settings_pixel, text='Personnage 1', command=lambda: []).grid(row=0, column=1, ipady=5, pady=10)
    
    Pers2_btn = Button(
    app_settings_pixel, text='Personnage 2', command=lambda: []).grid(row=1, column=1, ipady=5, pady=10)
    
    Pers3_btn = Button(
    app_settings_pixel, text='Personnage 3', command=lambda: []).grid(row=2, column=1, ipady=5, pady=10)
    
    Pers4_btn = Button(
    app_settings_pixel, text='Personnage 4', command=lambda: []).grid(row=3, column=1, ipady=5, pady=10)
    
    Pers5_btn = Button(
    app_settings_pixel, text='Personnage 5', command=lambda: []).grid(row=4, column=1, ipady=5, pady=10)


