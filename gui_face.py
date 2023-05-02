from tkinter import *
import os

root = Tk(className = 'face_recognition_gui')
svalue = StringVar() # defines the widget state as string

w = Entry(root,textvariable=svalue) # adds a textarea widget
w.pack()



def train_eigen_btn_load():
    name = svalue.get()
    os.system('python face_train_eigen.py %s'%name)


def recog_eigen_btn_load():
    os.system('python face_recog_eigen.py')



trainE_btn = Button(root,text="Train (EigenFaces)", command=train_eigen_btn_load)
trainE_btn.pack()

recogE_btn = Button(root,text="Recognize (EigenFaces)", command=recog_eigen_btn_load)
recogE_btn.pack()

root.mainloop()