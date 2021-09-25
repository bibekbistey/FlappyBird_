from tkinter import *
import sqlite3
from PIL import ImageTk, Image
from tkinter import messagebox

#Creating Window

root = Tk()
root.title('Flappy Bird!!! Login and Signup Page')
root.geometry('700x500')
root.iconbitmap('bird.ico')
root.resizable(False, False)

# Importing and resizing image for background in SignUp window

photo = Image.open("database_bg.jpg")
resize_pic = photo.resize((700, 500), Image.ANTIALIAS)
new_pic = ImageTk.PhotoImage(resize_pic)
label = Label(root, image=new_pic)
label.place(x=-3, y=0)

label1 = Label(root, text="WELCOME", font='Ubuntu', fg='red')
label1.place(x=300, y=10)

# Creating database
conn = sqlite3.connect('Login and Registration.db')

c = conn.cursor()

'''
c.execute("""CREATE TABLE addressA(
                FirstName text,
        Username text,
        Password text,
        Country text
)""")
print("Table created successfully")'''



# Creating database for SIGNUP

def Signin():
    def signUp():

        conn = sqlite3.connect("Login and Registration.db")
        c = conn.cursor()

        c.execute("INSERT INTO addressA VALUES(:Name_label, :Username_label, :Password_label,:Country_label)", {
            'Name_label': Name_entry.get(),
            'Username_label': Username_entry.get(),
            'Password_label': Password_entry.get(),
            'Country_label': Region_entry.get()
        })

        print('SIGN IN SUCCESSFUL')
        roe = c.fetchall()
        print(roe)

        conn.commit()
        conn.close()

        Name_entry.delete(0, END)
        Username_entry.delete(0, END)
        Password_entry.delete(0, END)
        Region_entry.delete(0, END)
mainloop()