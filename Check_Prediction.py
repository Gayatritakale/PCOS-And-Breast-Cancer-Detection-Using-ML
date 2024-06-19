#from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    from tkinter import ttk, LEFT, END
    from PIL import Image, ImageTk
    from tkinter.filedialog import askopenfilename
    from tkinter import messagebox as ms
    import cv2
    import sqlite3
    import os
    #import numpy as np
    import time
    import numpy as np
    import pandas as pd
    from tkinter import ttk
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder
    import tkinter as tk 
    import tkinter
    import sqlite3
    import random
    from tkinter import messagebox as ms
    from PIL import Image,ImageTk
   # from tkinter.ttk import *


    root=tk.Tk()

    root.title("PCOS and Breast Cancer Detection")
    w,h = root.winfo_screenwidth(),root.winfo_screenheight()
    
    root.geometry("%dx%d+0+0" % (w, h))
    # bg = Image.open(r"img7.jpg")
    # bg.resize((w,h),Image.ANTIALIAS)
    # print(w,h)
    # bg_img = ImageTk.PhotoImage(bg)
    # bg_lbl = tk.Label(root,image=bg_img)
    # bg_lbl.place(x=0,y=93)
   #, relwidth=1, relheight=1)

   # video_label =tk.Label(root)
   # video_label.pack()
   # # read video to display on label
   # player = tkvideo("road1.mp4", video_label,loop = 1, size = (w, h))
   # player.play()
   
    image2 = Image.open("1.jpg")

    image2 = image2.resize((w, h), Image.ANTIALIAS)

    background_image = ImageTk.PhotoImage(image2)


    background_label = tk.Label(root, image=background_image)
    background_label.image = background_image

    background_label.place(x=0, y=0) 


    # w = tk.Label(root, text="PCOS and Breast Cancer Detection",width=85,background="#800517",foreground="white",height=2,font=("Times new roman",19,"bold"))
    # w.place(x=0,y=0)
    
    # # 
    
    No= tk.IntVar()
    Patient_File_No= tk.IntVar()
    beta_HCG_mIU_mL = tk.IntVar()
    beta_HCG_mI_mL = tk.IntVar()
    AMH_ng_mL= tk.IntVar()
   
   
   #root.geometry("%dx%d+0+0" % (w,h))
   # oot.title("Background Image")

      
   
    #===================================================================================================================



    def Detect():
        
        
        
        e1=No.get()
        print(e1)
       
        e2=Patient_File_No.get()
        print(e2)
        
        e3=beta_HCG_mIU_mL.get()
        print(e3)
        
        e4=beta_HCG_mI_mL.get()
        print(e4)
        
        e5=AMH_ng_mL.get()
        print(e5)
        
        
       
           
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('new.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5]])
        print(v)
    
        if v[0]==0:
           print("No pcos ")
           yes = tk.Label(root,text="No pcos \n “PCOS is a journey that requires patience and understanding.” \n “PCOS may be a hurdle, but we are strong enough to jump over it.” \n  “PCOS – a journey that has taught us resilience and perseverance.” \n PCOS may slow us down, but it won't stop us from reaching our goals and dreams",background="green",foreground="white",font=('times', 20, ' bold '),width=70,height=7)
           yes.place(x=250,y=500)
           
               
        if v[0]==1:
            print("pcos detected")
            yes = tk.Label(root,text="pcos detected  \n Stay at a healthy weight. Weight loss can lower insulin and androgen levels. \n It also may restore ovulation.Limit carbohydrates.\n High-carbohydrate diets might make insulin levels go higher. \nBe active. Exercise helps lower blood sugar levels"
                          ,background="red",foreground="white",font=('times', 20, ' bold '),width=70,height=7)
            yes.place(x=250,y=500)
            import webbrowser  
            def open_google():
                webbrowser.open("https://www.practo.com/pune/treatment-for-liver-disease")
            label = tk.Label(root, text="https://www.practo.com/pune/treatment-for-liver-disease", fg="blue", cursor="hand2")
            label.place(x=650,y=700)

# Bind the label to the function that opens Google when clicked
            label.bind("<Button-1>", lambda e: open_google())
    
    l1=tk.Label(root,text="No",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l1.place(x=450,y=100)
    No=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=No)
    No.place(x=900,y=100)
    
    
    l2=tk.Label(root,text="Patient_File_No",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l2.place(x=450,y=150)
    Patient_File_No=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Patient_File_No)
    Patient_File_No.place(x=900,y=150)
    
   
   
   

    
    l3=tk.Label(root,text="beta_HCG_mIU_mL",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l3.place(x=450,y=200)
    beta_HCG_mIU_mL=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=beta_HCG_mIU_mL)
    beta_HCG_mIU_mL.place(x=900,y=200)
    
    l4=tk.Label(root,text="beta_HCG_mI_mL",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l4.place(x=450,y=250)
    beta_HCG_mI_mL=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=beta_HCG_mI_mL)
    beta_HCG_mI_mL.place(x=900,y=250)
     
     
    l5=tk.Label(root,text="AMH_ng_mL",background="darkolivegreen1",font=('times', 20, ' bold '),width=25)
    l5.place(x=450,y=300)
    AMH_ng_mL=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=AMH_ng_mL)
    AMH_ng_mL.place(x=900,y=300)
    
    
     
    
      
   
    
    button1 = tk.Button(root, foreground="white", background="red",text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=600,y=430)
    
    
    

    root.mainloop()

Train()