from tkinter import *
from tkinter import messagebox as ms
import sqlite3
import tkinter as tk 
from PIL import Image, ImageTk
root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
# root.title("Forget Password")


email= tk.StringVar()
password = tk.StringVar()
confirmPassword = tk.StringVar()

image2 = Image.open('3.webp')
image2 = image2.resize((1530, 900), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)


db = sqlite3.connect('profile.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS KneeReg"
               "(name TEXT, address TEXT,  Email TEXT, country TEXT, Phoneno TEXT,Gender TEXT, password TEXT)")
db.commit()

# l=tk. Label(root,text='Email',font=('Cambria',14)).place(x=570,y=280)
# new_password_entry=tk.Entry(root,width=40,textvariable=password).place(x=730,y=280)

l=tk. Label(root,text='Email',font=('Cambria',14)).place(x=100,y=220)
new_password_entry=tk.Entry(root,width=40,textvariable=email).place(x=230,y=220)


l=tk. Label(root,text='New Password',font=('Cambria',14)).place(x=60,y=280)
new_password_entry=tk.Entry(root,width=40,textvariable=password).place(x=230,y=280)

l=tk. Label(root,text='Confirm Password',font=('Cambria',14,)).place(x=60,y=315)

confirm_password_entry=tk.Entry(root,width=40,show="*",textvariable=confirmPassword).place(x=230,y=319)

def change_password():
    
    
    #Email=email.get()
    new_password_entry = password.get()
    confirm_password_entry = confirmPassword.get()
    
    with sqlite3.connect('profile.db') as db:
        c = db.cursor()

    
    find_user = ('SELECT * FROM KneeReg WHERE Email=?')
    c.execute(find_user, [(str(email.get()))])
    
    
    #find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
    #c.execute(find_entry, [(email.get()), (password.get())])
    
    result = c.fetchall()
    if result:
        if new_password_entry == confirm_password_entry:
            db = sqlite3.connect("profile.db")
            curs = db.cursor()
    
            curs.execute("update KneeReg set password=? WHERE Email=? ",(str(new_password_entry),email.get()))
            #curs.execute(insert, [new_password_entry ])
            db.commit()
            db.close()
            ms.showinfo('Congrats', 'Password changed successfully')
            root.destroy()
    
        else:
            ms.showerror('Error!', "Passwords didn't match")
            root.destroy()










b=tk.Button(root,text="Send",width=10,command=change_password)
#tk.messagebox.showinfo("Password Updated", "Your password has been updated successfully.")
b.place(x=220,y=390)

# button2=tk.Button(root,text="Forgot Password?",fg='blue',bg='light gray')
# button2.place(x=850,y=370)

root. mainloop()


