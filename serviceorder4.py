from cgitb import text
from telnetlib import STATUS
from tkinter import *
from cProfile import label
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from colorama import Cursor
from numpy import number, product
import pymysql
import pandas as pd
from time import strftime
# initalise the tkinter GUI
root = tk.Tk()
frame2 = tk.LabelFrame(root, text="Excel Data")
frame2.place(height=200, width=850, x=10, y=550)
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='214531',
        db='pythongui',
    )
    return conn
def refreshTable():
    for data in tv2.get_children():
        tv2.delete(data)

    for array in read():
        tv2.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    tv2.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    

tv2 = ttk.Treeview(frame2)
tv2.place(relheight=1, relwidth=1)  

treescrolly = tk.Scrollbar(frame2, orient="vertical", command=tv2.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame2, orient="horizontal", command=tv2.xview) # command means update the xaxis view of the widget
tv2.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget

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
l1 = tk.StringVar()
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
    
    
def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM serviceorder ORDER BY s_id DESC ")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    s_id = str('')
    cid = str(cidEntry.get())
    cname = str(nameEntry.get())
    number = str(numberEntry.get())
    address = str(addressEntry.get())
    pin = str(pinEntry.get())
    product = str(productEntry.get())
    ename = str(cb3.get())
    status=str('non')
    date = str(l1.cget("text"))

    if (cid == "" or cid == " ") or (cname == "" or cname == " ") or (number == "" or number == " ") or (address == "" or address == " ") or (pin == "" or pin == " ")or (product == "" or product == " ")or (ename == "" or ename == " ")or (status == "" or status == " ")or (date == "" or date == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("insert INTO serviceorder(cid,cname,number,address,pin,product,ename,status,date) VALUES ('"+cid+"','"+cname+"','"+number+"','"+address+"','"+pin+"','"+product+"','"+ename+"','"+status+"','"+date+"') ")
            conn.commit()
            conn.close()
        
        

    refreshTable()
def select():
    try:
        selected_item = tv1.selection()[0]
        id = str(tv1.item(selected_item)['values'][0])
        name = str(tv1.item(selected_item)['values'][1])
        number = str(tv1.item(selected_item)['values'][2])
        address = str(tv1.item(selected_item)['values'][3])
        pin = str(tv1.item(selected_item)['values'][4])
        product = str(tv1.item(selected_item)['values'][5])
        

        setph(id,1)
        setph(name,2)
        setph(number,3)
        setph(address,4)
        setph(pin,5)
        setph(product,6)


    except:
        messagebox.showinfo("Error", "Please select a data row")


root.geometry("1000x1000") # set the root dimensions
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable() # makes the root window fixed in size.

# Frame for TreeView
frame1 = tk.LabelFrame(root, text="Excel Data")
frame1.place(height=250, width=800,x=20,y=5)

# Frame for open file dialog
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=400, y=300, x=10)

frame_m_right=tk.Frame(root,bg='#f8fab4')
frame_m_left=tk.Frame(root,bg='#284474')
# Buttons
button1 = tk.Button(file_frame, text="Browse A File", command=lambda: File_dialog())
button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
button2.place(rely=0.65, relx=0.30)

# The file/file path text
label_file = ttk.Label(file_frame, text="No File Selected")
label_file.place(rely=0, relx=0)


## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1) # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=tv1.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=tv1.xview) # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget


def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"),("All Files", "*.*")))
    label_file["text"] = filename
    return None


def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column) # let the column heading = column name

    df_rows = df.to_numpy().tolist() # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end", values=row) # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None



cidLabel = Label(root, text="C_ID", font=('Arial', 15))
nameLabel = Label(root, text="C_Name", font=('Arial', 15))
numberLabel = Label(root, text="Number", font=('Arial', 15))
addressLabel = Label(root, text="Address", font=('Arial', 15))
pinLabel = Label(root, text="PIN Code", font=('Arial', 15))
productLabel = Label(root, text="Product", font=('Arial', 15))

cidLabel.place(x=450, y=300)
nameLabel.place(x=450, y=340)
numberLabel.place(x=450, y=380)
addressLabel.place(x=450, y=420)
pinLabel.place(x=450, y=460)
productLabel.place(x=450, y=500)

