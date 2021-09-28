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

        # Creating new window

        signupwindow = Toplevel()
        signupwindow.geometry('650x400')
        signupwindow.configure(bg="Light Yellow")
        signupwindow.title(' SIGNUP FAST!')
        signupwindow.resizable(False, False)
        signupwindow.iconbitmap('bird.ico')

        # Designing Frames

        Frame1 = Frame(signupwindow, bd=10, bg='black', relief=RIDGE)
        Frame1.place(x=15, y=0)

        Frame2 = Label(Frame1, font=('Ubuntu', 20, 'bold'), fg="red", bg='White', text='Create Your Account ', padx=150)
        Frame2.grid()

        Details_entry = Frame(signupwindow, bd=10, bg='orange', width=810, height=690, padx=180, relief=RIDGE)
        Details_entry.place(x=15, y=100)

        # Building and designing Labels, Entries and Buttons for SignUp Window
        Name = Label(Details_entry, text='Name', fg="blue", bg="orange", font='Helvetica')
        Name.grid(row=1, column=0)

        Name_entry = Entry(Details_entry, font='Times', bd=3, relief=SUNKEN)
        Name_entry.grid(row=1, column=1)

        Username = Label(Details_entry, text="Username", fg="blue", bg="orange", font='Helvetica')
        Username.grid(row=2, column=0)

        Username_entry = Entry(Details_entry, font='Times', bd=3, relief=SUNKEN)
        Username_entry.grid(row=2, column=1)

        Password = Label(Details_entry, text="Password", fg="blue", bg="orange", font='Helvetica')
        Password.grid(row=3, column=0)

        Password_entry = Entry(Details_entry, show="*", font='Times', bd=3, relief=SUNKEN)
        Password_entry.grid(row=3, column=1)

        Region = Label(Details_entry, text="Region", fg="blue", bg="orange", font='Helvetica')
        Region.grid(row=4, column=0)

        Region_entry = Entry(Details_entry, font='Times', bd=3, relief=SUNKEN)
        Region_entry.grid(row=4, column=1)

        Submit = Button(Details_entry, text="Submit", font='Times ', bg="Light Green", command=signUp)
        Submit.grid(row=5, column=1)
# Making and Designing labels, entries and buttons for LogIn Window

Username = Label(root, text="Username",fg="blue", bg="Light Green", font='Times')
Username.place(x=170, y=70)

Username_entry = Entry(root,  bd=3,font='Helvetica', relief=SUNKEN)
Username_entry.place(x=270, y=70)

Password = Label(root, text="Password", fg="blue", bg="light green",font='Times')
Password.place(x=170, y=150)

Password_entry = Entry(root,show="*",  bd=3,font='Helvetica', relief=SUNKEN)
Password_entry.place(x=270, y=150)

login_button = Button(root, text="LogIn",fg="blue", bg="Light Green", font='Cambria 15 italic',command=logdata)
login_button.place(x=295, y=240)

signup_button = Button(root, text="SignUp", fg="blue", bg="Light Green",font='Cambria 15 italic', command=Signin)
signup_button.place(x=295, y=350)

NewAccount = Label(root, text="First Time?",  fg='white', bg="red",font='Cambria 15 italic', width=10)
NewAccount.place(x=270, y=300)

conn.commit()

conn.close()

mainloop()