from tkinter import *
from tkinter import messagebox
import tkinter.filedialog
import os
import sys
pyexec = sys.executable
root=Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def open():
    print("Login Success")
    root.destroy()
    os.system('python GUI.py')

def signin():
    open()


img=PhotoImage(file='images.png')
Label(root,image=img,bg='white').place(x=100,y=100)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='Sing in',fg='#57a1f8',bg='white',font=('Microsoft VaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
################------------------------------------------------------------------------------------------- 
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')

user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft VaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)
#############------------------------------------------------------------
def on_enter(e):
    passwd.delete(0,'end')

def on_leave(e):
    name=passwd.get()
    if name=='':
        passwd.insert(0,'Password')

passwd=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft VaHei UI Light',11))
passwd.place(x=30,y=150)
passwd.insert(0,'Password')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)
#############################################################################################

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
Label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft VaHei UI Light',9))
Label.place(x=75,y=270)

sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signin)
sign_up.place(x=215,y=270)

root.mainloop()