from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
# from self import self

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("student system")
        
        #for first image
        img=Image.open("download.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=-10,y=0,width=500,height=130)
        
        #for second image
        img2=Image.open("download.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=490,y=0,width=500,height=130)
        
        #for third image
        img3=Image.open("download.jpg")
        img3=img3 .resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        f_lbl=Label(self.root,image=self.photoimg3)
        f_lbl.place(x=970,y=0,width=400,height=130)
        
        #background image
        img4=Image.open("image1.jpg")
        img4=img4 .resize((1530,720),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=130,width=1530,height=720)
        
        #title 
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM                  ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=100)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=90,width=1500,height=500)
        
        #left label frame
        Left_frame=LabelFrame(main_frame,bd=1,bg="white",relief=RAISED,text="students details",font=("Arial",20))
        Left_frame.place(x=0,y=0,width=600,height=480)
        
        img_left=Image.open("download.jpg")
        img_left=img_left .resize((590,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=2,y=0,width=590,height=130)
        
        #current course
        current_course_frame=LabelFrame(Left_frame,bd=1,bg="white",relief=RAISED,text="Student Information",font=("Arial",13))
        current_course_frame.place(x=5,y=140,width=595,height=200)
        
        #Name level
        name_label=Label(current_course_frame,text="Name",font=("times new romain",10,"bold"),bg="light green")
        name_label.grid(row=0,column=0,pady=10,padx=0)
        
        name_combo=ttk.Entry(current_course_frame,text="",font=("times new romain",10,"bold"),state="writeonly")
        name_combo.grid(row=0,column=1,padx=2)
      
        #id level
        Id_label=Label(current_course_frame,text="ID",font=("times new romain",10,"bold"),bg="light green")
        Id_label.grid(row=0,column=2,padx=2)
        
        Id_combo=ttk.Entry(current_course_frame,text="ID",font=("times new romain",10,"bold"),state="writeonly",width=24)
        Id_combo.grid(row=0,column=3,padx=2)
        
        #radio buttons
        Radiobutton1=ttk.Radiobutton(current_course_frame,text="Take a photo sample",value="yes")
        Radiobutton1.grid(row=1,column=1,pady=30)
       
        Radiobutton2=ttk.Radiobutton(current_course_frame,text="Don't Take a photo sample",value="yes")
        Radiobutton2.grid(row=1,column=3,pady=30)
        
        #button frame
        Button_frame=Frame(current_course_frame,bd=3,relief=RIDGE,bg="white")
        Button_frame.place(x=-3,y=130,width=600,height=49)
        
        save_button=Button(Button_frame,text="Save",width=10,font=("Arial",17,"bold"),bg="light gray")
        save_button.grid(row=0,column=0)
        
        update_button=Button(Button_frame,text="Update",width=10,font=("Arial",17,"bold"),bg="light gray")
        update_button.grid(row=0,column=1)
        
        delete_button=Button(Button_frame,text="Delete",width=10,font=("Arial",17,"bold"),bg="light gray")
        delete_button.grid(row=0,column=2)
        
        reset_button=Button(Button_frame,text="Reset",width=10,font=("Arial",17,"bold"),bg="light gray")
        reset_button.grid(row=0,column=3) 
       
       #right label frame 
        right_frame=LabelFrame(main_frame,bd=1,bg="white",relief=SUNKEN,text="students details",font=("monospaced ",20))
        right_frame.place(x=599,y=0,width=800,height=480)
        
        img_right=Image.open("stu.jpg")
        img_right=img_right .resize((750,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)
        
        f_lbl=Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=750,height=130)
        
        #search system frame
        search_frame=LabelFrame(right_frame,bd=1,bg="white",relief=FLAT,text="Search Information",font=("Arial",13))
        search_frame.place(x=2,y=140,width=755,height=70)
        
        #search label
        search_label=Label(search_frame,text="Search by ID*",font=("times new romain",11,"bold"),bg="light green")
        search_label.grid(row=0,column=0,pady=10,padx=5,sticky=W)
        
        search_combo=ttk.Entry(search_frame,font=("times new romain",11,"bold"),state="writeonly",width=20)
        search_combo.grid(row=0,column=1,padx=2)
        
        #search button
        search_button=Button(search_frame,text="Search",width=15,font=("Arial",9,"bold"),bg="light gray")
        search_button.grid(row=0,column=2)
        
        table_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=2,y=205,width=755,height=240)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Name","Id","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.student_table.xview)#view the table name
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("Name",text="NAME")
        self.student_table.heading("Id",text="Id")
        self.student_table.heading("photo",text="PHOTO")
        self.student_table["show"]="headings"
        
        self.student_table.pack(fill=BOTH,expand=1)
        
        
        
        
        
        
        
if __name__ == "__main__":
  root=Tk()
  obj=Student(root)
  root.mainloop()
  
  