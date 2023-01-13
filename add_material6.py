import tkinter as tk
from tkinter import *
from tkinter import ttk

from tkinter import messagebox
from sqlalchemy.exc import SQLAlchemyError
import pymysql
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

def refreshTable():
    for data in trv.get_children():
        trv.delete(data)

    for array in read():
        trv.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    trv.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    trv.grid(row=0,column=0,columnspan=2,padx=3,pady=2)



my_w = tk.Tk()
my_w.geometry("800x750+10+7") 

frame1=tk.Frame(my_w,bg='white')
frame1.grid(row=8,column=1)
trv = ttk.Treeview(frame1,selectmode ='browse')
trv.grid(row=0,column=0,columnspan=2,padx=3,pady=2)
name=tk.StringVar()
qut=tk.StringVar()
price=tk.StringVar()
id=tk.StringVar()
    
def setph(word,num):
    if num ==1:
        id.set(word)
    if num ==2:
        name.set(word)
    if num ==3:
        qut.set(word)
    if num ==4:
        price.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * FROM material ORDER BY ID DESC")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results
def add():
    id = str(idEntry.get())
    name = str(nameEntry.get())
    qut = str(qutEntry.get())
    price = str(priceEntry.get())
    

    if (id == "" or id == " ") or (name == "" or name == " ") or (qut == "" or qut == " ") or (price == "" or price == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("insert INTo material VALUES ('"+id+"','"+name+"','"+qut+"','"+price+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "ID already exist")
            return

    refreshTable()

def data_collect(self): # collect data to display for edit
    selected=trv.focus() # gets the product id or p_id
    if(selected != None ):
        query="SELECT * from material WHERE id=%s"
        row=my_conn.execute(query,selected)
        s = row.fetchone() # row details as tuple
        if(s != None):
            id.set(s[0])
            name.set(s[1])
            qut.set(s[2])
            price.set(s[3]) # set the category value
            
            b_update.config(state='normal')
            b_update.config(command=lambda:my_update(selected))
    else:
        b_update.config(state='disabled')
def my_update(p_id): # receives the p_id on button click to update
    
        data=(id.get(),name.get(),qut.get(),price.get())
        id=my_conn.execute("update material SET id=%s,name=%s,\
            qut=%s,price=%s WHERE id=%s",data)    
        #print(data)
    
refreshTable()
def update():
    selectedid = ""

    try:
        selected_item = trv.selection()[0]
        selectedid = str(trv.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    id = str(idEntry.get())
    name = str(nameEntry.get())
    qnt = str(qutEntry.get())
    price = str(priceEntry.get())
    

    if (id == "" or id == " ") or (name == "" or name == " ") or (qnt == "" or qnt == " ") or (price == "" or price == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:            
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("update material SET id='"+
            id+"', name='"+
            name+"', qnt='"+
            qnt+"', price='"+
            price+"' WHERE id='"+
            selectedid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", " ID already exist")
            return

    refreshTable()
def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = trv.selection()[0]
        deleteData = str(trv.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("delete FROM material WHERE id='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

idLabel = Label(my_w, text="ID", font=('Arial', 15))
nameLabel = Label(my_w, text="name", font=('Arial', 15))
qutLabel = Label(my_w, text="Quintity", font=('Arial', 15))
priceLabel = Label(my_w, text="Price", font=('Arial', 15))

idLabel.grid(row=3, column=0)
nameLabel.grid(row=4, column=0)
qutLabel.grid(row=5, column=0)
priceLabel.grid(row=6, column=0)

idEntry = Entry(my_w, width=55, bd=5, font=('Arial', 15),textvariable = id)
nameEntry = Entry(my_w, width=55, bd=5, font=('Arial', 15), textvariable = name)
qutEntry = Entry(my_w, width=55, bd=5, font=('Arial', 15), textvariable = qut)
priceEntry = Entry(my_w, width=55, bd=5, font=('Arial', 15), textvariable = price)

idEntry.grid(row=3, column=1, padx=5, pady=0)
nameEntry.grid(row=4, column=1, padx=5, pady=0)
qutEntry.grid(row=5, column=1, padx=5, pady=0)
priceEntry.grid(row=6, column=1,padx=5, pady=0)

b_update=tk.Button(my_w,text='Add',command=add)
b_update.grid(row=7,column=0)
# Layout is over , placing components 
update=tk.Button(my_w,text='Update',command=update)
update.grid(row=7,column=1)

deletebt=tk.Button(my_w,text='Delete',command=delete)
deletebt.grid(row=7,column=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))
# column identifiers 
trv['columns'] = ("id", "name","qut","price")
trv.column("#0", width=0, stretch=NO)
trv.column("id", width = 80) # p_id
trv.column("name", width = 80) # p_name
trv.column("qut", width =80 ) # unit
trv.column("price", width = 80) # price
 
  
# Headings  
# respective columns
trv.heading("id", text ="id")
trv.heading("name", text ="name")
trv.heading("qut", text ="qut")
trv.heading("price", text ="Price")

refreshTable()
#path_image="G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\"
#img_top = tk.PhotoImage(file = path_image+"restaurant-3.png")
#img_l1 = tk.Label(frame_top,  image=img_top)
#img_l1.grid(row=0,column=0,sticky='nw',pady=1)

#Right side layout to display product details for Edit 

trv.bind("<<TreeviewSelect>>", data_collect) 

 

my_w.mainloop()