from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db = Database("Employee.db")

root = Tk()
root.title('Employee Management System')
root.geometry('1240x615+0+0')
root.resizable(False, False)
root.configure(bg='#2c3e50')

name = StringVar()
age = StringVar()
job = StringVar()
gender = StringVar()
email = StringVar()
mobile = StringVar()

logo = PhotoImage(file='A.png')
lbl_logo = Label(root, image=logo, bg='#2c3e50')
lbl_logo.place(x=14, y=510)

# ====Functions====

def hide():
    root.geometry('360x515+0+0')

def show():
    root.geometry('1240x615+0+0')

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    job.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    mobile.set(row[6])
    textAddress.delete(1.0, END)
    textAddress.insert(END, row[7])

def delete():
 db.remove(row[0])
 clear()
 displayAll()

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("", END, values=row)

def clear():
    name.set("")
    age.set("")
    job.set("")
    gender.set("")
    email.set("")
    mobile.set("")
    textAddress.delete(1.0, END)

def add_employee():
    if txtName.get() == "" or txtAge.get() == "" or txtJob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or textAddress.get(1.0, END).strip() == "":
        messagebox.showerror("Error", "Please fill all the entries")
        return
    db.insert(
        txtName.get(),
        txtAge.get(),
        txtJob.get(),
        txtEmail.get(),
        comboGender.get(),
        txtContact.get(),
        textAddress.get(1.0, END).strip()
    )
    messagebox.showinfo("Success", "Added new Employee")
    clear()
    displayAll()

def update():
    if txtName.get() == "" or txtAge.get() == "" or txtJob.get() == "" or txtEmail.get() == "" or comboGender.get() == "" or txtContact.get() == "" or textAddress.get(1.0, END).strip() == "":
        messagebox.showerror("Error", "Please fill all the entries")
        return
    db.update(row[0],
        txtName.get(),
        txtAge.get(),
        txtJob.get(),
        txtEmail.get(),
        comboGender.get(),
        txtContact.get(),
        textAddress.get(1.0, END)
        )
    messagebox.showinfo("Success","The employee data is updated")
    clear()
    displayAll()

# ====Entries Frame====
entries_frame = Frame(root, bg='#2c3e50')
entries_frame.place(x=1, y=1, width=360, height=510)
title = Label(entries_frame, text='Employee Company', font=('Calibri', 18, 'bold'), bg='#2c3e50', fg='white')
title.place(x=10, y=1)
lblName = Label(entries_frame, text="Name", font=('Calibri', 16), bg='#2c3e50', fg='white')
lblName.place(x=10, y=50)

txtName = Entry(entries_frame, textvariable=name, width=20, font=('Calibri', 16))
txtName.place(x=120, y=50)

lblJob = Label(entries_frame, text="Job", font=('Calibri', 16), bg='#2c3e50', fg='white')
lblJob.place(x=10, y=90)
txtJob = Entry(entries_frame, textvariable=job, width=20, font=('Calibri', 16))
txtJob.place(x=120, y=90)

lblGender = Label(entries_frame, text="Gender", font=('Calibri', 16), bg='#2c3e50', fg='white')
lblGender.place(x=10, y=130)
comboGender = ttk.Combobox(entries_frame, textvariable=gender, state='readonly', width=18, font=('Calibri', 16))
comboGender['values'] = ("Male", "Female")
comboGender.place(x=120, y=130)

lblAge = Label(entries_frame, text="Age", font=('Calibri', 16), bg='#2c3e50', fg='white')
lblAge.place(x=10, y=170)
txtAge = Entry(entries_frame, textvariable=age, width=20, font=('Calibri', 16))
txtAge.place(x=120, y=170)

lblEmail = Label(entries_frame, text="Email", font=('Calibri', 16), bg='#2c3e50', fg='white')
lblEmail.place(x=10, y=210)
txtEmail = Entry(entries_frame, textvariable=email, width=20, font=('Calibri', 16))
txtEmail.place(x=120, y=210)

lblContact = Label(entries_frame, text="Mobile", font=('Calibri', 16), bg='#2c3e50', fg='white')
lblContact.place(x=10, y=250)
txtContact = Entry(entries_frame, textvariable=mobile, width=20, font=('Calibri', 16))
txtContact.place(x=120, y=250)

lblAddress = Label(entries_frame, text="Address:", font=('Calibri', 16), bg='#2c3e50', fg='white')
lblAddress.place(x=10, y=290)
textAddress = Text(entries_frame, width=30, height=2, font=('Calibri', 16))
textAddress.place(x=10, y=330)

# ====Buttons Frame====
btn_frame = Frame(entries_frame, bg='#2c3e50', bd=1, relief=SOLID)
btn_frame.place(x=10, y=400, width=335, height=100)

btnAdd = Button(btn_frame,
                text='Add Details',
                width=14,
                height=1,
                font=('Calibri', 16),
                fg='white',
                bg='#16a085',
                bd=0,
                command=add_employee
                ).place(x=4, y=5)

btnEdit = Button(btn_frame,
                 text='Update Details',
                 width=14,
                 height=1,
                 font=('Calibri', 16),
                 fg='white',
                 bg='#2980b9',
                 bd=0,
                 command=update
                 ).place(x=4, y=50)

btnDelete = Button(btn_frame,
                   text='Delete Details',
                   width=14,
                   height=1,
                   font=('Calibri', 16),
                   fg='white',
                   bg='#c0392b',
                   bd=0 ,
                   command=delete
                   ).place(x=170, y=5)

btnClear = Button(btn_frame,
                  text='Clear Details',
                  width=14,
                  height=1,
                  font=('Calibri', 16),
                  fg='white',
                  bg='#f39c12',
                  bd=0,
                  command=clear
                  ).place(x=170, y=50)

btnHide = Button(entries_frame, text='HIDE', bg='white', bd=1, relief=SOLID, cursor='hand2', command=hide)
btnHide.place(x=270, y=10)

btnShow = Button(entries_frame, text='SHOW', bg='white', bd=1, relief=SOLID, cursor='hand2', command=show)
btnShow.place(x=310, y=10)

# =====(Table Frame)============
tree_frame = Frame(root, bg='white')
tree_frame.place(x=365, y=1, width=875, height=610)
style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 13), rowheight=50)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13))
tv = ttk.Treeview(tree_frame, columns=(1, 2, 3, 4, 5, 6, 7, 8), style="mystyle.Treeview")
tv.heading("1", text="ID")
tv.column("1", width="40")
tv.heading("2", text="Name")
tv.column("2", width="140")
tv.heading("3", text="Age")
tv.column("3", width="50")
tv.heading("4", text="Job")
tv.column("4", width="120")
tv.heading("5", text="Email")
tv.column("5", width="150")
tv.heading("6", text="Gender")
tv.column("6", width="90")
tv.heading("7", text="Mobile")
tv.column("7", width="150")
tv.heading("8", text="Address")
tv.column("8", width="150")
tv['show'] = 'headings'
tv.place(x=1, y=1, height=610, width=875)
tv.bind("<ButtonRelease-1>", getData)
displayAll()

root.mainloop()

 ##==this code made by sarah ==cc========#