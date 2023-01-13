from cProfile import label
from tkinter import*
import tkinter
from PIL import ImageTk
from PIL import Image
from subprocess import call

from tkinter.font import BOLD
import tkinter as tk
master=tkinter.Tk()
master.title("Field service system")
master.geometry("550x500+250+50") 
master.configure(bg="gray")
master.bg=ImageTk.PhotoImage(file="images/logo.jpg")
master.bg_image=Label(master,image=master.bg).place(x=0,y=0,relwidth=1,relheight=1)
menubar = Menu(master)

def nextPage():
    master.destroy()
    call(['python' , 'adminlogin2.py'])

def prevPage():
    master.destroy()
    call(['python' , 'userlogin1.py'])

def close():
    master.destroy()



file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='LOGIN', menu = file)
file.add_command(label ='ADMIN LOGIN', command = nextPage)
file.add_command(label ='USER LOGIN', command = prevPage)

label9=tkinter.Label(master,text="Reliance Field Service System",font=('impact',19,'bold'))
label9.place(x=110,y=390)
Button(
    master, 
    text="CLOSE", 
    
    command = close
    ).pack(side="bottom", fill="x")


master.config(menu = menubar)



master.mainloop()