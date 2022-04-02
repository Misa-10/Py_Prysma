# Importing Tkinter module
from tkinter import *
import Json_API
from Json_API import *
# from tkinter.ttk import *

# Creating master Tkinter window
master = Tk()
master.geometry("175x300")
config_accoun_btn = Button(
    master, text='Créer une configuration comptes', command=lambda: [test()]).pack(ipady = 5)

Read_json()
# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
def generate():
    for x in Json_API.Json_data.keys():
	    Radiobutton(master, text = x, variable = v,
				value = x).pack(ipady = 5)




# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())

def test():
    print(v.get())
generate()
mainloop()
