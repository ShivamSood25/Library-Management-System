from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from issueret import ISSUE_RET
from books import Books
from register import MEMBERS
from datetime import date # type: ignore

def issue():
    db=Books('BOOK3.db')
    bd=MEMBERS('members.db')
    data=ISSUE_RET('issue.db')
    tk=Toplevel()
    mem_ID=StringVar()
    bookID=StringVar()
    tk.geometry('900x700')
    tk.title('Issue a book')
    doi=date.today()

    def showmids():
        global membersid
        membersid = []
        for ids in bd.showid():
            membersid.append(ids[0])
        return membersid

    def showbids():
        global booksid
        booksid = []
        for ids in db.showbookid():
            booksid.append(ids[0])
        return booksid

    frame=Frame(tk,bg='#4B4B4B')
    frame.pack(side=TOP,fill=X)

    head=Label(frame,text='ISSUE BOOK:',fg='#F5F5F5',bg='#4B4B4B',font=("Verdana", 20, "bold","underline"))
    head.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")

    # member
    lmem=Label(frame,text='Select member id:',bg='#4B4B4B',fg='#F5F5F5',font=("Verdana", 12))
    lmem.grid(row=2,column=1)
    memsid=ttk.Combobox(frame,textvariable=mem_ID,value=showmids(),width=50)
    memsid.grid(column=2, row=2, padx=10, pady=10)

    # book
    lbook=Label(frame,text='Select book id:',bg='#4B4B4B',fg='#F5F5F5',font=("Verdana", 12))
    lbook.grid(row=3,column=1)
    bookid=ttk.Combobox(frame,textvariable=bookID,value=showbids(),width=50)
    bookid.grid(column=2, row=3, padx=10, pady=10)

    def disp(): 
        tv.delete(*tv.get_children())
        for row in data.fetch():
            tv.insert("",END,values=row)

    def add():
        if mem_ID.get()=='' or bookID.get()=='': 
            messagebox.showerror('error','please fill all details', parent=tk)
            return
        data.insert(doi,mem_ID.get(),bookID.get(),dor='NA',fine='NA')
        messagebox.showinfo("Success", "Book Issued Successfully", parent=tk)
        clear()
        disp()

    def clear():
        mem_ID.set('')
        bookID.set('')

    def get(event):
        select_row=tv.focus()
        data=tv.item(select_row)
        global row
        row=data["values"]

    def delete():
        data.remove(row[0])
        clear()
        disp()

    btn_frame = Frame(frame, bg="#4B4B4B")
    btn_frame.grid(row=9, column=0, columnspan=4, padx=10, pady=10, sticky="w")

    insert=Button(btn_frame,command=add,text='Submit', font=("Verdana", 9, "bold"), width=12, bg='#00B894', fg="#2E2E2E")
    insert.grid(row=9,column=1,ipadx=6,ipady=2,padx=10)
    insert=Button(btn_frame,command=delete,text='Delete', font=("Verdana", 9, "bold"), width=12, bg='#FF7675', fg="#2E2E2E")
    insert.grid(row=9,column=2,ipadx=6,ipady=2,padx=10)

    # Treeview frame
    tf=Frame(tk,bg='White')
    tf.place(x=0, y=185, relwidth=1, relheight=0.7)
    tf.pack(fill=BOTH, expand=True)
    tf.pack_propagate(False)

    search_frame=Frame(tf,bg="#2E2E2E")
    search_frame.pack(side=TOP,fill=X,ipady=17) 

    scrollbar=Scrollbar(tf,orient=VERTICAL,width=25)
    scrollbar.pack(side=RIGHT,fill=Y) 

    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 12), rowheight=35) 
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,"bold"))

    tv=ttk.Treeview(tf,columns=(1,2,3,4,5,6), yscrollcommand=scrollbar.set,style="mystyle.Treeview")
    tv.heading("1", text="Transaction ID")
    tv.column("1", width=1,anchor='center')
    tv.heading("2", text="Date of Issue")
    tv.column("2", width=1,anchor='center')
    tv.heading("3", text="Member ID")
    tv.column("3", width=1,anchor='center')
    tv.heading("4", text="Books ID")
    tv.column("4", width=1,anchor='center')
    tv.heading("5", text="Date of return")
    tv.column("5", width=1,anchor='center')
    tv.heading("6", text="Fine")
    tv.column("6", width=1,anchor='center')
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", get)
    tv.pack(fill=BOTH, expand=1)
    disp()
    scrollbar.config(command=tv.yview)

    def resize(event):
        tf.config(width=event.width, height=event.height)

    tk.bind("<Configure>", resize)
    tk.mainloop()   

if __name__ == "__main__":
    issue()