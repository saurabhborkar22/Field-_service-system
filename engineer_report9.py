import tkinter as tk
from tkinter import ttk
from turtle import width
from tkcalendar import DateEntry 
import pymysql
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:214531@localhost/pythongui")
my_w = tk.Tk()
my_w.geometry("900x650")  # Size of the window 
my_w.title("Report") 
my_w.configure(bg="dark grey") # Adding a title
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='214531',
        db='pythongui',
    )
    return conn


font2=('Times',14,'bold')
Options =[]
query="SELECT distinct(ename) as ename FROM serviceorder"
conn = connection()
cursor = conn.cursor()
cursor.execute(query)
my_list = [r for r, in cursor]
sel1=tk.StringVar()
cb2 = ttk.Combobox(my_w, values=my_list,width=30,textvariable=sel1)
cb2.grid(row=0,column=0,sticky='nw',padx=20,pady=40)

query="SELECT distinct(status) as status FROM serviceorder"
conn = connection()
cursor = conn.cursor()
cursor.execute(query)
my_list = [r for r, in cursor]
sel=tk.StringVar()
cb2 = ttk.Combobox(my_w, values=my_list,width=30,textvariable=sel)
cb2.grid(row=0,column=0,sticky='ne',padx=20,pady=40)

def my_upd(*args): # triggered when value of string varaible changes
    query="select * from serviceorder WHERE ename='"+sel1.get()+"' and status='"+sel.get()+"'"
    r_set=my_conn.execute(query) # execute query with data
    for item in trv.get_children(): # delete all previous listings
        trv.delete(item)
        # to store total sale of the selected date
    for dt in r_set: 
        trv.insert("", 'end',iid=dt[0], text=dt[0],
           values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9]))

trv = ttk.Treeview(my_w, selectmode ='browse')
  
trv.grid(row=1,column=0,padx=20,pady=10)
# number of columns
trv["columns"] = ("1", "2", "3","4","5","6","7","8","9","10")
trv['height']  =20
# Defining heading
trv['show'] = 'headings'
  
# width of columns and alignment 
trv.column("1", width = 50, anchor ='c')
trv.column("2", width = 50, anchor ='c')
trv.column("3", width = 80, anchor ='c')
trv.column("4", width = 80, anchor ='c')
trv.column("5", width = 80, anchor ='c')
trv.column("6", width = 60, anchor ='c')
trv.column("7", width = 80, anchor ='c')
trv.column("8", width = 80, anchor ='c')
trv.column("9", width = 80, anchor ='c')
trv.column("10", width = 70, anchor ='c')

  
# Headings  
# respective columns
trv.heading("1", text ="s_id")
trv.heading("2", text ="cid")
trv.heading("3", text ="cname")
trv.heading("4", text ="number")  
trv.heading("5", text ="address")
trv.heading("6", text ="pin")
trv.heading("7", text ="product")
trv.heading("8", text ="ename")
trv.heading("9", text ="states")
trv.heading("10", text ="date")

sel.trace('w',my_upd)

l2=tk.Label(my_w,font=('Times',22,'bold'),text='Name',fg='red',bg="dark grey")
l2.place(x=30,y=4)
l3=tk.Label(my_w,font=('Times',22,'bold'),text='Status',fg='red',bg="dark grey")
l3.place(x=400,y=25)
my_w.mainloop()  # Keep the window open
