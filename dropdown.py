import tkinter as tkr


N1 = [1,2,3]
N2 =  [3,4,5]
N3 = [5,6,7]
N4 = ["success"]

master = tkr.Tk()
master.geometry("200x100")
master.title("dropdown list")


tkr.Label(master,text="basic dropdown list").grid(row=0)

var=tkr.StringVar()

set1 = tkr.OptionMenu(master,var,N1,N2,N3,N4)
set1.configure(font=("arial",25))
set1.grid(row=1,column=0)

tkr.mainloop()