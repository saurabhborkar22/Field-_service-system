
from tkinter import *
from tkinter.font import BOLD
from PIL import ImageTk
from subprocess import call
ws = Tk()
ws.geometry("1366x700+0+0")
ws.title('RELIANCE SYSTEM')
ws['bg']='#FF8000'

f = ("Times bold", 14)

menubar = Menu(ws)
#image
ws.img=ImageTk.PhotoImage(file="images/img1.JPG")
img=Label(image=ws.img).place(x=100,y=50,width=400,height=300)


# Adding File Menu and commands

def nextPage():
    ws.destroy()
    call(['python' , 'adminlogin2.py'])

def prevPage():
    ws.destroy()
    call(['python' , 'userlogin1.py'])

def close():
    ws.destroy()

Label(
    ws,
    text="RELIANCE FIELD SERVICE SYSTEM",
    padx=100,
    pady=200,
    bg='#FF8000',
    font=BOLD
).pack(expand=True, fill=BOTH)

file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='LOGIN', menu = file)
file.add_command(label ='ADMIN LOGIN', command = nextPage)
file.add_command(label ='USER LOGIN', command = prevPage)


Button(
    ws, 
    text="CLOSE", 
    font=f,
    command = close
    ).pack(fill=X, expand=TRUE, side=LEFT)


ws.config(menu = menubar)
ws.mainloop()