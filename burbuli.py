#mērķis ir uztaisīt programmu, kurā zemūdene spridzina burbuļus
#tiek skaitīti punkti
from tkinter import *
from random import *
from math import *
logs = Tk()
garums = 700
platums = 700
logs.title("Burbuļu spridzinātājs")
a = Canvas(logs, width=platums, height=garums, bg='lightpink')
a.pack()
kuga_id2 = a.create_oval(0,0,100,100,outline='purple', width=10)
















mainloop()