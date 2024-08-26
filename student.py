from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector

class Student:
     def __init__(self,root):
           self.root=root
           self.root.geometry("1350x700+0+0")
           self.root.title("Face Recognition System")


      #===================variables====================
           self.var_dep=StringVar()
           self.var_course=StringVar()
           self.var_year=StringVar()
           self.var_semester=StringVar()
           self.var_std_id=StringVar()
           self.var_std_name=StringVar()
           self.var_div=StringVar()
           self.var_roll=StringVar()
           self.var_gender=StringVar()
           self.var_dob=StringVar()
           self.var_email=StringVar()
           self.var_phone=StringVar()
           self.var_address=StringVar()
           self.var_teacher=StringVar()
        

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

           title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
           title_lbl.place(x=0,y=0,width=1350,height=50)

           main_frame=Frame(bg_img,bd=2,bg="white")
           main_frame.place(x=10,y=50,width=1300,height=620)

         #left label frame
           
           left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
           left_frame.place(x=10,y=10,width=620,height=500)

           img_left=Image.open(r"E:\Face Recognition System\photos\sd.jpeg")
           img_left=img_left.resize((617,130))
           self.photoimg_left=ImageTk.PhotoImage(img_left)
    
           f_lbl3=Label(left_frame,image=self.photoimg_left)
           f_lbl3.place(x=0,y=0,width=617,height=100)

         #cc label frame
           cc_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
           cc_frame.place(x=10,y=105,width=600,height=95)

        # Department
           deep_label=Label(cc_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
           deep_label.grid(row=0,column=0,padx=10)

           deep_combo=ttk.Combobox(cc_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
           deep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
           deep_combo.current(0)
           deep_combo.grid(row=0,column=1,padx=2,pady=3)
        
        #Course
           course_label=Label(cc_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
           course_label.grid(row=0,column=2,padx=10)

           course_combo=ttk.Combobox(cc_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
           course_combo["values"]=("Select Course","FE","SE","TE","BE")
           course_combo.current(0)
           course_combo.grid(row=0,column=3,padx=2,pady=3)

        #Year
           year_label=Label(cc_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
           year_label.grid(row=1,column=0,padx=10)

           year_combo=ttk.Combobox(cc_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
           year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
           year_combo.current(0)
           year_combo.grid(row=1,column=1,padx=2,pady=3)

        #Semester
           Semester_label=Label(cc_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
           Semester_label.grid(row=1,column=2,padx=10)

           Semester_combo=ttk.Combobox(cc_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
           Semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6")
           Semester_combo.current(0)
           Semester_combo.grid(row=1,column=3,padx=2,pady=3)

        #Class Student Information
           class_Student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
           class_Student_frame.place(x=10,y=200,width=600,height=275)
        
        #StudentID
           studentID_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
           studentID_label.grid(row=0,column=0,padx=5)
           
           studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=19,font=("times new roman",12,"bold"))
           studentID_entry.grid(row=0,column=1,padx=5)

        #Student Name
           studentname_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
           studentname_label.grid(row=0,column=2,padx=5)
           
           studentname_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=19,font=("times new roman",12,"bold"))
           studentname_entry.grid(row=0,column=3,padx=5)

         #Class Division
           studentID_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
           studentID_label.grid(row=1,column=0,padx=5)
           
          # studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=19,font=("times new roman",12,"bold"))
          
          # studentID_entry.grid(row=1,column=1,padx=5,pady=5) 

           division_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),width=17,state="readonly")
           division_combo["values"]=("Select Division","A","B","C","D","E","F")
           division_combo.current(0)
           division_combo.grid(row=1,column=1,padx=2,pady=3)

         #Roll Number
           studentrollnumber_label=Label(class_Student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
           studentrollnumber_label.grid(row=1,column=2,padx=5)
           
           studentrollnumber_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=19,font=("times new roman",12,"bold"))
           studentrollnumber_entry.grid(row=1,column=3,padx=5)

         #Email
           studentemail_label=Label(class_Student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
           studentemail_label.grid(row=2,column=0,padx=5)
           
           studentemail_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=19,font=("times new roman",12,"bold"))
           studentemail_entry.grid(row=2,column=1,padx=5)

        #Phone Number
           studentnumber_label=Label(class_Student_frame,text="Mobile Number:",font=("times new roman",12,"bold"),bg="white")
           studentnumber_label.grid(row=2,column=2,padx=5)
           
           studentnumber_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=19,font=("times new roman",12,"bold"))
           studentnumber_entry.grid(row=2,column=3,padx=5)

         #Address
           studentaddress_label=Label(class_Student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
           studentaddress_label.grid(row=3,column=0,padx=5)
           
           studentaddress_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=19,font=("times new roman",12,"bold"))
           studentaddress_entry.grid(row=3,column=1,padx=5,pady=5) 

         #Teacher Name
           teachernamelabel=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
           teachernamelabel.grid(row=3,column=2,padx=5)
           
           teachername_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=19,font=("times new roman",12,"bold"))
           teachername_entry.grid(row=3,column=3,padx=5)

        #Gender
           studentgender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
           studentgender_label.grid(row=4,column=0,padx=5)
           
          # studentgender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=19,font=("times new roman",12,"bold"))
          # studentgender_entry.grid(row=4,column=1,padx=5)

           gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
           gender_combo["values"]=("Select Gender","Male","Female","Other")
           gender_combo.current(0)
           gender_combo.grid(row=4,column=1,padx=2,pady=3)

         #DOB
           studentDOB_label=Label(class_Student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
           studentDOB_label.grid(row=4,column=2,padx=5)
           
           studentDOB_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=19,font=("times new roman",12,"bold"))
           studentDOB_entry.grid(row=4,column=3,padx=5,pady=5) 

         #radio buttons
           self.var_radio1=StringVar()
           radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
           radiobtn1.grid(row=5,column=0)

           radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
           radiobtn2.grid(row=5,column=1)

         #btn Frame
           btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
           btn_frame.place(x=0,y=180,width=595,height=40)

           save_btn=Button(btn_frame,text="Save",command=self.add_data,width=16,font=("times new roman",12,"bold"),bg="black",fg="white")
           save_btn.grid(row=0,column=0)

           update_btn=Button(btn_frame,text="Update",command=self.update_data,width=15,font=("times new roman",12,"bold"),bg="black",fg="white")
           update_btn.grid(row=0,column=1)

           delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=15,font=("times new roman",12,"bold"),bg="black",fg="white")
           delete_btn.grid(row=0,column=2)

           reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=16,font=("times new roman",12,"bold"),bg="black",fg="white")
           reset_btn.grid(row=0,column=3)
         #btn frame2
           btn_frame1=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
           btn_frame1.place(x=0,y=218,width=595,height=30)

           takephotosample_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=33,font=("times new roman",12,"bold"),bg="black",fg="white")
           takephotosample_btn.grid(row=0,column=0)
           
           updatephotosample_btn=Button(btn_frame1,text="Update Photo Sample",width=33,font=("times new roman",12,"bold"),bg="black",fg="white")
           updatephotosample_btn.grid(row=0,column=1)

        #right label frame
           
           right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
           right_frame.place(x=640,y=10,width=630,height=500)

           img_right=Image.open(r"E:\Face Recognition System\photos\sd1.jpeg")
           img_right=img_right.resize((630,130))
           self.photoimg_right=ImageTk.PhotoImage(img_right)
    
           f_lbl4=Label(right_frame,image=self.photoimg_right)
           f_lbl4.place(x=0,y=0,width=630,height=100)

        #==============Search System================

           search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
           search_frame.place(x=10,y=105,width=610,height=58)

           search_label=Label(search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="white")
           search_label.grid(row=0,column=0,padx=5)

           search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
           search_combo["values"]=("Select","Roll_No","Phone_No")
           search_combo.current(0)
           search_combo.grid(row=0,column=1,padx=2,pady=3)

           search_entry=ttk.Entry(search_frame,width=17,font=("times new roman",12,"bold"))
           search_entry.grid(row=0,column=2,padx=3,pady=5) 

           search_btn=Button(search_frame,text="Search",width=10,font=("times new roman",12,"bold"),bg="black",fg="white")
           search_btn.grid(row=0,column=3,padx=2)

           showAll_btn=Button(search_frame,text="Show All",width=10,font=("times new roman",12,"bold"),bg="black",fg="white")
           showAll_btn.grid(row=0,column=4)

        #===============Table Frame================
           table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
           table_frame.place(x=10,y=170,width=610,height=300)

           scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
           scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

           self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gen","dob","email","phone","add","teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
           
           scroll_x.pack(side=BOTTOM,fill=X)
           scroll_y.pack(side=RIGHT,fill=Y)

           scroll_x.config(command=self.student_table.xview)
           scroll_y.config(command=self.student_table.yview)

           self.student_table.heading("dep",text="Department")
           self.student_table.heading("course",text="Course")
           self.student_table.heading("year",text="Year")
           self.student_table.heading("sem",text="Semester")
           self.student_table.heading("id",text="StudentID")
           self.student_table.heading("name",text="Name")
           self.student_table.heading("div",text="Division")
           self.student_table.heading("roll",text="Roll Number")
           self.student_table.heading("gen",text="Gender")
           self.student_table.heading("dob",text="DOB")
           self.student_table.heading("email",text="Email")
           self.student_table.heading("phone",text="Phone")
           self.student_table.heading("add",text="Address")
           self.student_table.heading("teacher",text="Teacher")
           self.student_table.heading("Photo",text="PhotoSampleStatus")
           self.student_table["show"]="headings"

           self.student_table.column("dep",width=100)
           self.student_table.column("course",width=100)
           self.student_table.column("year",width=100)
           self.student_table.column("sem",width=100)
           self.student_table.column("id",width=100)
           self.student_table.column("name",width=100)
           self.student_table.column("div",width=100)
           self.student_table.column("roll",width=100)
           self.student_table.column("gen",width=100)
           self.student_table.column("dob",width=100)
           self.student_table.column("email",width=100)
           self.student_table.column("phone",width=100)
           self.student_table.column("add",width=100)
           self.student_table.column("teacher",width=100)
           self.student_table.column("Photo",width=120)

           self.student_table.pack(fill=BOTH,expand=1)
           self.student_table.bind("<ButtonRelease>",self.get_Cursor)
           self.fetch_data()

      #================Function Declaration====================

     def add_data(self):
      if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error","All Fields are required")
      else:
            
          # messagebox.showinfo("Success","Welcome")
               conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            

                                                                                                               self.var_dep.get(),
                                                                                                               self.var_course.get(),
                                                                                                               self.var_year.get(),
                                                                                                               self.var_semester.get(),
                                                                                                               self.var_std_id.get(),
                                                                                                               self.var_std_name.get(),
                                                                                                               self.var_div.get(),
                                                                                                               self.var_roll.get(),
                                                                                                               self.var_gender.get(),
                                                                                                               self.var_dob.get(),
                                                                                                               self.var_email.get(),
                                                                                                               self.var_phone.get(),
                                                                                                               self.var_address.get(),
                                                                                                               self.var_teacher.get(),
                                                                                                               self.var_radio1.get()

                                                                                                            ))
              
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox("sucess","done")
            
        #===================Fetch Data==============
     def fetch_data(self):
               conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
               my_cursor=conn.cursor()
               my_cursor.execute("Select * from Student")
               data=my_cursor.fetchall()

               if len(data)!=0:
                  self.student_table.delete(*self.student_table.get_children())
                  for i in data:
                      self.student_table.insert("",END,values=i)
                  conn.commit()
               conn.close()    


       #==================get Cursor========================
     def get_Cursor(self,event=""):
           cursor_focus=self.student_table.focus()
           content=self.student_table.item(cursor_focus)
           data=content["values"]

           self.var_dep.set(data[0]),
           self.var_course.set(data[1]),
           self.var_year.set(data[2]),
           self.var_semester.set(data[3]),
           self.var_std_id.set(data[4]),
           self.var_std_name.set(data[5]),
           self.var_div.set(data[6]),
           self.var_roll.set(data[7]),
           self.var_gender.set(data[8]),
           self.var_dob.set(data[9]),
           self.var_email.set(data[10]),
           self.var_phone.set(data[11]),
           self.var_address.set(data[12]),
           self.var_teacher.set(data[13]),
           self.var_radio1.set(data[14])

    # ===========Update Function============
     def update_data(self):
            if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error","All Fields are required")
            else:
                  try:
                        Update=messagebox.askyesno("Update","Do you want to Update this details")
                        if Update>0:
                              conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                              my_cursor=conn.cursor()
                              my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                    
                                                                                                                                                                                                                   self.var_dep.get(),
                                                                                                                                                                                                                   self.var_course.get(),
                                                                                                                                                                                                                   self.var_year.get(),
                                                                                                                                                                                                                   self.var_semester.get(),
                                                                                                                                                                                                                   self.var_std_name.get(),
                                                                                                                                                                                                                   self.var_div.get(),
                                                                                                                                                                                                                   self.var_roll.get(),
                                                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                                                   self.var_dob.get(),
                                                                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                                                                   self.var_phone.get(),
                                                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                                                   self.var_teacher.get(),
                                                                                                                                                                                                                   self.var_radio1.get(),
                                                                                                                                                                                                                   self.var_std_id.get(),

                                                                                                                                                                                                               ))
                        else:
                              if not Update:
                                    return
                        messagebox.showinfo("Success","Student Details Successfully updated")
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                  except Exception as es:
                       messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        #=========Delete Function================
     def delete_data(self):
           if self.var_std_id.get()=="":
                 messagebox.showerror("Error","Student ID must be Required")
           else:
                 try:
                       delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student")
                       if delete>0:
                             conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                             my_cursor=conn.cursor()
                             sql="delete from student where Student_id=%s"
                             val=(self.var_std_id.get(),)
                             my_cursor.execute(sql,val)
                       else:
                             if not delete:
                                   return
                       conn.commit()
                       self.fetch_data()
                       conn.close()
                       messagebox.showinfo("Delete","Successfully Deleted Student Details")
                 except Exception as es:
                       messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   

   
         #============rest button=============
     def reset_data(self):
           self.var_dep.set("Select Department")
           self.var_course.set("Select Course")
           self.var_year.set("Select Year")
           self.var_semester.set("Select Semester")
           self.var_std_id.set("")
           self.var_std_name.set("")
           self.var_div.set("Select Division")
           self.var_roll.set("")
           self.var_gender.set("Select Gender")
           self.var_dob.set("")
           self.var_email.set("")
           self.var_phone.set("")
           self.var_address.set("")
           self.var_teacher.set("")
           self.var_radio1.set("")


      #=============Generate Data Set or Take Photo Sample===============
     def generate_dataset(self):
           if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
              messagebox.showerror("Error","All Fields are required")
           else:
                  try:
                      conn=mysql.connector.connect(host="localhost",username="root",password="root",database="face_recognizer")
                      my_cursor=conn.cursor()
                      my_cursor.execute("Select * from student")
                      myresult=my_cursor.fetchall()
                      id=0
                      for x in myresult:
                            id+=1
                      my_cursor.execute("Update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                    
                                                                                                                                                                                                                   self.var_dep.get(),
                                                                                                                                                                                                                   self.var_course.get(),
                                                                                                                                                                                                                   self.var_year.get(),
                                                                                                                                                                                                                   self.var_semester.get(),
                                                                                                                                                                                                                   self.var_std_name.get(),
                                                                                                                                                                                                                   self.var_div.get(),
                                                                                                                                                                                                                   self.var_roll.get(),
                                                                                                                                                                                                                   self.var_gender.get(),
                                                                                                                                                                                                                   self.var_dob.get(),
                                                                                                                                                                                                                   self.var_email.get(),
                                                                                                                                                                                                                   self.var_phone.get(),
                                                                                                                                                                                                                   self.var_address.get(),
                                                                                                                                                                                                                   self.var_teacher.get(),
                                                                                                                                                                                                                   self.var_radio1.get(),
                                                                                                                                                                                                                   self.var_std_id.get()==id+1

                                                                                                                                                                                                               ))
                      conn.commit() 
                      self.fetch_data()
                      self.reset_data()
                      conn.close()    


               #===================Load Predifiend data on face frontal from opencv=================
                      face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                      def face_cropped(img):
                            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                            faces=face_classifier.detectMultiScale(gray,1.3,5)


                            for(x,y,w,h) in faces:
                                  face_cropped=img[y:y+h,x:x+w]
                                  return face_cropped
                            
                      cap=cv2.VideoCapture(0)
                      img_id=0
                      while True:
                            ret,my_frame=cap.read()
                            if face_cropped(my_frame) is not None:
                                  img_id+=1
                                  face=cv2.resize(face_cropped(my_frame),(300,300))
                                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                  file_namepath="data/user."+str(id)+"."+str(img_id)+".jpg"
                                  cv2.imwrite(file_namepath,face)
                                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                  cv2.imshow("Cropped Face",face)

                            if cv2.waitKey(1)==13 or int(img_id)==100:
                                  break
                      cap.release()
                      cv2.destroyAllWindows()
                      messagebox.showinfo("Result","Generating Data Sets Completed!!!!")

                  except Exception as es:
                       messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


if __name__ == "__main__":
         root=Tk()
         obj=Student(root)
         root.mainloop()