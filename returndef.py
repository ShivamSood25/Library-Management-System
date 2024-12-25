from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from issueret import ISSUE_RET
from datetime import date  # type: ignore

def retnb():
    data = ISSUE_RET('issue.db')
    tk = Toplevel()
    tk.geometry('900x700')
    tk.title('Return a book')
    dor = date.today().strftime('%Y-%m-%d')

    frame = Frame(tk, bg='#4B4B4B')
    frame.pack(side=TOP, fill=X)

    head = Label(frame, text='RETURN BOOK:', fg='#F5F5F5', bg='#4B4B4B', font=("Verdana", 20, "bold", "underline"))
    head.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")
    def update():
        if row:
            doi = row[1]
            data.update(row[0], dor,'0')
            disp()
            messagebox.showinfo('Success',"Book Returned succesfully", parent=tk)
        else:
            messagebox.showerror('Error', 'No book selected!', parent=tk)

    def disp():
        tv.delete(*tv.get_children())
        for row in data.fetch():
            tv.insert("", END, values=row)

    def get(event):
        select_row = tv.focus()
        data_selected = tv.item(select_row)
        global row
        row = data_selected["values"]

    # Search Bar
    def searchdata():
        search_query = search_entry.get().strip()
        if not search_query:
            messagebox.showwarning("Input Error", "Please enter a search query.", parent=tk)
            return
        if search_query:
            matching_rows = data.showmemid(search_query)
            if matching_rows:
                tv.delete(*tv.get_children())
                for row in matching_rows:
                    tv.insert("", END, values=row)
            else:
                messagebox.showinfo("Search Result", "No results found.", parent=tk)

    btn_frame = Frame(frame, bg="#4B4B4B")
    btn_frame.grid(row=9, column=0, columnspan=4, padx=10, pady=10, sticky="w")

    update_btn = Button(btn_frame, command=update, text='Return', font=("Verdana", 9, "bold"), width=12, bg='#00CEC9', fg="#2E2E2E")
    update_btn.grid(row=0, column=2,ipadx=6,ipady=2,padx=10)

    tf = Frame(tk, bg='White')
    tf.place(x=0, y=105, relwidth=1, relheight=0.7)
    tf.pack(fill=BOTH, expand=True)
    tf.pack_propagate(False)

    search_frame = Frame(tf, bg="#2E2E2E")
    search_frame.pack(side=TOP, fill=X, ipady=17)

    scrollbar = Scrollbar(tf, orient=VERTICAL, width=25)
    scrollbar.pack(side=RIGHT, fill=Y)

    search_label = Label(search_frame, text="Search Member ID:",bg ='#2E2E2E',fg="white",font=("Verdana",10,"bold"))
    search_label.place(x=30, y=7)
    search_entry = Entry(search_frame, width=40, font=("Verdana",10))
    search_entry.place(x=180, y=7)
    search_button = Button(search_frame, text="Search", command=searchdata,bg='#0984E3', fg="#2E2E2E", font=("Verdana",10,"bold"))
    search_button.place(x=570, y=5)

    all=Button(search_frame,text='Show All',command=disp,bg='#74B9FF',font=("Verdana",10,"bold"))
    all.place(x=670,y=5)


    style = ttk.Style()
    style.configure("mystyle.Treeview", font=('Calibri', 12),rowheight=35)
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,"bold"))  
    tv = ttk.Treeview(tf, columns=(1, 2, 3, 4, 5, 6), yscrollcommand=scrollbar.set,style="mystyle.Treeview")
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
    tv.heading("6", text="Fine (Rs.)")
    tv.column("6", width=1,anchor='center')
    tv['show'] = 'headings'
    tv.bind("<ButtonRelease-1>", get)
    tv.pack(fill=BOTH, expand=1)
    scrollbar.config(command=tv.yview)
    
    disp() 
    def resize(event):
        tf.config(width=event.width, height=event.height)

    tk.bind("<Configure>", resize)
    tk.mainloop()

if __name__ == "__main__":
    retnb()