cidEntry = Entry(root, width=25, bd=5, font=('Arial', 15), textvariable = ph1)
nameEntry = Entry(root, width=25, bd=5, font=('Arial', 15), textvariable = ph2)
numberEntry = Entry(root, width=25, bd=5, font=('Arial', 15), textvariable = ph3)
addressEntry = Entry(root, width=25, bd=5, font=('Arial', 15), textvariable = ph4)
pinEntry = Entry(root, width=25, bd=5, font=('Arial', 15), textvariable = ph5)
productEntry = Entry(root, width=25, bd=5, font=('Arial', 15), textvariable = ph6)

cidEntry.place(x=550, y=300)
nameEntry.place(x=550, y=340)
numberEntry.place(x=550, y=380)
addressEntry.place(x=550, y=420)
pinEntry.place(x=550, y=460)
productEntry.place(x=550, y=500)





tv2["columns"] = ("1", "2","3","4","5","6","7","8","9","10")
tv2.column("#0",width=0, stretch=NO)
tv2.column("1", width = 17, anchor ='w') 
tv2.column("2", width =17, anchor ='w') 
tv2.column("3", width = 17, anchor ='w') 
tv2.column("4", width = 17, anchor ='w')  
tv2.column("5", width = 17, anchor ='w') 
tv2.column("6", width = 17, anchor ='w')
tv2.column("7", width = 17, anchor ='w')
tv2.column("8", width = 17, anchor ='w')
tv2.column("9", width = 17, anchor ='w')
tv2.column("10", width = 17, anchor ='w')  
# Headings  
# respective columns
tv2.heading("#0",anchor='w')
tv2.heading("1", text ="S_id",anchor='w')
tv2.heading("2", text ="C_id",anchor='w')
tv2.heading("3", text ="Name",anchor='w')
tv2.heading("4", text ="Number",anchor='w')
tv2.heading("5", text ="Address",anchor='w')
tv2.heading("6", text ="pin",anchor='w')
tv2.heading("7", text ="product",anchor='w')
tv2.heading("8", text ="Ename",anchor='w')
tv2.heading("9", text ="status",anchor='w')
tv2.heading("10", text ="date",anchor='w')

selectBtn = tk.Button(
    root, text="Select Customer", padx=60, pady=7, width=5,
    bd=3, font=('Arial', 15), bg="#EEEEEE", command=select)
selectBtn.place(x=220, y=250)
addBtn = Button(
    root, text="Create Order", padx=60, pady=7, width=5,
    bd=3, font=('Arial', 15), bg="#EEEEEE", command=add)
addBtn.place(x=220,y= 470 )
def clear_data():
    tv1.delete(*tv1.get_children())
    return None
query="SELECT distinct(category) as category FROM engineer"
conn = connection()
cursor = conn.cursor()
cursor.execute(query)
my_list = [r for r, in cursor]
my_list2=[]  
my_list3=[]
my_list4=[]

sel=tk.StringVar()
def my_up(*args):
    cb3.set('') # remove the previous selected option 
    query2="select name FROM engineer WHERE area='"+ph5.get()+"' and category='"+sel.get()+"'"
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(query2) # SQLAlchem engine result
    my_list3 = [r for r, in cursor] # create a  list 
    cb3['values']=my_list3
    


sel1=tk.StringVar()


cb1 = ttk.Combobox(root, values=my_list,width=15,textvariable=sel)
cb1.place(x=860,y=300)
l2=tk.Label(root,font=('Times',22,'bold'),text='Category',fg='red')
l2.place(x=860,y=250)
sel.trace('w',my_up)
 # track the change event 


cb3 = ttk.Combobox(root, values=my_list3,width=15,textvariable=ph8)
cb3.place(x=860,y=400)

l2=tk.Label(root,font=('Times',22,'bold'),text='Engineer',fg='red')
l2.place(x=860,y=350)
def my_time():
    time_string = strftime('%Y-%m-%d') # time format 
    l1.config(text=time_string)
    l1.after(1000,my_time) # time delay of 1000 milliseconds 
	
my_font=('times',20,'bold') # display size and style

l1=tk.Label(root,font=my_font,bg='yellow')
l1.place(x=850,y=30)

my_time()


root.mainloop()