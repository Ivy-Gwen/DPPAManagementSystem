#Libraries
from tkinter import *
from tkinter import messagebox

root = Tk() #Display the window
root.title('Login to Dela Paz Pulot Aplaya Health Center Management System') #root Title
root.geometry("1320x720+50+50") #Size of the window
root.resizable(False,False) #fixed size

#Background Image
background = PhotoImage(file="bg.png")

#Label Of the Background
my_label=Label(root, image=background)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

#Label Of Heading
heading_Login= Label(root, text="USER LOGIN", fg="black", bg="#F6F6F6", font=("Math Sans", 30, "bold") )
heading_Login.place(x=820, y=150)

#Function for login Button
def login():
    if username_entry.get() == "" or password_entry.get() =="":
        messagebox.showerror("Error", "Fields cannot be empty")
    elif username_entry.get() == "BHW" and password_entry.get() == "1234":
        messagebox.showinfo("Success", "Successfully Login")
        root.destroy()
        import DPPAManagementSystem #my main file
        
    else:
        messagebox.showerror("Error", "Please Enter Correct Credentials ")

#User Name Label & Entry
username_label = Label(root, text= "Username", font=("Math Sans", 19), bg="white", activebackground="white")
username_label.place(x=740, y=250)
username_entry= Entry(root, width=19,font=("Math Sans", 19), border=2)
username_entry.place(x=890, y=250)

#Password Label & Entry
password_label = Label(root, text="Password", font=("Math Sans", 19), bg="white", activebackground="white")
password_label.place(x=740, y=335)
password_entry= Entry(root, width=19, font=("Math Sans", 19),border=2)
password_entry.place(x=890, y=335)

#Login Button
login_button = Button(root, text="Login", font=("Math Sans", 22, "bold"),bg="light blue", activebackground="light blue", cursor="hand2", command=login)
login_button.place(x=890, y=440)

root.mainloop()
