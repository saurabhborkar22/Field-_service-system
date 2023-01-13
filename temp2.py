import tkinter as tk
from tkinter import *
from tkinter import ttk
import pymysql
my_w = tk.Tk()
my_w.geometry("1000x600")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:214531@localhost/pythongui")
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='214531',
        db='pythongui',
    )
    return conn
Options =[]
query="select  id,name FROM engineer"
conn = connection()
cursor = conn.cursor()
cursor.execute(query)
ids=cursor.fetchall()
for i in ids:
    Options.append(str(i[0])+"-"+i[1])
sel1=tk.StringVar()
cb2 = ttk.Combobox(my_w, values=Options,width=30,textvariable=sel1)
cb2.grid(row=0,column=0,padx=20,pady=40)
def my_upd(*args):
    global trv
    month=sel.get() # Collecting the selected month name
    query="SELECT * FROM inventry WHERE DATE_FORMAT( date, '%%b' ) ='"+month+"' and engineer='"+cb2.get()+"'"
    lb.config(text=query) # display query 
    r_set=my_conn.execute(query)
    l1=[r for r in r_set.keys()] # List of column headers 
    r_set=[r for r in r_set] # Rows of data

    trv['height']=10 # Number of rows to display, default is 10
    trv['show'] = 'headings' 
    # column identifiers 
    trv["columns"] = l1
    print(l1)
    # Defining headings, other option in tree
    # width of columns and alignment 

    for i in l1:
        trv.column(i, width =80, anchor ='w',stretch=NO)
    # Headings of respective columns
    for i in l1:
        trv.heading(i, text =i)
		
    for item in trv.get_children(): # delete all rows 
        trv.delete(item)
		
    for dt in r_set:
        #print(dt)
        v=[r for r in dt] # collect the row data as list 
        trv.insert("",'end',iid=v[0],values=v)

sel=tk.StringVar() # string variable 

months=['Jan','Feb','Mar','Apr','May','Jun','Jul',
    'Aug','Sep','Oct','Nov','Dec']
cb1 = ttk.Combobox(my_w, values=months,width=7, textvariable=sel)
cb1.grid(row=0,column=1,padx=5,pady=20)

lb=tk.Label(my_w,text='Query',bg='yellow')
lb.grid(row=1,column=0,columnspan=3)
trv = ttk.Treeview(my_w, selectmode ='browse')
trv.grid(row=2,column=0,columnspan=3,padx=5,pady=20)

sel.trace('w',my_upd)


my_w.mainloop()