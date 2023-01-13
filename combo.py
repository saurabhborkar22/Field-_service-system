from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:214531@localhost/pythongui")
#my_conn = create_engine("sqlite:///D:\\testing\\sqlite\\my_db.db")
query="SELECT distinct(category) as category FROM engineer"
                
my_data=my_conn.execute(query) # SQLAlchem engine result
my_list = [r for r, in my_data] # create a  list 
import tkinter as tk
from tkinter import ttk
my_w = tk.Tk()
my_w.geometry("600x150")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
my_list2=[]  
my_list3=[]
def my_upd(*args):
    cb2.set('') # remove the previous selected option 
    query="select name FROM engineer WHERE category='"+sel.get()+"'"
    my_data=my_conn.execute(query) # SQLAlchem engine result
    my_list2 = [r for r, in my_data] # create a  list 
    cb2['values']=my_list2
sel=tk.StringVar()
def my_up(*args):
    cb3.set('') # remove the previous selected option 
    query="select area FROM engineer WHERE name='"+sel1.get()+"'"
    my_data=my_conn.execute(query) # SQLAlchem engine result
    my_list3 = [r for r, in my_data] # create a  list 
    cb3['values']=my_list3
 
sel1=tk.StringVar()


cb1 = ttk.Combobox(my_w, values=my_list,width=15,textvariable=sel)
cb1.grid(row=1,column=1,padx=30,pady=30)

sel.trace('w',my_upd) # track the change event 

cb2 = ttk.Combobox(my_w, values=my_list2,width=15,textvariable=sel1)
cb2.grid(row=1,column=2)

cb3 = ttk.Combobox(my_w, values=my_list3,width=15)
cb3.grid(row=1,column=3)
sel1.trace('w',my_up)
my_w.mainloop()  # Keep t