#Libraries 
from tkinter import *
import ttkthemes
from tkinter import ttk, messagebox
import pymysql #for database
import tkinter as tk


#connection for my phpmyadmin
def connection():
    conn = pymysql.connect(
        host="localhost", 
        user="root", 
        password="", 
        db="Health_Records_db",
    )
    return conn

#function for my refreshTable
def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text='', values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=("Math Sans", 12))
    my_tree.grid(row=10, column=0, columnspan=5, rowspan=90, padx=500, pady=50)
    

root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme("radiance")
root.geometry("1525x778+1+1")
root.title("Dela Paz Pulot Aplaya Health Center Managament System")
root.resizable(False,False)
my_tree = ttk.Treeview(root, height=33)

#Heading Label
heading_label = Label(root, text= "Dela Paz Pulot Aplaya Health Center Management System", font=("Math Sans", 19))
heading_label.place(x=440, y=1)

#placeholder for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()
ph6 = tk.StringVar()
ph7 = tk.StringVar()
ph8 = tk.StringVar()
ph9 = tk.StringVar()
ph10 = tk.StringVar()


#placeholder set ph function
def setph(word,num):
    if num == 1:
        ph1.set(word)
    if num == 2:
        ph2.set(word)
    if num == 3:
        ph3.set(word)
    if num == 4:
        ph4.set(word)
    if num == 5:
        ph5.set(word)
    if num == 6:
        ph6.set(word)
    if num == 7:
        ph7.set(word)
    if num == 8:
        ph8.set(word)
    if num == 9:
        ph9.set(word)
    if num == 10:
        ph10.set(word)

#Function for my read
def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM information")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

