from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Pythonguides')
ws.geometry('400x300')
ws.config(bg='#04B2D9')

def validation():
    name = name_tf.get()
    msg = ''

    if len(name) == 0:
        msg = 'name can\'t be empty'
    else:
        try:
            if any(ch.isdigit() for ch in name):
                msg = 'Name can\'t have numbers'
            elif len(name) <= 2:
                msg = 'name is too short.'
            elif len(name) > 100:
                msg = 'name is too long.'
            else:
                msg = 'Success!'
        except Exception as ep:
            messagebox.showerror('error', ep)
        
    messagebox.showinfo('message', msg)
    
frame = Frame(
    ws,
    padx=10,
    pady=10
)
frame.pack(pady=20)

Label(
    frame,
    text='Enter Name'
).grid(row=0, column=1)

name_tf = Entry(
    frame,
    font = ('sans-sherif', 14)
)
name_tf.grid(row=0, column=1)

Button(
    frame,
    text='Submit',
    pady=10,
    padx=20,
    command=validation
).grid(row=1, columnspan=2)

ws.mainloop()