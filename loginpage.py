import tkinter as tk
import os

def open_code_1():
    root.destroy()
    os.system("python dreamhome_tkinter\\userlogin.py")

def open_code_2():
    root.destroy()
    os.system("python dreamhome_tkinter\\stafflogin.py")
    
def open_code_3():
    root.destroy()
    os.system("python dreamhome_tkinter\\adminlogin.py")
    
def open_code_4():
    root.destroy()
    os.system("python dreamhome_tkinter\\clientregisteration.py")

root = tk.Tk()
root.title("Login Page")
root.geometry("400x380")
frame = tk.Frame(root, width=350, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)
large_font1 = ('Verdana', 10)

login_label = tk.Label(frame, text="Which Login?",bg="#2C3E50",fg="Orange",font=large_font)
login_label.place(x=125,y=15)

button1 = tk.Button(frame, text="User Login", command=open_code_1,font=large_font1)
button1.place(x=150,y=105)
button2 = tk.Button(frame, text="Staff Login", command=open_code_2,font=large_font1)
button2.place(x=145,y=175)
button3 = tk.Button(frame, text="Admin Login", command=open_code_3,font=large_font1)
button3.place(x=145,y=245)
button4 = tk.Button(frame, text="User Registeration", command=open_code_4,font=large_font1)
button4.place(x=125,y=315)


root.mainloop()
