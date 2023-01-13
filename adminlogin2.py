from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import mysqlx
import pymysql
import _mysql_connector
from subprocess import call
class Login: 
   def back(self):
          import mainpage1
          
   def __init__(self,root):
      self.root=root
      self.root.title("Admin Login")
      self.root.geometry("1320x750+10+7")
      self.root.resizable(False,False)
      self.loginform()

   def loginform(self):
      Frame_login=Frame(self.root,bg="red")
      Frame_login.place(x=0,y=0,height=700,width=1366)
      self.img=ImageTk.PhotoImage(file="images/adminlogin.jpg")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=320,y=130,height=450,width=350)
      label1=Label(frame_input,text="Admin Login",font=('impact',32,'bold'),fg="black",bg='white')
      label1.place(x=75,y=20)
      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label2.place(x=30,y=95)
      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      self.email_txt.place(x=30,y=145,width=270,height=35)
      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label3.place(x=30,y=195)
      self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      self.password.place(x=30,y=245,width=270,height=35)
      btn1=Button(frame_input,text="forgot password?",cursor='hand2',
      font=('calibri',10),bg='white',fg='black',bd=0)
      btn1.place(x=125,y=305)
      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",
      font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=90,y=340)
      #btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      #btn3.place(x=110,y=390)
      btn3=Button(frame_input,text="BACK",command=self.back,cursor="hand2",
      font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn3.place(x=90,y=400)
      btn3.after(3000) 
   def login(self):
    
      if self.email_txt.get()=="" or self.password.get()=="":

         messagebox.showerror("Error","All fields are required",parent=self.root)

      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='214531',

                                database='pythongui')

            cur=con.cursor()

            cur.execute('select * from admin where name=%s and password=%s'

                        ,(self.email_txt.get(),self.password.get()))

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Error','Invalid Username And Password'

                                    ,parent=self.root)

               self.loginclear()

               self.email_txt.focus()

            else:

               self.Register()

               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}'

                                 ,parent=self.root)

            

   def Register(self):



      Frame_login1=Frame(self.root,bg="white")

      Frame_login1.place(x=0,y=0,height=700,width=1366)

      

      self.img=ImageTk.PhotoImage(file="images/img1.JPG")

      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)
      btn4=Button(Frame_login1,command=self.work,

                  text="Work Report",cursor="hand2",

                  font=("times new roman",15),fg="white",

                  bg="orangered",bd=0,width=15,height=1)

      btn4.place(x=110,y=190)
      btn5=Button(Frame_login1,command=self.work1,

                  text="Material Report",cursor="hand2",

                  font=("times new roman",15),fg="white",

                  bg="orangered",bd=0,width=15,height=1)
      
      btn5.place(x=110,y=250)
      frame_input2=Frame(self.root,bg='white')

      frame_input2.place(x=320,y=130,height=450,width=630)



      label1=Label(frame_input2,text="Register User",font=('impact',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=45,y=20)



      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),

                        bg='lightgray')

      self.entry2.place(x=30,y=245,width=270,height=35)



      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry3.place(x=330,y=145,width=270,height=35)



      label5=Label(frame_input2,text="Confirm Password",

                   font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label5.place(x=330,y=195)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry4.place(x=330,y=245,width=270,height=35)



      btn2=Button(frame_input2,command=self.register,text="Register"

                  ,cursor="hand2",font=("times new roman",15),fg="white",

                  bg="orangered",bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input2,command=self.loginform,

                  text="Already Registered?Login",cursor="hand2",

                  font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)





   def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      elif self.entry2.get()!=self.entry4.get():

         messagebox.showerror("Error","Password and Confirm Password Should Be Same"

                              ,parent=self.root)

      else:

         try:

            con=pymysql.connect(host="localhost",user="root",password="214531",

                                database="pythongui")

            cur=con.cursor()

            cur.execute("select * from register where emailid=%s"

                        ,self.entry3.get())

            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error"

               ,"User already Exist,Please try with another Email"

                                    ,parent=self.root)

               self.regclear()

               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)"

                           ,(self.entry.get(),self.entry3.get(),

                           self.entry2.get(),

                           self.entry4.get()))

               con.commit()

               con.close()

               messagebox.showinfo("Success","Register Succesfull"

                                   ,parent=self.root)

               self.regclear()

         except Exception as es:

            messagebox.showerror("Error",f"Error due to:{str(es)}"

                                 ,parent=self.root)

   def work(self):
          call(['python' , 'engineer_report9.py'])
   def work1(self):
          call(['python','material_report10.py'])
   
   def regclear(self):

      self.entry.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END)



   def loginclear(self):

      self.email_txt.delete(0,END)

      self.password.delete(0,END)

root=Tk() 
obj=Login(root)
root.mainloop()
