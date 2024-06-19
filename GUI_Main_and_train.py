from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("Pcos Detection")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
# ++++++++++++++++++++++++++++++++++++++++++++

image2 = Image.open("img5.jpg")

image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)


background_label = tk.Label(root, image=background_image)
background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
lbl = tk.Label(root, text="Pcos detection", font=('times', 35,' bold '), height=1, width=55,bg="#A7C2E5",fg="black")
lbl.place(x=0, y=0)
# _+++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = pd.read_csv(r"PCOS_infertility.csv")


data = data.dropna()

le = LabelEncoder()



def Data_Preprocessing():
    data = pd.read_csv("PCOS_infertility.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['No'] = le.fit_transform(data['No'])
    
    data['Patient_File_No'] = le.fit_transform(data['Patient_File_No'])
    
    data['   beta_HCG_mIU_mL'] = le.fit_transform(data['   beta_HCG_mIU_mL'])
    
    data['beta_HCG_mI_mL'] = le.fit_transform(data['beta_HCG_mI_mL'])

    data['AMH_ng_mL'] = le.fit_transform(data['AMH_ng_mL'])
    
   
    
   
    
  

    """Feature Selection => Manual"""
    x = data.drop(['PCOS (Y/N)'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['PCOS (Y/N)']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("times", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=200, y=80)


def Model_Training():
    data = pd.read_csv("PCOS_infertility.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    le = LabelEncoder()
    
    data['No'] = le.fit_transform(data['No'])
    
    data['Patient_File_No'] = le.fit_transform(data['Patient_File_No'])
    
    data['   beta_HCG_mIU_mL'] = le.fit_transform(data['   beta_HCG_mIU_mL'])
    
    data['beta_HCG_mI_mL'] = le.fit_transform(data['beta_HCG_mI_mL'])

    data['AMH_ng_mL'] = le.fit_transform(data['AMH_ng_mL'])
    

    

    """Feature Selection => Manual"""
    x = data.drop(['PCOS (Y/N)'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['PCOS (Y/N)']
    print(type(y))
    x.shape

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25,random_state=123)

    # from sklearn.svm import SVC
    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    
    # from sklearn.linear_model import LogisticRegression 
    # svcclassifier = LogisticRegression() 
    # svcclassifier.fit(x_train, y_train)
    
    from sklearn.tree import DecisionTreeClassifier 
    svcclassifier = DecisionTreeClassifier()
    svcclassifier.fit(x_train, y_train)
    
    y_pred = svcclassifier.predict(x_test)
    print(y_pred)

    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accracy : "+str(ACC)+"%\nModel saved as new.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"new.joblib")
    print("Model saved as new.joblib")



def call_file():
    from subprocess import call
    call(["python","Check_Prediction.py"])

def file():
    from subprocess import call
    call(["python","pcos precaution.py"])



def window():
    root.destroy()

button2 = tk.Button(root, foreground="black", background="#A7C2E5", font=("times", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
button2.place(x=5, y=90)

# 

button4 = tk.Button(root, foreground="black", background="#A7C2E5", font=("times", 14, "bold"),
                    text="PCOS Prediction", command=call_file, width=15, height=2)
button4.place(x=5, y=190)

button4 = tk.Button(root, foreground="black", background="#A7C2E5", font=("times", 14, "bold"),
                    text="Precaution", command=file, width=15, height=2)
button4.place(x=5, y=290)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 14, ' bold '),bg="red",fg="white")
exit.place(x=5, y=390)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''