from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pyautogui
from pyautogui import *

Timer = Tk()

# style of page
Timer.title("Main")
Timer.geometry("300x100")
Timer.attributes('-topmost',True)

for i in range(10, 0, -1):
     time.sleep(1)
     Timer_label = Label(
                Timer, text="Recupération de la couleur dans "+str(i)+"\nPlacer votre souris sur l'élement", font=('calibre', 15, 'bold')).grid(row=0, column=0, ipady=5, pady=10)
     Timer.update()

Timer.mainloop()