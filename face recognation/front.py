from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
from student import Student
# from self import self

class Face_recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")
        
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
        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE                   ",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=50)
        
        
        #first button
        img5=Image.open("stu.jpg")
        img5=img5 .resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(self.root,image=self.photoimg5,command=self.student_inf,cursor="hand2")
        b1.place(x=180,y=180,width=200,height=200)
        
        b1=Button(self.root,text="students details",command=self.student_inf,cursor="hand2",font=("Arial",15,"bold"),bg="black",fg="white")
        b1.place(x=180,y=180,width=200,height=40)
        
        #second button
        img6=Image.open("image1.jpg")
        img6=img6 .resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(self.root,image=self.photoimg6,cursor="hand2")
        b1.place(x=580,y=180,width=200,height=200)
        
        b1=Button(self.root,text="app details",cursor="hand2",font=("Arial",15,"bold"),bg="black",fg="white")
        b1.place(x=580,y=180,width=200,height=40)
        
        #third button
        img7=Image.open("romit.jpg")
        img7=img7 .resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(self.root,image=self.photoimg7,cursor="hand2")
        b1.place(x=980,y=180,width=200,height=200)
        
        b1=Button(self.root,text="my details",cursor="hand2",font=("Arial",15,"bold"),bg="black",fg="white")
        b1.place(x=980,y=180,width=200,height=40)
        
        #fourth button
        img8=Image.open("debu.jpg")
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(self.root,image=self.photoimg8,cursor="hand2")
        b1.place(x=580,y=400,width=200,height=200)
        
        b1=Button(self.root,text="EXIT",cursor="hand2",font=("Arial",15,"bold"),bg="black",fg="white")
        b1.place(x=580,y=400,width=200,height=40)
        
        
        #function button
    def student_inf(self):
        self.new_window=Toplevel(self.root)
        self.application=Student(self.new_window)


if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_System(root)
    root.mainloop()