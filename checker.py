from tkinter import *
from tkinter import messagebox
import parser
import lexer

root=Tk()
root.title('Checking')
root.geometry('700x400')
root.configure(bg="#dae6f6")
#c=Canvas(bg="gray16",height=380,width=50)
#filename=PhotoImage(file='C:\\Users\\ExperBook\\Downloads\\images.png')
#backgrounlabel=Label(image=filename)
#backgrounlabel.place(x=0,y=0,relwidth=1,relheight=1)
#c.pack()

heading=Label(root,text="Checker",font=("Trebuchet MS",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

enter_text=Entry(root,justify="right",width=60,font=('poppins',25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

button=Button(root,text="check",font=("arial",20,"bold"),fg="white",bg="green")
button.pack()

root.mainloop()

res = parser.parse("إياك نعبد وإياك نستعين")