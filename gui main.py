# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

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

bg = Image.open(r"p.png")
bg.resize((1866,1900),Image.ANTIALIAS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=0)
#, relwidth=1, relheight=1)

# video_label =tk.Label(root)
# video_label.pack()
# # read video to display on label
# player = tkvideo("vi.mp4", video_label,loop = 1, size = (w, h))
# player.play()

w = tk.Label(root, text="PCOS and Breast Cancer Detection",width=110,background="#7CB7AF",foreground="black",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=0)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#800517")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])


# wlcm=tk.Label(root,text="......Welcome to Pcops Detection System ......",width=120,height=23,background="#800517",foreground="white",font=("Times new roman",19,"bold"))
# wlcm.place(x=0,y=720)




d2=tk.Button(root,text="Login",command=Login,width=15,height=1,bd=0,background="#7CB7AF",foreground="black",font=("times new roman",17,"bold"))
d2.place(x=600,y=300)


d3=tk.Button(root,text="Register",command=Register,width=15,height=1,bd=0,background="#7CB7AF",foreground="black",font=("times new roman",17,"bold"))
d3.place(x=600,y=400)



root.mainloop()
