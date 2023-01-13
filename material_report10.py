import tkinter as tk
from tkinter import END, ttk
from turtle import width
from tkcalendar import DateEntry 
import pymysql
import os
import tempfile
from time import strftime
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
def my_time():
    time_string = strftime('%Y-%m-%d') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',20,'bold') # display size and style

l1=tk.Label(my_w,font=my_font,bg='yellow')
l1.grid(row=0,column=2,padx=20,pady=40)

my_time()
l3=tk.Label(my_w,font=my_font,text='Engineer')
l3.place(x=50,y=10)
l4=tk.Label(my_w,font=my_font,text='Monath')
l4.place(x=400,y=10)
sel=tk.StringVar()
def my_upd(*args): # triggered when value of string varaible changes
        month=sel.get()
        query="SELECT * FROM inventry WHERE \
        DATE_FORMAT( date, '%%b' ) ='"+month+"' AND engineer='"+cb2.get()+"'"
        r_set=my_conn.execute(query) # execute query with data
        for item in trv.get_children(): # delete all previous listings
            trv.delete(item)
        total=0 # to store total sale of the selected date
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[1],dt[2],dt[3],dt[4],dt[5],dt[6]))
            total=round(total+(dt[3]*dt[4]),2)
        l2.config(text="Total: " + str(total)) # show total value
months=['Jan','Feb','Mar','Apr','May','Jun','Jul',
    'Aug','Sep','Oct','Nov','Dec']
cb1 = ttk.Combobox(my_w, values=months,width=20, textvariable=sel)
cb1.grid(row=0,column=1,padx=5,pady=20)


trv = ttk.Treeview(my_w, selectmode ='browse')
  
trv.grid(row=1,column=1,padx=20,pady=10)
# number of columns
trv["columns"] = ("1", "2", "3","4","5","6")
trv['height']  =20
# Defining heading
trv['show'] = 'headings'
  
# width of columns and alignment 
trv.column("1", width = 30, anchor ='c')
trv.column("2", width = 80, anchor ='c')
trv.column("3", width = 80, anchor ='c')
trv.column("4", width = 80, anchor ='c')
trv.column("5", width = 80, anchor ='c')
trv.column("6", width = 80, anchor ='c')
  
# Headings  
# respective columns

trv.heading("1", text ="engineer")
trv.heading("2", text ="mname")
trv.heading("3", text ="qnt")  
trv.heading("4", text ="price")
trv.heading("5", text ="total")
trv.heading("6", text ="date")
sel.trace('w',my_upd)

l2=tk.Label(my_w,font=('Times',22,'bold'),fg='red')
l2.grid(row=2,column=1,sticky='nw',pady=20)


#b1=tk.Button(my_w,text='monthly collection',font=('Times',22,'bold'),command=next)
#b1.grid(row=0,column=2)
my_w.mainloop()  # Keep the window open
