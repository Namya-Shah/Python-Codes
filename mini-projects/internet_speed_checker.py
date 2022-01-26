from tkinter import *
from tkinter import messagebox
from turtle import bgcolor
from matplotlib.pyplot import pink
import pyspeedtest

def one():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download())+"[Bytes per second]")
    messagebox.showinfo("Your Download Speed", a1)

root = Tk()
root.title("Internet Speed Checker")
root.config(bg="pink")
root.geometry("500x250")

label1 = Label(root, text="Internet Speed Checker!", font=("Arial", 30, "bold"), bg="lightblue").pack()
button1 = Button(root, text="Click!!", font=("Arial", 20, "bold"), bg="yellow", height=1, width=10, command=one).pack()




root.mainloop()
