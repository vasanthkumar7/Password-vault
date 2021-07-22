import tkinter
from tkinter import *
from cryptography.fernet import Fernet
import cv2
import numpy as np
import face_recognition
from cryptography.fernet import Fernet
from PIL import ImageTk,Image
import pyperclip as pc


root=Tk()
root.title("Password vault")
p1 = PhotoImage(file = 'security.png')
root.iconphoto(False, p1)

img = ImageTk.PhotoImage(Image.open("lock.png").resize((200,200)))
img1 = ImageTk.PhotoImage(Image.open("copy.png").resize((20,20)))

def list_tostring(a):
    l=""
    for i in a:
        l+=str(i)+" "
    return l

def save_faces():
    global t4
    cap = cv2.VideoCapture(0)
    while True:
        img = cap.read()
        img = np.array(img[1], dtype=np.uint8)
        img2=np.array(img[1], dtype=np.uint8)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('img', img)
        if cv2.waitKey(1)& 0xFF == ord('s'):
            cv2.imwrite('test1.jpg',img)
            break
    cap.release()
    cv2.destroyAllWindows()
    t4.grid(row=4,column=0)

def save_done():
    global t4,t42,t1,t2,t3,t5,glbkey,name,t0
    known_image = face_recognition.load_image_file("test1.jpg")
    biden_encoding = face_recognition.face_encodings(known_image)[0]
    ass=list_tostring(list(biden_encoding))
    biden_encoding=list(map(float,ass.split()))
    biden_encoding=np.array(biden_encoding)
    f=open("faces.txt","a")
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encMessage = fernet.encrypt(ass.encode())
    fgh=t42.get()
    glbkey=key
    encMessage2 = fernet.encrypt(fgh.encode())
    f.write(str(key)+" "+str(encMessage)+" "+str(encMessage2)+" \n")
    fsda=open("details/"+str(encMessage2)+".txt","a")
    fsda.close()
    t4.grid_forget()
    
    
def welcome_page(message,key):
    global t5,t51,t52,t53,t54,t1,t2,t3,t4,name,glbkey,whats1,t0
    glbkey=key
    name=message
    fernet = Fernet(glbkey)
    decMessage2 = fernet.decrypt(bytes(message[2:len(message)-1],'utf-8')).decode()
    fernet = Fernet(key)
    glbkey=key
    f5=open("details/"+name+".txt","r")
    f51=f5.read().split("\n")
    t53.delete(0,END)
    whats1=f51[:len(f51)-1]
    if f51[0]!="":
        for i in f51:
            i=i.split()
            if i==[]:
                break
            decMessage = fernet.decrypt(bytes(i[0][2:len(i[0])-1],'utf-8')).decode()
            t53.insert(END,decMessage)
    encMessage = fernet.encrypt(message.encode())
    t51.configure(text="Welcome "+decMessage2,font=("arial",30))
    t4.grid_forget()
    t1.grid_forget()
    t2.grid_forget()
    t3.grid_forget()
    t0.grid_forget()
    t5.grid(row=0,column=0)

def add_to_profile():
    global name,glbkey
    global t5,t51,t52,t53,t54,t1,t2,t3,t4,t55,t551,t552,t553,t554,t556,t557
    t54.grid_forget()
    clear_all()
    t55.grid(row=3,column=0)


def save_to_profile():
    global name,glbkey
    global t5,t51,t52,t53,t54,t1,t2,t3,t4,t55,t551,t552,t553,t554,t556,t557
    global whats1
    fernet = Fernet(glbkey)
    f=open("details/"+name+".txt","a")
    enc1=fernet.encrypt(t552.get().encode())
    enc2=fernet.encrypt(t554.get().encode())
    enc3=fernet.encrypt(t556.get().encode())
    t53.insert(END,t552.get())
    whats1.append(str(enc1)+" "+str(enc2)+" "+str(enc3)) 
    f.write(str(enc1)+" "+str(enc2)+" "+str(enc3)+" \n")
    t55.grid_forget()

whats1=None
def copythem(msg):
    pc.copy(msg)

def viewpassword():
    global name,glbkey
    global t5,t51,t52,t53,t54,t1,t2,t3,t4,t55,t551,t552,t553,t554,t556,t557,t541,t542,t543,whats1
    global t541,t542,t543,t544,t545,t546,t547,t548,img1
    t55.grid_forget()
    clear_all()
    i=t53.curselection()[0]
    fernet = Fernet(glbkey)
    ghs=whats1[i].split()
    
    decMessage = fernet.decrypt(bytes(ghs[0][2:len(ghs[0])-1],'utf-8')).decode()
    decMessage1 = fernet.decrypt(bytes(ghs[1][2:len(ghs[1])-1],'utf-8')).decode()
    decMessage2 = fernet.decrypt(bytes(ghs[2][2:len(ghs[2])-1],'utf-8')).decode()
    b1=Button(t54,image=img1,command=lambda:copythem(decMessage)).grid(row=0,column=3,padx=10)
    b1=Button(t54,image=img1,command=lambda:copythem(decMessage1)).grid(row=1,column=3,padx=10)
    b1=Button(t54,image=img1,command=lambda:copythem(decMessage2)).grid(row=2,column=3,padx=10)
    t542.delete(0, END)
    t544.delete(0, END)
    t546.delete(0, END)
    t542.insert(0,decMessage)
    t544.insert(0,decMessage1)
    t546.insert(0,decMessage2)
    t54.grid(row=3,column=0,padx=5,pady=5)
    

