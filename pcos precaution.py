import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import webbrowser



##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Tips")

#####For background Image
#loading the images
# img=ImageTk.PhotoImage(Image.open("8.jpg"))

# img2=ImageTk.PhotoImage(Image.open("8.jpg"))

# img3=ImageTk.PhotoImage(Image.open("8.jpg"))

image2 =Image.open('1.webp')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)


logo_label=tk.Label()
logo_label.place(x=0,y=0)

x=1


# function to change to next image
# def move():
#     global x
#     if x == 4:
#             x = 1
#     if x == 1:
#         logo_label.config(image=img)
#     elif x == 2:
#         logo_label.config(image=img2)
#     elif x == 3:
#         logo_label.config(image=img3)
#     x = x+1
#     root.after(2000, move)
  
# # calling the function
# move()

# calling the function
label_l1 = tk.Label(root, text="Pcos Detection",font=("Times New Roman", 18, 'bold'),
                    background="#647C90", fg="white", width=70, height=2)
label_l1.place(x=0, y=0)

#frame_display = tk.LabelFrame(root, text=" --Display-- ", width=900, height=250, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display.grid(row=0, column=0, sticky='nw')
#frame_display.place(x=300, y=100)

#frame_display1 = tk.LabelFrame(root, text=" --Result-- ", width=900, height=200, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display1.grid(row=0, column=0, sticky='nw')
#frame_display1.place(x=300, y=430)

#frame_display2 = tk.LabelFrame(root, text=" --Calaries-- ", width=900, height=50, bd=5, font=('times', 14, ' bold '),bg="lightblue4")
#frame_display2.grid(row=0, column=0, sticky='nw')
#frame_display2.place(x=300, y=380)



# frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=280, height=550, bd=5, font=('times', 14, ' bold '),bg="grey")
# frame_alpr.grid(row=0, column=0, sticky='nw')
# frame_alpr.place(x=10, y=130)





    
################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 

    
###########################################################################



        
        
        
               
               
               



def sym():
    
#     
    image2 =Image.open('symp.jpg')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=90)
        
def yoga():

    image2 =Image.open('yogap.png')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=90)
    
# def Robbery():

#     image2 =Image.open('types.jpg')
#     image2 =image2.resize((700,700), Image.ANTIALIAS)

#     background_image=ImageTk.PhotoImage(image2)

#     background_label = tk.Label(root, image=background_image)

#     background_label.image = background_image
#     background_label.place(x=350, y=90)
    
def diet():

    image2 =Image.open('dietp.jpg')
    image2 =image2.resize((700,700), Image.ANTIALIAS)

    background_image=ImageTk.PhotoImage(image2)

    background_label = tk.Label(root, image=background_image)

    background_label.image = background_image
    background_label.place(x=350, y=90)

def pre():
  
    from subprocess import call
    call(['python','GUI_Master.py'])



#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(root, text="Symptoms", command= sym, width=17, height=2,bd=0, font=('times', 15, ' bold '),bg="#647C90",fg="white")
button1.place(x=950, y=0)

button2 = tk.Button(root, text="What Is Yoga", command=yoga, width=17, height=2, bd=0,font=('times', 15, ' bold '),bg="#647C90",fg="white")
button2.place(x=1120, y=0)

# button3 = tk.Button(root, text="Types Of Yoga", command=Robbery, width=17, height=2,bd=0, font=('times', 15, ' bold '),bg="#647C90",fg="white")
# button3.place(x=1120, y=0)

button4 = tk.Button(root, text="Diet plan", command=diet, width=17, height=2,bd=0,bg="#647C90",fg="white", font=('times', 15, ' bold '))
button4.place(x=1320, y=0)





root.mainloop()

