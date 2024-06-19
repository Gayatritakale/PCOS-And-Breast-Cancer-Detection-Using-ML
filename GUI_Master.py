

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''

root=tk.Tk()

root.title("PCOS and Breast Cancer Detection")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#800517")

bg = Image.open(r"d1.jpg")
bg.resize((1866,1900),Image.ANTIALIAS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=0)
#, relwidth=1, relheight=1)

# video_label =tk.Label(root)
# video_label.pack()
# # read video to display on label
# player = tkvideo("road1.mp4", video_label,loop = 1, size = (w, h))
# player.play()

w = tk.Label(root, text="PCOS and Breast Cancer Detection",width=85,background="#A7C2E5",foreground="black",height=2,border=0,font=("Times new roman",25,"bold"))
w.place(x=0,y=0)






# label=tk.Label(root,text='''
#                These PCOS quotes are a powerful reminder that
#                so many people worldwide are grappling with the
#                real-life implications of PCOS. Not only that, but
#                some of these messages show it’s possible to lead a happy
#                life despite PCOS – whatever that happiness looks like for you.
#                '''
#                ,font=("Calibri",12),
               
#                fg="black")
# label.place(x=400,y=200)

# label=tk.Label(root,text='''
#               Having cancer does make you try to be better at everything
#               you do and enjoy every moment. It changes you forever.
#               But it can be a positive change.
#                '''
#                ,font=("Calibri",12),
               
#                fg="black")
# label.place(x=600,y=400)

from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","GUI_Main_and_train.py"])
def Register():
    from subprocess import call
    call(["python","GUI_Master_old.py"])

def pre():
    from subprocess import call
    call(["python","precautions.py"])
    
def diet():
    from subprocess import call
    call(["python","diet_plan.py"])





d2=tk.Button(root,text="PCOS Detection",command=Login,width=20,height=2,bd=0,background="#59D7EE",foreground="black",font=("times new roman",17,"bold"))
d2.place(x=670,y=500)


d3=tk.Button(root,text="Breast Cancer Detection",command=Register,width=20,height=2,bd=0,background="#59D7EE",foreground="black",font=("times new roman",17,"bold"))
d3.place(x=670,y=600)



root.mainloop()