def back_home():
    global t4,t42,t1,t2,t3,t5,t0
    t5.grid_forget()
    clear_all()

    
    t1.grid(row=0,column=0,padx=10,pady=10)
    t0.grid(row=1,column=0,padx=10,pady=10)
    t2.grid(row=2,column=0,padx=10,pady=10)
    t3.grid(row=3,column=0,padx=10,pady=10)
    
    

def delete_password():
    global whats1
    global name,glbkey
    global t5,t51,t52,t53,t54,t1,t2,t3,t4,t55,t551,t552,t553,t554,t556,t557,t541,t542,t543,whats1
    clear_all()
    t55.grid_forget()
    i=t53.curselection()[0]
    whats1=whats1[:i]+whats1[i+1:]

    f=open("details/"+name+".txt","w")
    for i in whats1:
        f.write(i+" \n")

    t54.grid_forget()
    t55.grid_forget()
    t53.delete(ACTIVE)
    
def check_facematch():
    global t5,name
    cap = cv2.VideoCapture(0)
    while True:
        img = cap.read()
        img = np.array(img[1], dtype=np.uint8)
        img2=np.array(img[1], dtype=np.uint8)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('img', img)
        if cv2.waitKey(1)& 0xFF == ord('s'):
            cv2.imwrite('test1.jpg',img)
            break
    cap.release()
    cv2.destroyAllWindows() 
    f=open("faces.txt","r")
    ff=f.read().split("\n")
    for i in ff:
        j=i.split()
        if j==[]:
            break
        jkl=bytes(j[0][2:len(j[0])-1],'utf-8')
        fernet = Fernet(jkl)
        decMessage = fernet.decrypt(bytes(j[1][2:len(j[1])-1],'utf-8')).decode()
        decMessage2 = fernet.decrypt(bytes(j[2][2:len(j[2])-1],'utf-8')).decode()
        bdg=list(map(float,decMessage.split()))
        bdg=np.array(bdg)
        unknown_image = face_recognition.load_image_file("test1.jpg")
        unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
        results = face_recognition.compare_faces([bdg], unknown_encoding)
        if results[0]:
            name=decMessage2
            welcome_page(j[2],jkl)

name=None
glbkey=None

def clear_all():
    global t42 ,t552,t554,t556,t542,t544,t546,t54,t55

    t54.grid_forget()
    t55.grid_forget()
    t42.delete(0, END)
    t542.delete(0, END)
    t544.delete(0, END)
    t546.delete(0, END)
    t552.delete(0, END)
    t554.delete(0, END)
    t556.delete(0, END)

    
t0=Label(root,image=img)
t0.grid(row=1,column=0,pady=10,padx=10)
t1=Label(root,text="Password Vault",font=("arial",20))
t1.grid(row=0,column=0,padx=10,pady=10)

t2=Button(root,text="Setup profile",font=("arial",20),command=save_faces,width=20,bg="black",fg="white")
t2.grid(row=2,column=0,padx=10,pady=10)

t3=Button(root,text="Check your password",font=("arial",20),command=check_facematch,width=20,bg="black",fg="white")
t3.grid(row=3,column=0,padx=10,pady=10)

t4=Frame(root)

t41=Label(t4,text="Enter your name :",font=("arial",15))
t41.grid(row=0,column=0,padx=10,pady=10)
t42=Entry(t4,font=("arial",15))
t42.grid(row=0,column=1,padx=10,pady=10)
t43=Button(t4,text="Enter",command=save_done,font=("arial",15))
t43.grid(row=1,column=0,padx=10,pady=10,columnspan=2)

t5=Frame(root)

t51=Label(t5,text="")
t51.grid(row=0,column=0,padx=10,pady=10)

t52=Frame(t5)
t521=Button(t52,text="Add",command=add_to_profile,font=("arial",15),bg="black",fg="white")
t521.grid(row=0,column=0,padx=10,pady=10)

t522=Button(t52,text="View",command=viewpassword,font=("arial",15),bg="black",fg="white")
t522.grid(row=0,column=1,padx=10,pady=10)

t523=Button(t52,text="Back",command=back_home,font=("arial",15),bg="black",fg="white")
t523.grid(row=0,column=2,padx=10,pady=10)

t524=Button(t52,text="Delete",command=delete_password,font=("arial",15),bg="black",fg="white")
t524.grid(row=0,column=3,padx=10,pady=10)

t52.grid(row=1,column=0,pady=10)

t53=Listbox(t5,height=8,width=40,font=10)
t53.grid(row=2,column=0,padx=10,pady=10)

t54=Frame(t5)

t541=Label(t54,text="Link: ",font=("arial",15)).grid(row=0,column=0)
t542=Entry(t54,font=("arial",15))
t542.grid(row=0,column=1,pady=10)

t543=Label(t54,text="Username: ",font=("arial",15)).grid(row=1,column=0)
t544=Entry(t54,font=("arial",15))
t544.grid(row=1,column=1,pady=10)

t545=Label(t54,text="Password: ",font=("arial",15)).grid(row=2,column=0)
t546=Entry(t54,font=("arial",15))
t546.grid(row=2,column=1,pady=10)


t55=Frame(t5)
t551=Label(t55,text="Link: ",font=("arial",15)).grid(row=0,column=0)
t552=Entry(t55,font=("arial",15))
t552.grid(row=0,column=1,pady=10)

t553=Label(t55,text="Username: ",font=("arial",15)).grid(row=1,column=0)
t554=Entry(t55,font=("arial",15))
t554.grid(row=1,column=1,pady=10)

t555=Label(t55,text="Password: ",font=("arial",15)).grid(row=2,column=0)
t556=Entry(t55,font=("arial",15))
t556.grid(row=2,column=1,pady=10)

t557=Button(t55,text="Enter",command=save_to_profile).grid(row=3,column=0,columnspan=2)



root.mainloop()
