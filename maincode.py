from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from books import Books
from register import MEMBERS
from returndef import retnb
from issue import issue
from registerBook import window
from datetime import date # type: ignore

db=Books('BOOK3.db')
bd=MEMBERS('member.db')
root=Tk()
root.title('Library Management System')
root.geometry("1920x1080+0+0")
root.config(bg="#2E2E2E")
root.state("zoomed")
t=StringVar()
a=StringVar()
l=StringVar()
p=StringVar()
n=StringVar()
b=StringVar()


frame=Frame(root,bg='#4B4B4B')
frame.pack(side=TOP,fill=X)
frame.place(x=0,y=0,height=500,width=2000)
head=Label(frame,text='LIBRARY MANAGEMENT SYSTEM', fg='#F5F5F5', bg='#4B4B4B',font=("Verdana", 27, "bold","italic","underline"))
head.grid(row=1, columnspan=8, pady=20)

title=Label(frame,text='Title:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
title.grid(row=2,column=0,sticky='w',padx=20)
etitle=Entry(frame,textvariable=t,fg='black',bg='white',font=("Verdana", 13),width=30)
etitle.grid(row=2,column=1,pady=10,sticky='w')

Author=Label(frame,text='Author:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
Author.grid(row=3,column=0,sticky='w',padx=20)
eauthor=Entry(frame,textvariable=a,fg='black',bg='white',font=("Verdana", 13),width=30)
eauthor.grid(row=3,column=1,pady=20,sticky='w')

lang=Label(frame,text='Language:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
lang.grid(row=4,column=0,sticky='w',padx=20)
elang=Entry(frame,textvariable=l,fg='black',bg='white',font=("Verdana", 13),width=30)
elang.grid(row=4,column=1,pady=20,sticky='w')

price=Label(frame,text='Price:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
price.grid(row=5,column=0,sticky='w',padx=20)
eprice=Entry(frame,textvariable=p,fg='black',bg='white',font=("Verdana", 13),width=30)
eprice.grid(row=5,column=1,pady=20,sticky='w')

copy=Label(frame,text='No. of copies:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
copy.grid(row=6,column=0,sticky='w',padx=20)
ecopy=Entry(frame,textvariable=n,fg='black',bg='white',font=("Verdana", 13),width=30)
ecopy.grid(row=6,column=1,pady=20,sticky='w')

disc=Label(frame,text='Description:', fg='#F5F5F5', bg="#4B4B4B", font=("Verdana", 14))
disc.grid(row=7,column=0,sticky='w',padx=20)
edisc=Entry(frame,textvariable=b,fg='black',bg='white',font=("Verdana", 13),width=30)
edisc.grid(row=7,column=1,pady=20,sticky='w')



def get(event):
    select_row=tv.focus()
    data=tv.item(select_row)
    global row
    row=data["values"]
    t.set(row[1])
    a.set(row[2])
    l.set(row[3])
    p.set(row[4])
    n.set(row[5])
    b.set(row[6])
def disp():
    sel_author.set("") 
    sel_lang.set("") 
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def add():
    if t.get()=='' or a.get()=='' or l.get()=='' or p.get()=='' or b.get()=='':
        messagebox.showerror('error','please fill all details', parent=root)
        return
    try:
        price= int(p.get())
    except ValueError:
        messagebox.showerror("Error in Input", "price should not be in text form")
        return
    try:
        noc= int(n.get())
    except ValueError:
        messagebox.showerror("Error in Input", "No. of copies should not be in text form")
        return
    
    db.insert(t.get(),a.get(),l.get(),p.get(),n.get(),b.get())
    messagebox.showinfo("Success", "Record Inserted", parent=root)
    clear()
    disp()
def update():
    if t.get()=='' or a.get()=='' or l.get()=='' or p.get()=='' or b.get()=='':
        messagebox.showerror('Success','please fill all details', parent=root)
        return
    db.update(row[0],t.get(),a.get(),l.get(),p.get(),n.get(),b.get())
    messagebox.showinfo('success','Data updated', parent=root)
    clear()
    disp()
def clear():
    t.set('')
    a.set('')
    l.set('')
    p.set('')
    n.set('')
    b.set('')
def delete():
    db.remove(row[0])
    clear()
    disp()
sel_author=StringVar()
def sel(author):
    global sel_author
    sel_author.set(author)
    both()
sel_lang=StringVar()
def sel2(language):
    global sel_lang
    sel_lang.set(language)
    both()
def both():
    tv.delete(*tv.get_children())
    language=sel_lang.get()
    author=sel_author.get()
    if author and language:
        row=db.select2(author,language)
    elif author:
        row=db.select(author)
    elif language:
        row=db.selectA(language)
    else:
        row=db.fetch()
    for rows in row:
        tv.insert("",END,values=rows)

#search Bar
def searchdata():
    search_query = search_entry.get().strip()
    if not search_query:
        messagebox.showwarning("Input Error", "Please enter a search query.")
        return
    if search_query:
        matching_rows = db.showdata(search_query)
        if matching_rows:
            tv.delete(*tv.get_children())
            for row in matching_rows:
                tv.insert("", END, values=row)
        else:
            messagebox.showinfo("Search Result", "No results found.")

#REGISTER
def reg():
    window()
#ISSUE BUTTON
def issueBook():
    issue()
#return
def returnb():
    retnb()


#--------------------------------------------------------------------------------------------
btn_frame = Frame(frame, bg='#4B4B4B')
btn_frame.grid(row=8, column=0, columnspan=4, padx=30, pady=5, sticky="w")
insert=Button(btn_frame,command=add,text='Add',bg='#00B894', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
insert.grid(row=10,column=10,padx=10,ipadx=10,ipady=2)
update=Button(btn_frame,command=update,text='Update',bg='#00CEC9', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
update.grid(row=10,column=11,padx=10,ipadx=10,ipady=2)
delete=Button(btn_frame,command=delete,text='Delete',bg='#FF7675', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
delete.grid(row=10,column=12,padx=10,ipadx=10,ipady=2)
clears=Button( btn_frame,command=clear,text='Clear',bg='#6C5CE7', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
clears.grid(row=10,column=13,padx=10,ipadx=10,ipady=2)
login=Button(btn_frame,text='Register',command=reg,bg='#FAB1A0', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
login.grid(row=10,column=14,padx=10,ipadx=10,ipady=2)
Issue=Button(btn_frame,text='Issue a book',command=issueBook,bg='#FFB142', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
Issue.grid(row=10,column=15,padx=10,ipadx=10,ipady=2)
Return=Button(btn_frame,text='Return a book',command=returnb,bg='#E17055', fg="#2E2E2E", font=("Verdana", 11, "bold"), width=12)
Return.grid(row=10,column=16,padx=10,ipadx=10,ipady=2)
#--------------------------------------------------------------------------------------------

tf=Frame(root,bg='grey')
tf.place(x=0, y=500, width=1920, height=520)
scrollbar=Scrollbar(tf,orient=VERTICAL,width=25)
scrollbar.pack(side=RIGHT,fill=Y)

search_frame=Frame(tf,bg="#2E2E2E")
search_frame.pack(side=TOP,fill=X,ipady=17)

style = ttk.Style()
style.configure("mystyle.Treeview", font=('Calibri', 12),rowheight=35)
style.configure("mystyle.Treeview.Heading", font=('Calibri', 14,"bold"))  
tv=ttk.Treeview(tf,columns=(1,2,3,4,5,6,7), yscrollcommand=scrollbar.set,style="mystyle.Treeview")
tv.heading("1", text="Book ID")
tv.column("1", width=20,anchor='center')
tv.heading("2", text="Title")
tv.column("2", width=100,anchor='w')
tv.heading("3", text="Author")
tv.column("3", width=100,anchor='w')
tv.heading("4", text="Language")
tv.column("4", width=70,anchor='w')
tv.heading("5", text="Price (Rs.)")
tv.column("5", width=20,anchor='center')
tv.heading("6", text="number of copies")
tv.column("6", width=20,anchor='center')
tv.heading("7", text="Description")
tv.column("7", width=300,anchor='w')
tv['show'] = 'headings'
tv.bind("<ButtonRelease-1>", get)


tooltip = Label(root, text="", bg="light gray", font=("Calibri", 12), wraplength=250,padx=10,pady=10)
tooltip.place_forget()  
def show_tooltip(event):
    item = tv.identify_row(event.y)
    if item:
        column = tv.identify_column(event.x)
        if column == "#7":
            description_text = tv.item(item, "values")[6] 
            tooltip.config(text=description_text)
            tooltip.place(x=event.x_root + 10, y=event.y_root + 10) 
        else:
            tooltip.place_forget()
def hide_tooltip(event):
    tooltip.place_forget()
tv.bind("<Motion>", show_tooltip)
tv.bind("<Leave>", hide_tooltip)


tv.pack(fill=BOTH, expand=1)
scrollbar.config(command=tv.yview)
disp()

#--------------------------------------------------------------------------------------------

searchA=Menubutton(search_frame,text='Author',relief=RAISED,bg='#00CEC9',font=("Verdana",10,"bold"))
searchA.place(x=1690,y=5)
searchA.menu=Menu(searchA,tearoff=0)
searchA['menu']=searchA.menu
authors = db.fetch_unique_authors()
for author in authors:
    searchA.menu.add_command(label=author, command=lambda a=author: sel(a))
searchL=Menubutton(search_frame,text='Language',relief=RAISED,bg='#00CEC9',font=("Verdana",10,"bold"))
searchL.place(x=1600,y=5)
searchL.menu=Menu(searchL,tearoff=0)
searchL['menu']=searchL.menu
languages = db.fetch_unique_languages()
for language in languages:
    searchL.menu.add_command(label=language, command=lambda l=language: sel2(l))
all=Button(search_frame,text='Show All',command=disp,bg='#74B9FF',font=("Verdana",10,"bold"))
all.place(x=1760,y=5)
search_label = Label(search_frame, text="Search Book Title:",bg ='#2E2E2E',fg="white",font=("Verdana",10,"bold"))
search_label.place(x=15, y=7)
search_entry = Entry(search_frame, width=80)
search_entry.place(x=170, y=7)
search_button = Button(search_frame, text="Search",bg='#0984E3', fg="#2E2E2E", command=searchdata,font=("Verdana",10,"bold"))
search_button.place(x=670, y=5)
#--------------------------------------------------------------------------------------------

root.mainloop()