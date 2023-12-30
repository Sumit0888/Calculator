#create the calculate:

import tkinter as tk
from tkinter import StringVar
root=tk.Tk()
root.geometry("400x260")
root.resizable(0,0)
root.config(bg="black")
x=StringVar()
def show(c):
    x.set(x.get()+c)

def clear():
    x.set("")

def equal():
    b=x.get()
    x.set(eval(b))
    
e=tk.Entry(root,font=("Times",20),justify="right",textvariable=x)
e.place(x=0,y=0,width=400,height=40)


b1=tk.Button(root,text="7",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b1.place(x=0,y=41)
b1.configure(command=lambda:show("7"))
b2=tk.Button(root,text="8",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b2.place(x=100,y=41)
b2.configure(command=lambda:show("8"))
b3=tk.Button(root,text="9",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b3.place(x=200,y=41)
b3.configure(command=lambda:show("9"))
b4=tk.Button(root,text="+",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b4.place(x=300,y=41)
b4.configure(command=lambda:show("+"))


b5=tk.Button(root,text="4",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b5.place(x=0,y=95)
b5.configure(command=lambda:show("4"))
b6=tk.Button(root,text="5",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b6.place(x=100,y=95)
b6.configure(command=lambda:show("5"))
b7=tk.Button(root,text="6",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b7.place(x=200,y=95)
b7.configure(command=lambda:show("6"))
b8=tk.Button(root,text="-",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b8.place(x=300,y=95)
b8.configure(command=lambda:show("-"))

b9=tk.Button(root,text="1",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b9.place(x=0,y=150)
b9.configure(command=lambda:show("1"))
b10=tk.Button(root,text="2",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b10.place(x=100,y=150)
b10.configure(command=lambda:show("2"))
b11=tk.Button(root,text="3",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b11.place(x=200,y=150)
b11.configure(command=lambda:show("3"))
b12=tk.Button(root,text="*",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b12.place(x=300,y=150)
b12.configure(command=lambda:show("*"))

b13=tk.Button(root,text="c",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b13.place(x=0,y=205)
b13.configure(command=lambda:clear())
b14=tk.Button(root,text="=",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b14.place(x=100,y=205)
b14.configure(command=lambda:equal())

b15=tk.Button(root,text="0",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b15.place(x=200,y=205)
b15.configure(command=lambda:show("0"))
b16=tk.Button(root,text="/",font=("Times",20),width=6,height=0,activebackground="yellow",activeforeground="red")
b16.place(x=300,y=205)
b16.configure(command=lambda:show("/"))

root.mainloop()




































































