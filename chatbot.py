from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import numpy as np



class ChatBot:
     def __init__(self,root):
           self.root=root
           self.root.geometry("550x500+0+0")
           self.root.title("CHATBOT")

           main_frame=Frame(self.root,bd=4,bg="powder blue",width=500)
           main_frame.pack()

           img_chat=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           img_chat=img_chat.resize((150,70))
           self.photoimg_chat=ImageTk.PhotoImage(img_chat)

           title_lbl=Label(main_frame,text="Chat Me",bd=3,relief=RAISED,anchor='nw',width=550,compound=LEFT,image=self.photoimg_chat,font=("Arial",26,'bold'),fg='green',bg='white')
           title_lbl.pack(side=TOP)

          # scroll_x=ttk.Scrollbar(main_frame,orient=HORIZONTAL)
           self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
           self.text=Text(main_frame,width=60,height=15,bd=10,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
           self.scroll_y.pack(side=RIGHT,fill=Y)
           self.text.pack()


           btn_frame=Frame(self.root,bd=4,bg='white',width=550,height=62)
           btn_frame.pack()

           lbl=Label(btn_frame,text="Type :",font=("Arial",10,'bold'),fg='green',bg='white',width=50,height=26)
           lbl.place(x=0,y=1,width=50,height=26)

           self.entry=ttk.Entry(btn_frame,width=60,font=("Arial",10,'bold'))
           self.entry.place(x=55,y=1,width=490,height=24)

           bttn_frame=Frame(btn_frame,bd=4,bg='white',width=550,height=36)
           bttn_frame.place(x=0,y=25,width=550,height=33)

           self.search=Button(bttn_frame,text="Search",command=self.search_data,font=("Arial",10,'bold'),width=8,bg='green',relief=RAISED,bd=5)
           self.search.place(x=0,y=0,width=80,height=30)

           self.msg=''
           self.lbl1=Label(bttn_frame,text=self.msg,font=("Arial",10,'bold'),fg='green',bg='white')
           self.lbl1.place(x=160,y=0,width=200,height=30)

           self.Clear=Button(bttn_frame,text="Clear",font=("Arial",8,'bold'),width=8,bg='red',relief=RAISED,bd=5)
           self.Clear.place(x=460,y=0,width=80,height=30)

           #=================Function Declaration======================

     def search_data(self):
            send='\t\t\t'+'You: '+self.entry.get()
            self.text.insert(END,'\n'+send)

            if(self.entry.get()==''):
                   self.msg='Please Enter Some Input'
                   self.lbl1.config(text=self.msg,fg='red')
            else:
                   self.msg=''
                   self.lbl1.config(text=self.msg,fg='red') 

            if(self.entry.get()=="hello"):
                   self.text.insert(END,'\n\n'+'Bot: Hi')

            




           #f_lbl=Label(self.root,image=self.photoimg_chat)
           #f_lbl.place(x=0,y=50,width=1350,height=300)




if __name__ == "__main__":
         root=Tk()
         obj=ChatBot(root)
         root.mainloop()
         