from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector

class Help:
     def __init__(self,root):
           self.root=root
           self.root.geometry("1350x700+0+0")
           self.root.title("Face Recognition System")

           title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="red")
           title_lbl.place(x=0,y=0,width=1350,height=50)

           bg_img=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           bg_img=bg_img.resize((1350,650))
           self.photoimg_bg=ImageTk.PhotoImage(bg_img)
    
           f_lbl3=Label(self.root,image=self.photoimg_bg)
           f_lbl3.place(x=0,y=50,width=1350,height=650)

           dev_label=Label(f_lbl3,text="Email:codewithDIT@gmail.com",font=("times new roman",20,"bold"),bg="white")
           dev_label.place(x=500,y=400)






if __name__ == "__main__":
         root=Tk()
         obj=Help(root)
         root.mainloop()