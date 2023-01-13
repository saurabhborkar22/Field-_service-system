import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import BOTH, END, LEFT
from sqlalchemy import create_engine
import pymysql
from  datetime import date
my_conn = create_engine("mysql+mysqldb://root:214531@localhost/pythongui")
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='214531',
        db='pythongui',
    )
    return conn
font1=('Times',14,'normal')
font2=('Times',32,'bold')
sb=[]
my_w = tk.Tk()
my_w.geometry("700x500") 

frame_m_left=tk.Frame(my_w,bg='#284474')

#placing in grid

frame_m_left.grid(row=1,column=0,sticky='WENS')
trv = ttk.Treeview(frame_m_left, selectmode ='browse')
trv.grid(row=6,column=0,columnspan=1,padx=3,pady=2)
        
# column identifiers 
trv["columns"] = ("1", "2","3","4","5")
trv.column("#0", width = 0, stretch=NO)
trv.column("1", width = 50, anchor ='w')
trv.column("2", width =50 , anchor ='w')
trv.column("3", width = 50, anchor ='w')
trv.column("4", width = 50, anchor ='w')
trv.column("5", width = 50, anchor ='w')
# Headings  
# respective columns

trv.heading("1", text ="engineer",anchor='w')
trv.heading("2", text ="mname",anchor='w')
trv.heading("3", text ="qty",anchor='w')
trv.heading("4", text ="price",anchor='w')
trv.heading("5", text ="Total",anchor='w')
def my_reset():
    for item in trv.get_children(): # loop all child items 
        trv.delete(item)        # delete them 
    my_sum() # call the re-calculate and update the labels text
# Layout is over , sart placing buttons 
#path_image="G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\"
#img_top = tk.PhotoImage(file = path_image+"restaurant-3.png")
#bg=tk.PhotoImage(file=path_image+'bg2.png')

#img_l1 = tk.Label(frame_top,  image=img_top)
#img_l1.grid(row=0,column=0,sticky='nw',pady=1)

sel=tk.StringVar() # string variable for the Combobox
cb1=ttk.Combobox(frame_m_left,width=15,textvariable=sel,font=font2)
cb1.grid(row=0,column=0,padx=10, pady=20) 
cb1['values']
Options =[]
query= "select id,name from engineer"
conn = connection()
cursor = conn.cursor()
cursor.execute(query) 
ids=cursor.fetchall()
for i in ids:
    Options.append(str(i[0])+"-"+i[1])

sel1=tk.StringVar()
pr=tk.StringVar()
to=tk.StringVar()
el1=tk.StringVar()
cb2 = ttk.Combobox(frame_m_left,width=20,textvariable=sel1,font=font2)
cb2['values']= Options
cb2.grid(row=1,column=0,padx=10, pady=20)
cb2.current(0)

e1=tk.Entry(frame_m_left,width=4,font=font2,textvariable=el1)   
e1.grid(row=0,column=1)

priceLabel = Label(frame_m_left, text="ID", font=('Arial', 15))
totalLabel = Label(frame_m_left, text="name", font=('Arial', 15))
priceLabel.place(x=450,y=180)
totalLabel.place(x=450,y=260)
priceEntry = Entry(frame_m_left, width=15, bd=2, font=('Arial', 15),textvariable = pr)
totalEntry = Entry(frame_m_left, width=15, bd=2, font=('Arial', 15), textvariable = to)
priceEntry.place(x=450,y=220)
totalEntry.place(x=450,y=300)


def my_sum(): # Calculate total and tax part 
    total=0
    for line in trv.get_children(): # Loop through all items
        total=total+float(trv.item(line)['values'][3])
    tax=round(0.1*total,2)   # change the tax rate here 
    final=round(total+tax,2) # final price 
    #show it at Label 


def add():
    eng = str(cb2.get())
    mname = str(cb1.get())
    qnt = str(e1.get())
    price = str(priceEntry.get())
    total = str(totalEntry.get())
    dt=date.today().strftime('%Y-%m-%d')

    if (eng == "" or eng == " ") or (mname == "" or mname == " ") or (qnt == "" or qnt == " ") or (price == "" or price == " ")or (total == "" or total == " ")or (dt == "" or dt == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
      
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("insert INTo inventry(engineer,mname,qnt,price,total,date) VALUES ('"+eng+"','"+mname+"','"+qnt+"','"+price+"','"+total+"','"+dt+"') ")
            cursor1 = conn.cursor()
            cursor1.execute("update material set qnt=qnt-("+e1.get()+") where name='"+cb1.get()+"'")
            conn.commit()
            messagebox.showinfo(" ","entry added")
            messagebox.showinfo(" ","material update")    
        
            return
    
       #print(total, tax)
    
def my_add(): #adding item to bill 
    try:
        
        eng=sel1.get()
        p_name=my_menu2[sel.get()][1]
        quantity=e1.get()
        price=my_menu2[sel.get()][2]
    except:
        return None 
    if(int(price)>0 and len(p_name)>0 ):
        sub_total=round(float(quantity)*int(price),2)
        trv.insert("",'end',values=[eng,p_name,quantity,price,sub_total])
        my_sum() # 
        cb1.set(p_name)
        cb2.set(eng)
        el1.set(quantity)
        pr.set(price)
        to.set(sub_total)
my_menu2={}
my_menu={} # Dictionary to store items with price
def show_items(cat): # Populating the Combobox 
    global my_menu,my_menu2
    my_menu.clear() # remove all items
    cb1.set('')
    e1.delete(0,END)
    r_set=my_conn.execute("select * FROM material WHERE qnt>0")
    
    for item in r_set:
        my_menu.update({item[0]:item[1]}) 
        my_menu2.update({item[1]:[item[0],item[1],item[3]]})
    options=list(my_menu.values())
    cb1.config(values=options)
    b1=tk.Button(frame_m_left,text='Add',font=font2,
     command=lambda:my_add())
    b1.grid(row=0,column=2,padx=10)
bill=tk.Button(frame_m_left,text='Add bill',command=add)
bill.grid(row=7,column=0)
show_items(1)
 # We used integer variable here 


my_w.mainloop()
