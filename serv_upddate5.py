from itertools import product
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry 
from time import strftime
from tkinter import filedialog, messagebox, ttk
import pymysql
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:214531@localhost/pythongui")
#my_conn = create_engine("sqlite:///D:\\testing\\sqlite\\my_db.db")
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='214531',
        db='pythongui',)
    return conn

my_w = tk.Tk()
my_w.geometry("950x700")  # Size of the window 
my_w.title("Update")  # Adding a title
sel=tk.StringVar()
cal=DateEntry(my_w,selectmode='day',textvariable=sel)
cal.place(x=270,y=100)
l2=tk.Label(my_w,font=('Times',22,'bold'),text='Date',fg='red')
l2.place(x=270,y=50)
frame2 = tk.LabelFrame(my_w, text="Excel Data")
frame2.place(height=200, width=850, x=10, y=450)

ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()
ph7 = tk.StringVar()
ph8 = tk.StringVar()
ph9 = tk.StringVar()
ph10 = tk.StringVar()

def refreshTable():
    for data in trv.get_children():
        trv.delete(data)

    for array in read():
        trv.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    trv.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    


trv = ttk.Treeview(frame2)
trv.place(relheight=1, relwidth=1)      
treescrolly = tk.Scrollbar(frame2, orient="vertical", command=trv.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame2, orient="horizontal", command=trv.xview) # command means update the xaxis view of the widget
trv.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widge
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

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
    if num ==6:
        ph6.set(word)
    if num ==7:
        ph7.set(word)
    if num ==8:
        ph8.set(word)
    if num ==9:
        ph9.set(word)
    if num ==10:
        ph10.set(word)

        


query="SELECT distinct(name) as name FROM engineer"
conn = connection()
cursor = conn.cursor()
cursor.execute(query)
my_list = [r for r, in cursor]
sel1=tk.StringVar()
cb2 = ttk.Combobox(my_w, values=my_list,width=30,textvariable=sel1)
cb2.place(x=30,y=100)
l2=tk.Label(my_w,font=('Times',22,'bold'),text='Engineer',fg='red')
l2.place(x=30,y=50)
def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("select * FROM serviceorder")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results
def my_upd(*args):
     # triggered when value of string varaible changes
    if(len(sel.get())>4):
        dt=cal.get_date() # get selected date object from calendar
        dt1=dt.strftime("%Y-%m-%d") #format for MySQL date column 
        dt2=dt.strftime("%d-%B-%Y") #format to display at label 
         # display date at Label
        query="select * from serviceorder WHERE date=%s and ename='"+sel1.get()+"'"
        r_set=my_conn.execute(query,dt1) # execute query with data
        for item in trv.get_children(): # delete all previous listings
            trv.delete(item)
        # to store total sale of the selected date
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5],dt[6],dt[7],dt[8],dt[9]))





            
def select():
    
    try:
        selected_item = trv.selection()[0]
        s_id = str(trv.item(selected_item)['values'][0])
        cid = str(trv.item(selected_item)['values'][1])
        cname = str(trv.item(selected_item)['values'][2])
        number = str(trv.item(selected_item)['values'][3])
        address = str(trv.item(selected_item)['values'][4])
        pin = str(trv.item(selected_item)['values'][5])
        product = str(trv.item(selected_item)['values'][6])
        ename = str(trv.item(selected_item)['values'][7])
        status = str(trv.item(selected_item)['values'][8])
        date = str(trv.item(selected_item)['values'][9])
        
        
        setph(s_id,1)
        setph(cid,2)
        setph(cname,3)
        setph(number,4)
        setph(address,5)
        setph(pin,6)
        setph(product,7)
        setph(ename,8)
        setph(status,9)
        setph(date,10)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def update():
    selectedStudid = ""

    try:
        selected_item = trv.selection()[0]
        selectedStudid = str(trv.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    s_id = str(s_idEntry.get())
    cid = str(cidEntry.get())
    cname = str(cnameEntry.get())
    number = str(numberEntry.get())
    address = str(addressEntry.get())
    pin = str(pinEntry.get())
    product = str(productEntry.get())
    ename = str(enameEntry.get())
    status = str(statusEntry.get())
    date = str(dateEntry.get())
    if (s_id == "" or s_id == " ") or (cid == "" or cid == " ") or (cname == "" or cname == " ") or (number == "" or number == " ") or (address == "" or address== " ")or (pin == "" or pin == " ")or (product == "" or product == " ")or (ename == "" or ename == " ")or (status == "" or status == " ")or (date == "" or date == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("update serviceorder SET s_id='"+
            s_id+"', cid='"+
            cid+"', cname='"+
            cname+"', number='"+
            number+"', address='"+
            address+"', pin='"+
            pin+"', ename='"+
            ename+"', status='"+
            status+"', date='"+
            date+"'  WHERE s_id='"+
            selectedStudid+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", " ID already exist")
            return

    refreshTable()

s_idLabel = Label(my_w, text="S_ID", font=('Arial', 15))
cidLabel = Label(my_w, text="C_ID", font=('Arial', 15))
cnameLabel = Label(my_w, text="C_Name", font=('Arial', 15))
numberLabel = Label(my_w, text="Number", font=('Arial', 15))
addressLabel = Label(my_w, text="Address", font=('Arial', 15))
pinLabel = Label(my_w, text="PIN Code", font=('Arial', 15))
productLabel = Label(my_w, text="Product", font=('Arial', 15))
enameLabel = Label(my_w, text="Eanme", font=('Arial', 15))
statusLabel = Label(my_w, text="Status", font=('Arial', 15))
dateLabel = Label(my_w, text="date", font=('Arial', 15))

s_idLabel.place(x=50, y=170)
cidLabel.place(x=50, y=210)
cnameLabel.place(x=50, y=250)
numberLabel.place(x=50, y=290)
addressLabel.place(x=50, y=330)
pinLabel.place(x=450, y=170)
productLabel.place(x=450, y=210)
enameLabel.place(x=450, y=250)
statusLabel.place(x=450, y=290)
dateLabel.place(x=450, y=330)

s_idEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph1)
cidEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph2)
cnameEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph3)
numberEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph4)
addressEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph5)
pinEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph6)
productEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph7)
enameEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph8)
statusEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph9)
dateEntry = Entry(my_w, width=25, bd=5, font=('Arial', 15), textvariable = ph10)

