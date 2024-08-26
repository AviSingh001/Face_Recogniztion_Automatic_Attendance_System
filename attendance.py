from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import mysql.connector
import os
import csv
from tkinter import filedialog

mydata=[]

class StudentAttendance:
     def __init__(self,root):
           self.root=root
           self.root.geometry("1350x700+0+0")
           self.root.title("Face Recognition System")


          #========Text Variables===============
           self.var_atten_id=StringVar()
           self.var_atten_roll=StringVar()
           self.var_atten_name=StringVar()
           self.var_atten_dep=StringVar()
           self.var_atten_time=StringVar()
           self.var_atten_date=StringVar()
           self.var_atten_attendance=StringVar()


           #========Images=========================

           img=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           img=img.resize((675,200))
           self.photoimg=ImageTk.PhotoImage(img)
    
           f_lbl=Label(self.root,image=self.photoimg)
           f_lbl.place(x=0,y=0,width=675,height=200)

           img1=Image.open(r"E:\Face Recognition System\photos\logo.jpeg")
           img1=img1.resize((675,200))
           self.photoimg1=ImageTk.PhotoImage(img1)
    
           f_lbl1=Label(self.root,image=self.photoimg1)
           f_lbl1.place(x=675,y=0,width=675,height=200)

           title_lbl=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="red")
           title_lbl.place(x=0,y=200,width=1350,height=40)

           main_frame=Frame(self.root,bd=2,bg="white")
           main_frame.place(x=0,y=240,width=1350,height=460)

           left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
           left_frame.place(x=5,y=5,width=670,height=450)

           img_left=Image.open(r"E:\Face Recognition System\photos\att.jpeg")
           img_left=img_left.resize((667,100))
           self.photoimg_left=ImageTk.PhotoImage(img_left)
    
           f_lbl3=Label(left_frame,image=self.photoimg_left)
           f_lbl3.place(x=0,y=5,width=667,height=100)

           left_iniside_frame=Frame(left_frame,bd=2,bg="white",relief=RIDGE)
           left_iniside_frame.place(x=5,y=115,width=657,height=200)

           #labels & Entries
           #attendance ID
           attendanceID_label=Label(left_iniside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
           attendanceID_label.grid(row=0,column=0,padx=5,pady=5)
           
           attendanceID_entry=ttk.Entry(left_iniside_frame,width=19,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
           attendanceID_entry.grid(row=0,column=1,padx=3,pady=5)

           #Roll
           roll_label=Label(left_iniside_frame,text="Roll:",font=("times new roman",12,"bold"),bg="white")
           roll_label.grid(row=0,column=2,padx=5,pady=5)
           
           roll_entry=ttk.Entry(left_iniside_frame,width=19,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
           roll_entry.grid(row=0,column=3,padx=3,pady=5)

           #Name
           Name_label=Label(left_iniside_frame,text="Name:",font=("times new roman",12,"bold"),bg="white")
           Name_label.grid(row=1,column=0,padx=5,pady=5)
           
           Name_entry=ttk.Entry(left_iniside_frame,width=19,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
           Name_entry.grid(row=1,column=1,padx=3,pady=5)

           #Department
           department_label=Label(left_iniside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
           department_label.grid(row=1,column=2,padx=5,pady=5)
           
           department_entry=ttk.Entry(left_iniside_frame,width=19,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
           department_entry.grid(row=1,column=3,padx=3,pady=5)

             #Time
           Time_label=Label(left_iniside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
           Time_label.grid(row=2,column=0,padx=5,pady=5)
           
           Time_entry=ttk.Entry(left_iniside_frame,width=19,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
           Time_entry.grid(row=2,column=1,padx=3,pady=5)

           #Date
           Date_label=Label(left_iniside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
           Date_label.grid(row=2,column=2,padx=5,pady=5)
           
           Name_entry=ttk.Entry(left_iniside_frame,width=19,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
           Name_entry.grid(row=2,column=3,padx=3,pady=5)

           #Attendance
           Attendance_label=Label(left_iniside_frame,text="Attendance Status:",font=("times new roman",12,"bold"),bg="white")
           Attendance_label.grid(row=3,column=0,padx=5,pady=5)

           self.atten_combo=ttk.Combobox(left_iniside_frame,font=("times new roman",12,"bold"),textvariable=self.var_atten_attendance,width=17,state="readonly")
           self.atten_combo["values"]=("Status","Present","Absent")
           self.atten_combo.current(0)
           self.atten_combo.grid(row=3,column=1,padx=3,pady=5)

           #btn Frame
           btn_frame=Frame(left_iniside_frame,bd=2,relief=RIDGE,bg="white")
           btn_frame.place(x=0,y=140,width=657,height=36)

           Importcsv_btn=Button(btn_frame,text="Import csv",command=self.importscv,width=17,font=("times new roman",12,"bold"),bg="black",fg="white")
           Importcsv_btn.grid(row=0,column=0)

           Exportcsv_btn=Button(btn_frame,text="Export csv",command=self.exportcsv,width=17,font=("times new roman",12,"bold"),bg="black",fg="white")
           Exportcsv_btn.grid(row=0,column=1)

           update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",12,"bold"),bg="black",fg="white")
           update_btn.grid(row=0,column=2)

           reset_btn=Button(btn_frame,text="Reset",width=17,command=self.restdata,font=("times new roman",12,"bold"),bg="black",fg="white")
           reset_btn.grid(row=0,column=3)


           right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
           right_frame.place(x=680,y=5,width=665,height=450)

           table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
           table_frame.place(x=5,y=115,width=655,height=310)

           img_right=Image.open(r"E:\Face Recognition System\photos\att1.jpeg")
           img_right=img_right.resize((665,100))
           self.photoimg_right=ImageTk.PhotoImage(img_right)
    
           f_lbl4=Label(right_frame,image=self.photoimg_right)
           f_lbl4.place(x=0,y=5,width=665,height=100)

        #==================scrollbar==============
           scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
           scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

           self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

           scroll_x.pack(side=BOTTOM,fill=X)
           scroll_y.pack(side=RIGHT,fill=Y)

           scroll_x.config(command=self.AttendanceReportTable.xview)
           scroll_y.config(command=self.AttendanceReportTable.yview)

           self.AttendanceReportTable.heading("id",text="Attendance ID")
           self.AttendanceReportTable.heading("roll",text="Roll")
           self.AttendanceReportTable.heading("name",text="Name")
           self.AttendanceReportTable.heading("department",text="Department")
           self.AttendanceReportTable.heading("time",text="Time")
           self.AttendanceReportTable.heading("date",text="Date")
           self.AttendanceReportTable.heading("attendance",text="Attendance Status")

           self.AttendanceReportTable["show"]="headings"
           
           self.AttendanceReportTable.column("id",width=100)
           self.AttendanceReportTable.column("roll",width=100)
           self.AttendanceReportTable.column("name",width=100)
           self.AttendanceReportTable.column("department",width=100)
           self.AttendanceReportTable.column("time",width=100)
           self.AttendanceReportTable.column("date",width=100)
           self.AttendanceReportTable.column("attendance",width=100)

           self.AttendanceReportTable.pack(fill=BOTH,expand=1)
           self.AttendanceReportTable.bind("<ButtonRelease>",self.getcursor)
          # sel.AttendanceReportTable

          #==============Fetch Data (import csv)=================

     def fetchdata(self,rows):
            self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
            for i in rows:
                   self.AttendanceReportTable.insert("",END,values=i)


     def importscv(self):
              global mydata
              mydata.clear()
              fin=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
              with open(fin) as myfile:
                     csvread=csv.reader(myfile,delimiter=",")
                     for i in csvread:
                            mydata.append(i)
                     self.fetchdata(mydata)

           #==============Exportcsv================
     def exportcsv(self):
            try:
                   if len(mydata)<1:
                          messagebox.showerror("No Data","No Data Found to Export",parent=self.root)
                          return False
                   fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
                   with open(fin,mode="w",newline="") as myfile:
                          exp_write=csv.writer(myfile,delimiter=",")
                          for i in mydata:
                                 exp_write.writerow(i)
                          messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fin)+" Successfully")
            except Exception as es:
                   messagebox.showerror("Error",f"Due To: {str(es)}",parent=self.root)

         #===================Get Cursor=================
      
     def getcursor(self,event=""):
            cursor_row=self.AttendanceReportTable.focus()
            content=self.AttendanceReportTable.item(cursor_row)
            rows=content['values']
            self.var_atten_id.set(rows[0])
            self.var_atten_roll.set(rows[1])
            self.var_atten_name.set(rows[2])
            self.var_atten_dep.set(rows[3])
            self.var_atten_time.set(rows[4])
            self.var_atten_date.set(rows[5])
            self.var_atten_attendance.set(rows[6])

        #=====================Reset Data==================

     def restdata(self):
            self.var_atten_id.set("")
            self.var_atten_roll.set("")
            self.var_atten_name.set("")
            self.var_atten_dep.set("")
            self.var_atten_time.set("")
            self.var_atten_date.set("")
            self.var_atten_attendance.set("")
            

            

                            

            











if __name__ == "__main__":
         root=Tk()
         obj=StudentAttendance(root)
         root.mainloop()