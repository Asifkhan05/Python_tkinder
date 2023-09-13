from tkinter import *
from tkinter import ttk
from dp import Database
from tkinter import messagebox

db=Database("emp.db")

root = Tk()
root.title("User management")
root.geometry("1920x1080+0+0")
root.state("zoomed")
root.config(bg="silver")

name=StringVar()
age=StringVar()
doj=StringVar()
email=StringVar()
gender=StringVar()
contact=StringVar()
address=StringVar()


frame=Frame(root,bg="gray")
frame.pack(side=TOP,fill=X)
title=Label(frame,text="Employess management system", font=("Calibri",18,"bold"),bg="gray",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20,)

lb_name=Label(frame,text="Name",font=("calibir",16),bg="gray",fg="white")
lb_name.grid(row=1,column=0 ,padx=10,pady=10,sticky="w")
txt_name=Entry(frame,textvariable=name,font=("calibir",16),width=30)
txt_name.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lb_age=Label(frame,text="Age",font=("calibir",16),bg="gray",fg="white")
lb_age.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txt_age=Entry(frame,textvariable=age,font=("calibir",16),width=30)
txt_age.grid(row=1,column=3,padx=10,pady=10,sticky="w")

lb_doj=Label(frame,text="DOJ",font=("calibir",16),bg="gray",fg="white")
lb_doj.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txt_doj=Entry(frame,textvariable=doj,font=("calibir",16),width=30)
txt_doj.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lb_email=Label(frame,text="Email",font=("calibir",16),bg="gray",fg="white")
lb_email.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txt_email=Entry(frame,textvariable=email,font=("calibir",16),width=30)
txt_email.grid(row=2,column=3,padx=10,pady=10,sticky="w")

lb_gender=Label(frame,text="Gender",font=("calibir",16),bg="gray",fg="white")
lb_gender.grid(row=3,column=0,padx=10,pady=10,sticky="w")
combo=ttk.Combobox(frame,font=("calibri",16),width=31,textvariable=gender,state="readonly")
combo["values"]=("Male","Female","Others")
combo.grid(row=3,column=1,padx=10,pady=10,sticky="w")

lb_contact=Label(frame,text="Contact",font=("calibir",16),bg="gray",fg="white")
lb_contact.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txt_contact=Entry(frame,textvariable=contact,font=("calibir",16),width=30)
txt_contact.grid(row=3,column=3,padx=10,pady=10,sticky="w")

lb_address=Label(frame,text="Address",font=("calibir",16),bg="gray",fg="white")
lb_address.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txt_address=Text(frame,width=80,height=5,font=("calibir",16))
txt_address.grid(row=5,columnspan=4,padx=10,sticky="w")

def getData(ev):
    select=tv.focus()
    data=tv.item(select)
    global row
    row=data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txt_address.delete(1.0,END)
    txt_address.insert(END,row[7])


def display():
    tv.delete(*tv.get_children())
    for wow in db.fetch():
        tv.insert("",END,values=wow)
def add_emp():
    if txt_name.get()=="" or txt_age.get() == "" or txt_doj.get()=="" or txt_email.get()=="" or combo.get()=="" or txt_contact.get()=="" or  txt_address.get(1.0,END)=="":
        messagebox.showerror("Error in Input","Please Fill All The Details")
        return
    db.insert(txt_name.get(),txt_age.get(),txt_doj.get(), txt_email.get(), combo.get(),txt_contact.get(), txt_address.get(1.0,END))
    messagebox.showinfo("Success","User details insert")
    clear_emp()
    display()


def update_emp():
    if txt_name.get() == "" or txt_age.get() == "" or txt_doj.get() == "" or txt_email.get() == "" or combo.get() == "" or txt_contact.get() == "" or txt_address.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "Please Fill All The Details")
        return
    db.update(row[0],txt_name.get(), txt_age.get(), txt_doj.get(), txt_email.get(), combo.get(), txt_contact.get(),
              txt_address.get(1.0, END))
    messagebox.showinfo("Success", "User details updated")
    clear_emp()
    display()

def delete_emp():
    db.delete(row[0])
    clear_emp()
    display()

def clear_emp():
    name.set("")
    age.set("")
    doj.set("")
    email.set("")
    gender.set("")
    contact.set("")
    address.set("")
    txt_address.delete(1.0,END)


btn_frame=Frame(frame,bg="gray")
btn_frame.grid(row=6,columnspan=4,pady=10,sticky="w")

add=Button(btn_frame,command=add_emp, text="Add Details",width=15,bg="blue",font=("calibir",16,"bold"),fg="white",bd=0).grid(row=0,column=0,padx=10)

edit=Button(btn_frame,command=update_emp, text="Update Details",width=15,bg="green",font=("calibir",16,"bold"),fg="white",bd=0).grid(row=0,column=1,padx=10)

delete=Button(btn_frame,command=delete_emp, text="Delete Details",width=15,bg="red",font=("calibir",16,"bold"),fg="white",bd=0).grid(row=0,column=2,padx=10)

clear=Button(btn_frame,command=clear_emp, text="Clear Details",width=15,bg="yellow",font=("calibir",16,"bold"),fg="white",bd=0).grid(row=0,column=3,padx=10)



# table frame

t_frame=Frame(root,bg="white")
t_frame.place(x=0,y=457,width=1600,height=520)


style=ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",18),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=("calibri",18))

tv =ttk.Treeview(t_frame,style="mystyle.Treeview",columns=(1,2,3,4,5,6,7,8))
tv.heading("1",text="ID")
tv.column("1",width=4)
tv.heading("2",text="Name")
tv.heading("3",text="Age")
tv.column("3",width=4)
tv.heading("4",text="DOJ")
tv.heading("5",text="Email")
tv.heading("6",text="Gender")
tv.column("6",width=7)
tv.heading("7",text="Contact")
tv.heading("8",text="Address")
tv["show"]="headings"
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

display()

root.mainloop()