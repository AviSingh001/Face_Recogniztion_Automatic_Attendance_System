from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import numpy as np



class Train:
     def __init__(self,root):
           self.root=root
           self.root.geometry("1350x700+0+0")
           self.root.title("Face Recognition System")

           title_lbl=Label(self.root,text="Train Data Set",font=("times new roman",35,"bold"),bg="white",fg="red")
           title_lbl.place(x=0,y=0,width=1350,height=50)

           img_top=Image.open(r"E:\Face Recognition System\photos\fr.gif")
           img_top=img_top.resize((1350,300))
           self.photoimg_top=ImageTk.PhotoImage(img_top)
    
           f_lbl3=Label(self.root,image=self.photoimg_top)
           f_lbl3.place(x=0,y=50,width=1350,height=300)

           b33=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="Black",fg="white")
           b33.place(x=0,y=350,width=1350,height=50)

           img_bottom=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           img_bottom=img_bottom.resize((1350,300))
           self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)
    
           f_lbl3=Label(self.root,image=self.photoimg_bottom)
           f_lbl3.place(x=0,y=400,width=1350,height=300)


           #=============function for Training=================

     def train_classifier(self):
            data_dir=("data")
            path=[os.path.join(data_dir,file)for file in os.listdir(data_dir)]#list comprehensing

            faces=[]
            ids=[]

            for image in path:
                   img=Image.open(image).convert('L')#GRAY SCALE IMAGE
                   image_np=np.array(img,'uint8') #Converting image into grid scale
                   id=int(os.path.split(image)[1].split('.')[1])

               #    E:\Face Recognition System\data\user.4.1.jpg
                #    0                                1
                    
                   faces.append(image_np)
                   ids.append(id)
                   cv2.imshow("Training",image_np)
                   cv2.waitKey(1)==13
            ids=np.array(ids)


            #====================Train the Classifier and save===============

            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces,ids)
            clf.write("Classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Training Data Sets Completed!!!")
            

if __name__ == "__main__":
         root=Tk()
         obj=Train(root)
         root.mainloop()