s_idEntry.place(x=150, y=170)
cidEntry.place(x=150, y=210)
cnameEntry.place(x=150, y=250)
numberEntry.place(x=150, y=290)
addressEntry.place(x=150, y=330)
pinEntry.place(x=550, y=170)
productEntry.place(x=550, y=210)
enameEntry.place(x=550, y=250)
statusEntry.place(x=550, y=290)
dateEntry.place(x=550, y=330)

selectBtn = Button(
    my_w, text="Select", padx=15, pady=10, width=10,
    bd=5, font=('Arial', 15), bg="#EEEEEE", command=select)
selectBtn.place(x=100,y=375)

updateBtn = Button(
    my_w, text="Update", padx=15, pady=10, width=10,
    bd=5, font=('Arial', 15), bg="#84E8F8", command=update)
updateBtn.place(x=250,y=375)
#################################################


trv["columns"] = ("1", "2", "3","4","5","6","7","8","9","10")
trv['height']  =20
# Defining heading
trv['show'] = 'headings'
  
# width of columns and alignment 
trv.column("1", width = 30, anchor ='c')
trv.column("2", width = 30, anchor ='c')
trv.column("3", width = 30, anchor ='c')
trv.column("4", width = 30, anchor ='c')
trv.column("5", width = 30, anchor ='c')
trv.column("6", width = 30, anchor ='c')
trv.column("7", width = 30, anchor ='c')
trv.column("8", width = 30, anchor ='c')
trv.column("9", width = 30, anchor ='c')
trv.column("10", width = 30, anchor ='c')

  
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

l2=tk.Label(my_w,font=('Times',22,'bold'),fg='red')
l2.grid(row=1,column=2,sticky='ne',pady=20)



my_w.mainloop()  # Keep the window open
