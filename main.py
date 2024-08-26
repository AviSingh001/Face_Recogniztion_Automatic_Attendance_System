from time import strftime
from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import StudentAttendance
from developer import Developer
from help import Help
from datetime import datetime
from chatbot import ChatBot
import os


class Face_Recognition_System:
    def __init__(self,root):
           self.root=root
           self.root.geometry("1350x700+0+0")
           self.root.title("Face Recognition System")

    #  img=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           img=Image.open(r"E:\Face Recognition System\photos\bg1.jpeg")
           img=img.resize((300,130))
           self.photoimg=ImageTk.PhotoImage(img)
    
           f_lbl=Label(self.root,image=self.photoimg)
           f_lbl.place(x=0,y=0,width=300,height=130)

           img1=Image.open(r"E:\Face Recognition System\photos\bg2.jpeg")
           img1=img1.resize((300,130))
           self.photoimg1=ImageTk.PhotoImage(img1)
    
           f_lbl1=Label(self.root,image=self.photoimg1)
           f_lbl1.place(x=500,y=0,width=300,height=130)

           img2=Image.open(r"E:\Face Recognition System\photos\bg3.jpeg")
           img2=img2.resize((300,130))
           self.photoimg2=ImageTk.PhotoImage(img2)
    
           f_lbl2=Label(self.root,image=self.photoimg2)
           f_lbl2.place(x=1000,y=0,width=300,height=130)

           img3=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           img3=img3.resize((1350,670))
           self.photoimg3=ImageTk.PhotoImage(img3)
    
           bg_img=Label(self.root,image=self.photoimg3)
           bg_img.place(x=0,y=130,width=1350,height=670)

           title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",30,"bold"),bg="white",fg="red")
           title_lbl.place(x=0,y=0,width=1380,height=50)

        #===========================Time Show=======================
           def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text= string)
            lbl.after(1000, time)  #1s=1000ms


           lbl=Label(title_lbl,font=("times new roman",14,'bold'),background='white',foreground='blue')
           lbl.place(x=0,y=0,width=110,height=50)
           time()

       #b1
           img4=Image.open(r"E:\Face Recognition System\photos\student.jpeg")
           img4=img4.resize((220,220))
           self.photoimg4=ImageTk.PhotoImage(img4)

           b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
           b1.place(x=100,y=100,width=200,height=180)

           b11=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="Black",fg="white")
           b11.place(x=100,y=278,width=200,height=20)


       #b5
           img8=Image.open(r"E:\Face Recognition System\photos\train.jpeg")
           img8=img8.resize((220,220))
           self.photoimg8=ImageTk.PhotoImage(img8)
           b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
           b5.place(x=100,y=350,width=200,height=180)

           b55=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg="Black",fg="white")
           b55.place(x=100,y=528,width=200,height=20)

       #b2
           img5=Image.open(r"E:\Face Recognition System\photos\face.jpeg")
           img5=img5.resize((220,220))
           self.photoimg5=ImageTk.PhotoImage(img5)

           b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
           b2.place(x=400,y=100,width=200,height=180)

           b22=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),bg="Black",fg="white")
           b22.place(x=400,y=278,width=200,height=20)

       #b6
           img9=Image.open(r"E:\Face Recognition System\photos\phots.jpg")
           img9=img9.resize((220,220))
           self.photoimg9=ImageTk.PhotoImage(img9)

           b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
           b6.place(x=400,y=350,width=200,height=180)

           b66=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="Black",fg="white")
           b66.place(x=400,y=528,width=200,height=20)

       #b3
           img6=Image.open(r"E:\Face Recognition System\photos\attend.jpeg")
           img6=img6.resize((220,180))
           self.photoimg6=ImageTk.PhotoImage(img6)

           b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
           b3.place(x=720,y=100,width=200,height=180)

           b33=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",12,"bold"),bg="Black",fg="white")
           b33.place(x=720,y=278,width=200,height=20)

       #b7
           img10=Image.open(r"E:\Face Recognition System\photos\developer.jpeg")
           img10=img10.resize((220,220))
           self.photoimg10=ImageTk.PhotoImage(img10)

           b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
           b7.place(x=720,y=350,width=200,height=180)

           b77=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",12,"bold"),bg="Black",fg="white")
           b77.place(x=720,y=528,width=200,height=20)

       #b4
           img7=Image.open(r"E:\Face Recognition System\photos\helpdesk.jpeg")
           img7=img7.resize((200,180))
           self.photoimg7=ImageTk.PhotoImage(img7)

           b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help)
           b4.place(x=1050,y=100,width=200,height=180)

           b44=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help,font=("times new roman",12,"bold"),bg="Black",fg="white")
           b44.place(x=1050,y=278,width=200,height=20)

       #b8
           img11=Image.open(r"E:\Face Recognition System\photos\exit.jpg")
           img11=img11.resize((220,220))
           self.photoimg11=ImageTk.PhotoImage(img11)

           b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
           b8.place(x=1050,y=350,width=200,height=180)

           b88=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",12,"bold"),bg="Black",fg="white")
           b88.place(x=1050,y=528,width=200,height=20)


        #==============================Chat BOT==============================

           imgchat=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           imgchat=imgchat.resize((60,50))
           self.photoimgchat=ImageTk.PhotoImage(imgchat)

           bchat=Button(bg_img,image=self.photoimgchat,cursor="hand2",command=self.chatbot1_btn)
           bchat.place(x=1275,y=0,width=60,height=50)



       #===============================

    def open_img(self):
          os.startfile("data")
          
    def iExit(self):
           self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are U Sure exit this Project",parent=self.root)
           if self.iExit>0:
                  self.root.destroy()
           else:
                  return

       #================Function Button==================
         
    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)

            #===================
    def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)


            #======================================

    def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)

            #====================================
     
    def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=StudentAttendance(self.new_window)

            #=====================================
    def developer_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Developer(self.new_window) 

            #=====================================
    def help(self):
            self.new_window=Toplevel(self.root)
            self.app=Help(self.new_window)

            #=====================================
    def chatbot1_btn(self):
            self.new_window=Toplevel(self.root)
            self.app=ChatBot(self.new_window) 
                 



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