#Function for my add button
def add():
    id = str(id_entry.get())
    name = str(name_entry.get())
    phone_number = str(phone_number_entry.get())
    date_of_birth = str(date_of_birth_entry.get())
    age = str(age_entry.get())
    gender = str(gender_entry.get())
    weight = str(weight_entry.get())
    height = str(height_entry.get())
    health_condition = str(health_condition_entry.get())
    medicine = str(medicine_entry.get())

    if (id == "" or id == " ") or (name == "" or name == " ") or (phone_number == "" or phone_number == " ") or (date_of_birth == "" or date_of_birth == " ") or (age == "" or age == " ")or (gender == "" or gender == " ")or (weight == "" or weight == " ")or (height == "" or height == " ")or (health_condition == "" or health_condition == " ")or (medicine == "" or medicine == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO information VALUES ('"+id+"','"+name+"','"+phone_number+"','"+date_of_birth+"','"+age+"','"+gender+"','"+weight+"','"+height+"','"+health_condition+"','"+medicine+"')")
            conn.commit()
            conn.close() 
            messagebox.showinfo("Success", "Added Successfully")
        except:
            messagebox.showinfo("Error", "Id already exist")
            return
    refreshTable()

#Function for my reset button
def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM information")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

#Function for my delete button
def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM information WHERE ID='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

#function for my select button
def select():
    try:
        selected_item = my_tree.selection()[0]
        id = str(my_tree.item(selected_item)['values'][0])
        name = str(my_tree.item(selected_item)['values'][1])
        phone_number = str(my_tree.item(selected_item)['values'][2])
        date_of_birth = str(my_tree.item(selected_item)['values'][3])
        age = str(my_tree.item(selected_item)['values'][4])
        gender = str(my_tree.item(selected_item)['values'][5])
        weight = str(my_tree.item(selected_item)['values'][6])
        height = str(my_tree.item(selected_item)['values'][7])
        health_condition = str(my_tree.item(selected_item)['values'][8])
        medicine = str(my_tree.item(selected_item)['values'][9])

        setph(id,1)
        setph(name,2)
        setph(phone_number,3)
        setph(date_of_birth,4)
        setph(age,5)
        setph(gender,6)
        setph(weight,7)
        setph(height,8)
        setph(health_condition,9)
        setph(medicine,10)

    except:
        messagebox.showinfo("Error", "Please select a data row")

#Function for my search button
def search():
    id = str(id_entry.get())
    name = str(name_entry.get())
    phone_number = str(phone_number_entry.get())
    date_of_birth = str(date_of_birth_entry.get())
    age = str(age_entry.get())
    gender = str(gender_entry.get())
    weight = str(weight_entry.get())
    height = str(height_entry.get())
    health_condition = str(health_condition_entry.get())
    medicine = str(medicine_entry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM information WHERE ID='"+
                id+"' or name='"+
                name+"' or phone_number='"+
                phone_number+"' or date_of_birth='"+
                date_of_birth+"' or age='"+
                age+"'or gender='"+
                gender+"' or weight='"+
                weight+"' or height='"+
                height+"' or health_condition='"+
                health_condition+"' or medicine='"+
                medicine+"' ")

    try:
        result = cursor.fetchall()
        for num in range(0,10):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

#Function for my update button
def update():
    selected_information_id = ""

    try:
        selected_item = my_tree.selection()[0]
        selected_information_id = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    id = str(id_entry.get())
    name = str(name_entry.get())
    phone_number = str(phone_number_entry.get())
    date_of_birth = str(date_of_birth_entry.get())
    age = str(age_entry.get())
    gender = str(gender_entry.get())
    weight = str(weight_entry.get())
    height = str(height_entry.get())
    health_condition = str(health_condition_entry.get())
    medicine = str(medicine_entry.get())

    if (id == "" or id == " ") or (name == "" or name == " ") or (phone_number == "" or phone_number == " ") or (date_of_birth == "" or date_of_birth == " ") or (age == "" or age == " ")or (gender == "" or gender == " ")or (weight == "" or weight == " ")or (height == "" or height == " ")or (health_condition == "" or health_condition == " ")or (medicine == "" or medicine == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE information SET ID='"+
            id+"', Name='"+
            name+"', Phone_Number='"+
            phone_number+"', Date_of_Birth='"+
            date_of_birth+"', Age='"+
            age+"', Gender='"+
            gender+"', Weight='"+
            weight+"', Height='"+
            height+"',  Health_Condition='"+
            health_condition+"', Medicine='"+
            medicine+"' WHERE ID='"+
            selected_information_id+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "ID already exist")
            return

    refreshTable()

#Function for my clear button
def clear_entry():
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    phone_number_entry.delete(0, END)
    date_of_birth_entry.delete(0, END)
    age_entry.delete(0, END)
    gender_entry.delete(0, END)
    weight_entry.delete(0, END)
    height_entry.delete(0, END)
    health_condition_entry.delete(0, END)
    medicine_entry.delete(0, END)

#Id Label & Entry
id_label=Label(root, text= "Id", font=("Math Sans", 15))
id_label.place(x=30, y=50)
id_entry = Entry(root, font=("Math Sans", 15), width=25, bd=2, textvariable=ph1)
id_entry.place(x=190, y=50)

#Name Label & Entry
name_label=Label(root, text= "Name", font=("Math Sans", 15))
name_label.place(x=30, y=90)
name_entry = Entry(root, font=("Math Sans", 15), width=25, bd=2, textvariable=ph2)
name_entry.place(x=190, y=90)

#Phone Number Label & Entry
phone_numberlabel = Label(root, text="Phone Number", font=("Math Sans", 15))
phone_numberlabel.place(x=30, y=130)
phone_number_entry= Entry(root,font=("Math Sans", 15), width=25, bd=2, textvariable=ph3)
phone_number_entry.place(x=190, y=130)

#Date of Birth Label & Entry
date_of_birthlabel=Label(root, text= "Date of Birth", font=("Math Sans", 15))
date_of_birthlabel.place(x=30, y=170)
date_of_birth_entry = Entry(root, font=("Math Sans", 15), width=25, bd=2, textvariable=ph4)
date_of_birth_entry.place(x=190, y=170)

#Age Label & Entry
age_label=Label(root, text= "Age", font=("Math Sans", 15))
age_label.place(x=30, y=210)
age_entry = Entry(root, font=("Math Sans", 15), width=25, bd=2, textvariable=ph5)
age_entry.place(x=190, y=210)

#Gender Label & Entry
gender_label=Label(root, text= "Gender", font=("Math Sans", 15))
gender_label.place(x=30, y=250)
gender_entry = Entry(root, font=("Math Sans", 15), width=25, bd=2, textvariable=ph6)
gender_entry.place(x=190, y=250)

#Weight Label & Entry
weight_label=Label(root, text= "Weight", font=("Math Sans", 15))
weight_label.place(x=30, y=290)
weight_entry = Entry(root, font=("Math Sans", 15), width=25, bd=2, textvariable=ph7)
weight_entry.place(x=190, y=290)

#Height Label & Entry
height_label=Label(root, text= "Height", font=("Math Sans", 15))
height_label.place(x=30, y=330)
height_entry = Entry(root, font=("Math Sans", 15), width=25, bd=2, textvariable=ph8)
height_entry.place(x=190, y=330)

#Health Condition Label & Entry
health_condition_label=Label(root, text= "Health Condition", font=("Math Sans", 15))
health_condition_label.place(x=30, y=370)
health_condition_entry = Entry(root, font=("Math Sans", 15), width=25, bd=2, textvariable=ph9)
health_condition_entry.place(x=190, y=370)

#Medicine Label & Entry
medicine_label=Label(root, text= "Medicine", font=("Math Sans", 15))
medicine_label.place(x=30, y=410)
medicine_entry = Entry(root, font=("Math Sans", 15), width=25, bd=2, textvariable=ph10)
medicine_entry.place(x=190, y=410)

#Add Button
addname_button = ttk.Button(root, text="Add", command=add)
addname_button.place(x=50, y=480)

#Update Button
update_button = ttk.Button(root,text="Update", command=update)
update_button.place(x=190, y=480)

#Delete Button
delete_button = ttk.Button(root, text="Delete", command=delete)
delete_button.place(x=330, y=480)

#Search Button
search_button = ttk.Button(root, text="Search", command=search)
search_button.place(x=50, y=560)

#Reset Button
reset_button = ttk.Button(root, text="Reset", command=reset)
reset_button.place(x=190, y=560)

#Select Button
select_button = ttk.Button(root, text="Select", command=select)
select_button.place(x=330, y=560)

#Clear Button
clear_button = ttk.Button(root, text="Clear", command=clear_entry)
clear_button.place(x=190, y=640)

#My Tree View
style=ttk.Style()
style.configure("Treeview.Heading", font=("Math Sans", 15))
my_tree['columns'] =("Id", "Name", "Phone Number", "Date of Birth", "Age", "Gender", "Weight", "Height", "Health Condition", "Medicine")

#Column of my Tree View
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Id",anchor=CENTER, width=50,)
my_tree.column("Name",anchor=CENTER, width=80)
my_tree.column("Phone Number",anchor=CENTER, width=150)
my_tree.column("Date of Birth",anchor=CENTER, width=150)
my_tree.column("Age",anchor=CENTER, width=60)
my_tree.column("Gender",anchor=CENTER, width=80)
my_tree.column("Weight",anchor=CENTER, width=80)
my_tree.column("Height",anchor=CENTER, width=80)
my_tree.column("Health Condition",anchor=CENTER, width=150)
my_tree.column("Medicine",anchor=CENTER, width=110)

#Heading of the Column in my Tree View
my_tree.heading("Id", text="Id", anchor=CENTER)
my_tree.heading("Name", text="Name", anchor=CENTER)
my_tree.heading("Phone Number", text="Phone Number", anchor=CENTER)
my_tree.heading("Date of Birth", text="Date of Birth", anchor=CENTER)
my_tree.heading("Age", text="Age", anchor=CENTER)
my_tree.heading("Gender", text="Gender", anchor=CENTER)
my_tree.heading("Weight", text="Weight", anchor=CENTER)
my_tree.heading("Height", text="Height", anchor=CENTER)
my_tree.heading("Health Condition", text="Health Condition", anchor=CENTER)
my_tree.heading("Medicine", text="Medicine", anchor=CENTER)


refreshTable()
root.mainloop()