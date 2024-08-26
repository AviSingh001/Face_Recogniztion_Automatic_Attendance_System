from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector

class Developer:
     def __init__(self,root):
           self.root=root
           self.root.geometry("1350x700+0+0")
           self.root.title("Face Recognition System")

           title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="red")
           title_lbl.place(x=0,y=0,width=1350,height=50)

           bg_img=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           bg_img=bg_img.resize((1350,650))
           self.photoimg_bg=ImageTk.PhotoImage(bg_img)
    
           f_lbl3=Label(self.root,image=self.photoimg_bg)
           f_lbl3.place(x=0,y=50,width=1350,height=650)

           #main Frame

           main_frame=Frame(f_lbl3,bd=2,bg="white")
           main_frame.place(x=950,y=0,width=400,height=500)

           gp_img=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           gp_img=bg_img.resize((125,125))
           self.photoimg_gp=ImageTk.PhotoImage(gp_img)
    
           f_lbl=Label(main_frame,image=self.photoimg_gp)
           f_lbl.place(x=270,y=0,width=125,height=125)

           # Developer Info

           dev_label=Label(main_frame,text="Hello My Name is Avi ",font=("times new roman",20,"bold"),bg="white")
           dev_label.place(x=0,y=5)

           info_label=Label(main_frame,text="MCA Student ",font=("times new roman",20,"bold"),bg="white")
           info_label.place(x=0,y=45)

           bg1_img=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           bg1_img=bg_img.resize((390,365))
           self.photoimg1_bg=ImageTk.PhotoImage(bg1_img)
    
           f_lbl4=Label(main_frame,image=self.photoimg1_bg)
           f_lbl4.place(x=3,y=130,width=390,height=365)







if __name__ == "__main__":
         root=Tk()
         obj=Developer(root)
         root.mainloop()