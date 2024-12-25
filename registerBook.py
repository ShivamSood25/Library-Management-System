from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from issueret import ISSUE_RET
from register import MEMBERS

def window():
    top=Toplevel()
    db=MEMBERS('members.db')
    bd=ISSUE_RET('issue.db')
    top.title('Register')
    top.geometry('900x700')
    top.f = StringVar()
    top.l = StringVar()
    top.fees = StringVar()
    top.p = StringVar()
    top.a = StringVar()
    
    frame=Frame(top,bg='#4B4B4B')
    frame.pack(side=TOP,fill=X)

    heading=Label(frame,text='REGISTER:', fg='#F5F5F5', bg='#4B4B4B',font=("Verdana", 20, "bold","underline"))
    heading.grid(row=1, columnspan=1, pady=20)
    
    Fname=Label(frame,text='First name:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
    Fname.grid(row=2,column=0,sticky='w',padx=20)
    eFname=Entry(frame,textvariable=top.f,fg='black',bg='white',font=("Verdana", 13),width=30)
    eFname.grid(row=2,column=2,pady=10,sticky='w')
    
    Lname=Label(frame,text='Last name:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
    Lname.grid(row=3,column=0,sticky='w',padx=20)
    eLname=Entry(frame,textvariable=top.l,fg='black',bg='white',font=("Verdana", 13),width=30)
    eLname.grid(row=3,column=2,pady=10,sticky='w')
    
    Phone = Label(frame, text='Contact:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
    Phone.grid(row=4,column=0,sticky='w',padx=20)
    ePhone = Entry(frame, textvariable=top.p,fg='black',bg='white',font=("Verdana", 13),width=30)
    ePhone.grid(row=4, column=2,pady=10,sticky='w')

    Address = Label(frame, text='Address:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
    Address.grid(row=5,column=0,sticky='w',padx=20)
    eAddress = Entry(frame, textvariable=top.a,fg='black',bg='white',font=("Verdana", 13),width=30)
    eAddress.grid(row=5, column=2,pady=10,sticky='w')

    def disp():
        tv.delete(*tv.get_children())
        for row in db.fetch():
            tv.insert("", END,values=row)

    def clear():
        top.f.set('')
        top.l.set('')
        top.a.set('')
        top.p.set('')      

    def login():
        if top.f.get()=='' or top.l.get()==''or top.p.get()==''  or top.a.get()=='':
            messagebox.showerror('Error','Fill all details', parent=top)
        try:
            phone= int(top.p.get())
        except ValueError:
            messagebox.showerror("Error in Input", "Phone number should not be in text form")
            return
        else:
            top.fees=0
            db.insert(top.f.get(),top.l.get(),top.p.get(),top.a.get())
            messagebox.showinfo('Succesfull','Registered succesfully', parent=top)
            top.quit()
            clear()
            disp()

    def update():
        if top.f.get()=='' or top.l.get()==''or top.p.get()==''  or top.a.get()=='':
            messagebox.showerror('Success','please fill all details', parent=top)
            return
        try:
            phone= int(top.p.get())
        except ValueError:
            messagebox.showerror("Error in Input", "Phone number should not be in text form")
            return
        db.update(row[0],top.f.get(),top.l.get(),top.p.get(),top.a.get())
        messagebox.showinfo('success','Data updated', parent=top)
        clear()
        disp()

    def get(event):
        select_row=tv.focus()
        data=tv.item(select_row)
        global row
        row=data["values"]
        top.f.set(row[1])
        top.l.set(row[2])
        top.fees.set(row[3])
        top.p.set(row[4])
        top.a.set(row[5])
    
    def delete():
        db.remove(row[0])
        clear()
        disp()


    def searchdata():
        search_query = search_entry.get().strip()
        if not search_query:
            messagebox.showwarning("Input Error", "Please enter a search query.", parent=top)
            return
        if search_query:
            matching_rows = db.showmemid(search_query)
            if matching_rows:
                tv.delete(*tv.get_children())
                for row in matching_rows:
                    tv.insert("", END, values=row)
            else:
                messagebox.showinfo("Search Result", "No results found.", parent=top)  

    btn_frame = Frame(frame, bg="#4B4B4B")
    btn_frame.grid(row=9, column=0, columnspan=4, padx=30, pady=10, sticky="w")

    submit=Button(btn_frame,text='Submit',command=login,bg='#00B894', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
    submit.grid(row=10,column=3,padx=10,ipadx=10,ipady=2)
    submit=Button(btn_frame,text='Update',command=update,bg='#00CEC9', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
    submit.grid(row=10,column=4,padx=10,ipadx=10,ipady=2)
    delete=Button(btn_frame,text='Delete',command=delete,bg='#FF7675', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
    delete.grid(row=10,column=5,padx=10,ipadx=10,ipady=2)
    cancel=Button(btn_frame,text='Clear',command=clear,bg='#E17055', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
    cancel.grid(row=10,column=6,padx=10,ipadx=10,ipady=2)


    tf=Frame(top,bg='White')
    tf.place(x=0, y=310, relwidth=1, relheight=0.7)
    tf.pack(fill=BOTH, expand=True)
    tf.pack_propagate(False)

    search_frame=Frame(tf,bg="#2E2E2E")
    search_frame.pack(side=TOP,fill=X,ipady=17)

    scrollbar=Scrollbar(tf,orient=VERTICAL,width=25)
    scrollbar.pack(side=RIGHT,fill=Y)
    
    search_label = Label(search_frame, text="Search Member ID:",bg ='#2E2E2E',fg="white",font=("Verdana",10,"bold"))
    search_label.place(x=30, y=7)
    search_entry = Entry(search_frame, width=40, font=("Verdana",10))
    search_entry.place(x=180, y=7)
    search_button = Button(search_frame, text="Search", command=searchdata,bg='#0984E3', fg="#2E2E2E", font=("Verdana",10,"bold"))
    search_button.place(x=570, y=5)

    all=Button(search_frame,text='Show All',command=disp,bg='#74B9FF',font=("Verdana",10,"bold"))
    all.place(x=670,y=5)

    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=35) 
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,"bold"))
 
    tv=ttk.Treeview(tf,columns=(1,2,3,4,5,6), yscrollcommand=scrollbar.set,style="mystyle.Treeview")
    tv.heading("1", text="Member ID")
    tv.column("1", width=20,anchor='center')
    tv.heading("2", text="First Name")
    tv.column("2", width=20)
    tv.heading("3", text="Last Name")
    tv.column("3", width=20)
    tv.heading("4", text="Fine (Rs.)")
    tv.column("4", width=20,anchor='center')
    tv.heading("5", text="Contact")
    tv.column("5", width=20)
    tv.heading("6", text="Address")
    tv.column("6", width=20)
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", get)
    tv.pack(fill=BOTH,expand=1)
    scrollbar.config(command=tv.yview)
    
    disp()
    def resize(event):
        tf.config(width=event.width, height=event.height)

    top.bind("<Configure>", resize)
    top.mainloop()

if __name__ == "__main__":
    window()