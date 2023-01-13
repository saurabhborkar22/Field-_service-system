#pip install PyMySQL
from distutils.cmd import Command
import email
from unicodedata import category
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import re
#connection for phpmyadmin
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='214531',
        db='pythongui',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("Engineer")
root.geometry("1250x720+70+30")
my_tree = ttk.Treeview(root)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * FROM engineer")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    id = str(idEntry.get())
    name = str(nameEntry.get())
    email = str(emailEntry.get())
    phone = str(phoneEntry.get())
    area = str(areaEntry.get())
    category = str(sel.get())
    name = nameEntry.get()
    msg = ''
    num=phoneEntry.get()
    em=emailEntry.get()
    if len(name) == 0:
        messagebox.showerror('name can\'t be empty')
        return
    else:
        try:
            if any(ch.isdigit() for ch in name):
                messagebox.showerror('Name can\'t have numbers')
                return
            elif len(name) <= 2:
                msg = 'name is too short.'
                return
            elif len(name) > 100:
                msg = 'name is too long.'   
                return
            
        except Exception as ep:
            messagebox.showerror('error', ep)
        
    messagebox.showinfo('message', msg)
    if len(num)==0:
        msg='number cant be empty'
    
    val = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if len(em)==0:
        msg='number cant be empty'
    else:
        try:
            r=re.fullmatch(val,em)
            if r!=None: # checking whether it is none or not 
                msg='Valid email'
            else:
                messagebox.showerror('check email')
                return
        except Exception as ep:
            messagebox.showerror('error', ep)
            return
    if len(num)==0:
        msg='number cant be empty'
    else:
        try:
            r=re.fullmatch('[6-9][0-9]{9}',num)
            if r!=None: # checking whether it is none or not 
                msg='Valid number'
            else:
                messagebox.showerror('check num')
                return
        except Exception as ep:
            messagebox.showerror('error', ep)
            return
    

    if  (name == "" or name == " ") or (email == "" or email == " ") or (phone == "" or phone == " ") or (area == "" or area == " ")or (category == "" or category == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("insert INTO engineer(name,email,phone,area,category) VALUES ('"+name+"','"+email+"','"+phone+"','"+area+"','"+category+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "ID already exist")
            return

    refreshTable()
    

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("delete FROM engineer")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("delete FROM engineer WHERE id='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        id = str(my_tree.item(selected_item)['values'][0])
        name = str(my_tree.item(selected_item)['values'][1])
        email = str(my_tree.item(selected_item)['values'][2])
        phone = str(my_tree.item(selected_item)['values'][3])
        area = str(my_tree.item(selected_item)['values'][4])
        category = str(my_tree.item(selected_item)['values'][5])
        
        setph(id,1)
        setph(name,2)
        setph(email,3)
        setph(phone,4)
        setph(area,5)
        setph(category,6)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    id = str(idEntry.get())
    name = str(nameEntry.get())
    email = str(emailEntry.get())
    phone = str(phoneEntry.get())
    area = str(areaEntry.get())
    category = str(sel.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * FROM engineer WHERE id='"+
    id+"' or name='"+
    name+"' or email='"+
    email+"' or phone='"+
    phone+"' or area='"+
    area+"' or category='"+
    category+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedStudid = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedStudid = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    id = str(idEntry.get())
    name = str(nameEntry.get())
    email = str(emailEntry.get())
    phone = str(phoneEntry.get())
    area = str(areaEntry.get())
    category = str(sel.get())

    if (id == "" or id == " ") or (name == "" or name == " ") or (email == "" or email == " ") or (phone == "" or phone == " ") or (area == "" or area == " ")or (category == "" or category == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("update engineer SET id='"+
            id+"', name='"+
            name+"', email='"+
            email+"', phone='"+
            phone+"', area='"+
            area+"', category='"+
            category+"' WHERE id='"+
            selectedStudid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()

label = Label(root, text="ENFINEER REGISTRATION", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

idLabel = Label(root, text="E ID", font=('Arial', 15))
nameLabel = Label(root, text="name", font=('Arial', 15))
emailLabel = Label(root, text="email", font=('Arial', 15))
phoneLabel = Label(root, text="phone", font=('Arial', 15))
areaLabel = Label(root, text="area", font=('Arial', 15))
categoryLabel = Label(root, text="category", font=('Arial', 15))

idLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
nameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
emailLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
phoneLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
areaLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)
categoryLabel.grid(row=8, column=0, columnspan=1, padx=50, pady=5)




idEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
nameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
emailEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
phoneEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
areaEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

idEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
nameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
emailEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
phoneEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
areaEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

def validation():
    name = ph2.get()
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

my_list2=[] 
query="SELECT distinct(category) as category FROM engineer"
conn = connection()
cursor = conn.cursor()
cursor.execute(query)
my_list = [r for r, in cursor]
sel=tk.StringVar()
cb2 = ttk.Combobox(root, values=my_list,width=45,textvariable=sel)
cb2.place(x=400,y=390)




addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84F894", command=add)
updateBtn = Button(
    root, text="Update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#FF9999", command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F4FE82", command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#F398FF", command=reset)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("id","name","email","phone","area","category")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("id", anchor=W, width=80)
my_tree.column("name", anchor=W, width=120)
my_tree.column("email", anchor=W, width=120)
my_tree.column("phone", anchor=W, width=120)
my_tree.column("area", anchor=W, width=120)
my_tree.column("category", anchor=W, width=120)

my_tree.heading("id", text="ID", anchor=W)
my_tree.heading("name", text="Name", anchor=W)
my_tree.heading("email", text="Email", anchor=W)
my_tree.heading("phone", text="Phone", anchor=W)
my_tree.heading("area", text="Area", anchor=W)
my_tree.heading("category", text="Category", anchor=W)

refreshTable()

root.mainloop()