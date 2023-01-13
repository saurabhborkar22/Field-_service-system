from fileinput import hook_compressed
from tkinter import*
from turtle import back
from PIL import ImageTk
from subprocess import call
root=Tk() 
class home:
       
   
   def __init__(self,root):
      self.root=root
      self.root.title("Reliance Field Service System")
      self.root.geometry("1250x700+50+60")

      #self.root.resizable(False,False)
      self.loginform()

   def loginform(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=700,width=1366)
      self.img=ImageTk.PhotoImage(file="images/img3.JPG")
      img=Label(Frame_login,image=self.img).place(x=0,y=10,width=1366,height=700)
      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=320,y=130,height=450,width=350)
      label1=Label(frame_input,text="Reliance Feild Service System",font=('impact',18,'italic'),fg="black",bg='white')
      label1.place(x=55,y=20)
    
def back():
       
       call(['python' , 'engineerRe8.py'])
def open1():
       call(['python' , 'serviceorder4.py'])
def open2():
       call(['python' , 'serv_upddate5.py'])
def open3():
       call(['python' , 'add_material6.py'])
def open4():
       call(['python' , 'material_reg7.py'])


menubar = Menu(root)
  
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Service Order', menu = file)
file.add_command(label ='Assign Work', command = open1)
file.add_command(label ='Check  Status', command = open2)

file.add_command(label ='Exit', command = root.destroy)
  
# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Material', menu = edit)
edit.add_command(label ='Add material', command = open3)
edit.add_command(label ='Register', command = open4)

  
# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Engineer', menu = help_)
help_.add_command(label ='Add Engineer', command= back)


root.config(menu = menubar)

obj=home(root)
root.mainloop()