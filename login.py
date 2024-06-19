import tkinter as tk 
import tkinter
import sqlite3
import random
from tkinter import messagebox as ms
from PIL import Image,ImageTk
from tkinter.ttk import *

root=tk.Tk()
root.configure(background='white')

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
# oot.title("Background Image")

image2=Image.open('3.jpg')
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root,image=background_image)
background_label.image = background_image
background_label.place(x=0,y=0)

#############################################################################################################


Email = tk.StringVar()
password = tk.StringVar() 
 
def login():
 

    with sqlite3.connect('profile.db') as db:
         c = db.cursor()

        
         db = sqlite3.connect('profile.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS KneeReg"
                        "(name TEXT, address TEXT,  Email TEXT, country TEXT, Phoneno TEXT, Gender TEXT, password TEXT)")
         db.commit()
         
         
         find_entry = ('SELECT * FROM KneeReg WHERE Email = ? and password = ?')
         
         c.execute(find_entry, [(Email.get()), (password.get())])
         result = c.fetchall()
         if result:
            msg = ""
          
            print(msg)
            ms.showinfo("messege", "Login sucessfully")
            

            from subprocess import call
            call(['python','GUI_Master.py'])
            
           
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')





# New_Password=tk.StringVar()
# def forget():
#     con=sqlite3.connect("project11.db")
#     con.execute("""
#                 update registration set New_Password= Password where pass)

###############################################################################################################

label=tk.Label(root,text="PCOS and Breast Cancer Detection",font=("Calibri",45),
               bg="light blue",
               width=50,
               height=1)
label.place(x=0,y=0)


a11=tk. Label(root,text='Login here ',fg='black',bg ='light blue',font=('Forte',25)).place(x=900,y=150)

canvas1=tk.Canvas(root,background="light blue")
canvas1.place(x=750,y=220,width=500,height=350)

#login=Label(root,text="Login",font=('Arial',25),foreground='green').place(x=270,y=350)
a11=tk. Label(root,text='Enter Email',bg='light blue',font=('Cambria',14)).place(x=800,y=300)
a12=tk. Label(root,text='Enter Password',bg='light blue',font=('Cambria',14)).place(x=800,y=350)

b11=tk.Entry(root,width=40, textvariable=Email).place(x=970,y=300,)
b12=tk. Entry(root,width=40,show='*', textvariable=password).place(x=970,y=350,)


def forgot():
    from subprocess import call
    call(['python','forgot password.py'])


button2=tk.Button(root,text="Forgot Password?",fg='black',bg='#ADD8E6',command=forgot)
button2.place(x=850,y=513)



button2=tk.Button(root,text="Login",font=("Bold",9),command=login,width=50,fg='black',bg='#ADD8E6')
button2.place(x=830,y=410)

a=tk. Label(root,text='Not a Member?',font=('Cambria',11),bg='light blue').place(x=1050,y=470)

def reg():
    from subprocess import call
    call(['python','registration.py'])

button1=tk.Button(root,text="sign up",fg='black',bg='#ADD8E6',command=reg)
button1.place(x=1070,y=513,width=55)



root.mainloop()