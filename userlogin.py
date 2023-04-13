import tkinter as tk
import mysql.connector
import os

def open_code_1():
    root.destroy()
    os.system("python userInterface.py")

def open_code_2():
    root.destroy()
    os.system("python loginpage.py")

def check_credentials():
    clientno = id_box.get()
    email = email_box.get()
    
    db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='proj'
    )
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM clients WHERE clientno = %s AND email = %s", (clientno, email))
    
    row = cursor.fetchone()
    
    if row:
        message.config(text="Login Successful", fg="green")
        open_code_2()
        root.destroy()
    else:
        message.config(text="Invalid User ID or Email", fg="red")


root = tk.Tk()
root.title("User Login")
root.geometry("400x250")
frame = tk.Frame(root, width=350, height=500, bg="#2C3E50")
frame.pack(fill=tk.BOTH, expand=True)

large_font = ('Verdana', 15)
large_font1 = ('Verdana', 10)

button1 = tk.Button(frame, text="Back",fg="red", command=open_code_2)
button1.place(x=10,y=10)

user_label = tk.Label(frame, text="User Login",bg="#2C3E50",fg="Orange",font=large_font)
user_label.place(x=125,y=15)

id_label = tk.Label(frame, text="Enter Client Id :",bg="#2C3E50",fg="white",font=large_font1)
id_label.place(x=50, y=80)
id_box = tk.Entry(frame)
id_box.place(x=180, y=80)
email_label = tk.Label(frame, text="Enter Email :",bg="#2C3E50",fg="white",font=large_font1)
email_label.place(x=50, y=120)
email_box = tk.Entry(frame)
email_box.place(x=180, y=120)

button = tk.Button(frame, text="Login", command=check_credentials,bg="#1ABC9C")
button.place(x=180, y=180)

message = tk.Label(frame, text="")


root.mainloop()
