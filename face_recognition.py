from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import numpy as np
from time import strftime
from datetime import datetime


class Face_Recognition:
     def __init__(self,root):
           self.root=root
           self.root.geometry("1350x700+0+0")
           self.root.title("Face Recognition System")

           title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",44,"bold"),bg="white",fg="red")
           title_lbl.place(x=0,y=0,width=1350,height=50)

           img_left=Image.open(r"E:\Face Recognition System\photos\t.jpeg")
           img_left=img_left.resize((675,650))
           self.photoimg_left=ImageTk.PhotoImage(img_left)
    
           f_lbl3=Label(self.root,image=self.photoimg_left)
           f_lbl3.place(x=0,y=50,width=675,height=650)


           img_right=Image.open(r"E:\Face Recognition System\photos\fr.gif")
           img_right=img_right.resize((675,650))
           self.photoimg_right=ImageTk.PhotoImage(img_right)
    
           f_lbl3=Label(self.root,image=self.photoimg_right)
           f_lbl3.place(x=675,y=50,width=675,height=650)
           
           b33=Button(f_lbl3,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",26,"bold"),bg="Black",fg="white")
           b33.place(x=0,y=580,width=675,height=50)
           
           #=========================Attendance===================
     def mark_attendance(self,i,r,n,d):
           with open("Attendance.csv","r+",newline="\n") as f:
                 myDataList=f.readlines()
                 name_list=[]
                 for line in myDataList:
                       entry=line.split((",")) #kiran,1,Computer(Data will save as follows)
                       name_list.append(entry[0])
                  
                 if((i not in name_list) and (r not in name_list) and (n not in name_list) and ( d not in name_list)):
                       now=datetime.now()
                       d1=now.strftime("%d/%m/%Y")
                       dtString=now.strftime("%H:%M:%S")
                       f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

           #=================face recognition===========

     def face_recog(self):
            def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)       
                coord=[]

                for (x,y,w,h) in features:
                      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                      id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                      confidence=int((100*(1-predict/300)))

                      conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                      my_cursor=conn.cursor()

                      my_cursor.execute("Select Name from student where Student_id="+str(id))
                      n=my_cursor.fetchone()
                      n="+".join(n)

                      my_cursor.execute("Select Roll from student where Student_id="+str(id))
                      r=my_cursor.fetchone()
                      r="+".join(r)

                      my_cursor.execute("Select Dep from student where Student_id="+str(id))
                      d=my_cursor.fetchone()
                      d="+".join(d)

                      my_cursor.execute("Select Student_id from student where Student_id="+str(id))
                      i=my_cursor.fetchone()
                      i="+".join(i)



                      if confidence>77:
                            cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            cv2.putText(img,f"Dep:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                            self.mark_attendance(i,r,n,d)
                      else:
                             cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                             cv2.putText(img,f"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)


                      coord=[x,y,w,h]

                return coord 

            def recognize(img,clf,faceCascade):
                  coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
                  return img

            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("Classifier.xml") 

            video_cap=cv2.VideoCapture(0)

            while True:
                  ret,img=video_cap.read()
                  img=recognize(img,clf,faceCascade)
                  cv2.imshow("Welcome To Face Recognition",img)

                  if cv2.waitKey(1)==13:
                        break
            video_cap.release()
            cv2.destroyAllWindows()



if __name__ == "__main__":
         root=Tk()
         obj=Face_Recognition(root)
         root.mainloop()