from tkinter import *
import time
from PIL import ImageTk
import pandas
import pymysql
import ttkthemes
from tkinter import ttk,messagebox,filedialog
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1080x700+100+0')
root.resizable(False,False)
root.title("student management system")
count=0
text=""
def slider():
    global text,count
    if count==len(s):
        count=0
        text=""
    text+=s[count]
    sliderlabel.config(text=text)
    count+=1
    sliderlabel.after(100,slider)
def clock():
    global date,currentime
    date=time.strftime('%d/%m/%Y')
    currentime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'    Date:{date}\nTime:{currentime}')
    datetimeLabel.after(1000,clock)
datetimeLabel=Label(root,font=('times new roman',20,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s="Student Management System"
sliderlabel=Label(root,font=('times new roman',18,'bold'))
sliderlabel.place(x=300,y=0)
slider()


def update_data():


    query = 'update student set name=%s,phone=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query, (nameEntry.get(), phoneEntry.get(), emailEntry.get(), addressEntry.get(), genderEntry.get(), dobEntry.get(), date,currentime, idEntry.get()))
    conn.commit()
    messagebox.showinfo('success', f'Id {idEntry.get()} is modified', parent=screen)
    screen.destroy()
    show_student()


def toplevel_data(title,button_text,command):
    global idEntry,phoneEntry,emailEntry,nameEntry,addressEntry,genderEntry,dobEntry,screen
    screen = Toplevel()
    screen.title(title)
    screen.resizable(False, False)
    screen.grab_set()
    idLabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'), foreground='red')
    idLabel.grid(row=0, column=0, padx=30, pady=15)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(screen, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15)
    phoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(screen, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    screen_button = ttk.Button(screen, text=button_text, command=command)
    screen_button.grid(row=7, columnspan=2, pady=15)

    if title=='update student':
        indexing = studenttable.focus()
        content = studenttable.item(indexing)
        listdata = content['values']
        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])


def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for data in fetched_data:
        studenttable.insert("", END, values=data)

def delete_student():
    indexing=studenttable.focus()
    content=studenttable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    conn.commit()
    messagebox.showinfo("deleted",f'Id {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for data in fetched_data:
        studenttable.insert("",END,values=data)



def export():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studenttable.get_children()
    newlist=[]
    for index in indexing:
        content=studenttable.item(index)
        datalist=content['values']
        print(datalist)
        print(type(datalist))
        newlist.append(datalist)

    table=pandas.DataFrame(newlist,columns=['Id','name','phone','email','address','gender','dob','date','time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success f','Data is saved successfully')


def exit():
    result=messagebox.askyesno('confirm','Do you want to exit')
    if result:
        root.destroy()
    else:
        pass







def search_data():
    query="select * from student where id=%s or name=%s  or phone=%s or email=%s or address=%s or gender=%s or dob=%s"
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    fetched_data=mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for data in fetched_data:
        studenttable.insert("",END,values=data)







def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or  emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror("error","all fields are required",parent=screen)
    else:
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currentime))
            conn.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form? ')
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0, END)
                phoneEntry.delete(0, END)
                emailEntry.delete(0, END)
                addressEntry.delete(0, END)
                dobEntry.delete(0,END)
                genderEntry.delete(0,END)
        except:
            messagebox.showerror("error","id cannot be repeated",parent=screen)
            return

        query="select * from student"
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for data in fetched_data:
            datalist=list(data)
            studenttable.insert("",END,values=datalist)

    

def connect_database():
    def connect():
        global mycursor,conn
        try:
            conn=pymysql.connect(host='localhost',user='root',password='as42DF*&15G!68hj')
            mycursor=conn.cursor()
            #messagebox.showinfo("Succes","database Connection is success=ful",parent=connectwindow)
        except:
            messagebox.showerror("error","invalid details")
            return
        try:
            query='create database student_management_system'
            mycursor.execute(query)
            query='use student_management_system'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),phone varchar(30),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),date varchar(20),time varchar(20))'
            mycursor.execute(query)
        except:
            query = 'use student_management_system'
            mycursor.execute(query)
        messagebox.showinfo('success','Database Connection is successful',parent=connectwindow)
        connectwindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        upstudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportButton.config(state=NORMAL)
        delstudentButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)



    connectwindow=Toplevel()
    connectwindow.geometry('470x250+630+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(False,False)

    hostnameLabel=Label(connectwindow,text="Host name",font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)
    hostentry=Entry(connectwindow,font=('arial',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=10,pady=20)

    usernameLabel = Label(connectwindow, text="User name", font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0,padx=20)
    userentry = Entry(connectwindow,bd=2, font=('arial', 15, 'bold'))
    userentry.grid(row=1, column=1, padx=10, pady=20)

    passwordLabel = Label(connectwindow, text="Password", font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)
    passwordentry = Entry(connectwindow, bd=2, font=('arial', 15, 'bold'))
    passwordentry.grid(row=2, column=1, padx=10, pady=20)

    connectButton=ttk.Button(connectwindow,text='Connect',command=connect)
    connectButton.grid(row=3,columnspan=2)


connectButton=ttk.Button(root,text="connect database",command=connect_database)
connectButton.place(x=900,y=0)


leftframe=Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)

logo_image=ImageTk.PhotoImage(file='student.png')
logo_label=Label(leftframe,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftframe,text="add student",width=25,state=DISABLED,command=lambda :toplevel_data('add student','ADD STUDENT',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftframe,text="search student",width=25,state=DISABLED,command=lambda:toplevel_data('search student','SEARCH STUDENT',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

delstudentButton=ttk.Button(leftframe,text="delete student",width=25,state=DISABLED,command=delete_student)
delstudentButton.grid(row=3,column=0,pady=20)


upstudentButton=ttk.Button(leftframe,text="update student",width=25,state=DISABLED,command=lambda:toplevel_data('update student','UPDATE',update_data))
upstudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftframe,text="show student",width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportButton=ttk.Button(leftframe,text="Export data",width=25,state=DISABLED,command=export)
exportButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftframe,text="Exit",width=25,state=DISABLED,command=exit)
exitButton.grid(row=7,column=0,pady=20)

rightframe=Frame(root)
rightframe.place(x=300,y=80,width=750,height=600)
scrollbarx=Scrollbar(rightframe,orient=HORIZONTAL)
scrollbary=Scrollbar(rightframe,orient=VERTICAL)
studenttable=ttk.Treeview(rightframe,columns=('Id','Name','phone','Email','Address','Gender','D.O.B','Added Date','Added Time'),xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
scrollbarx.config(command=studenttable.xview)
scrollbary.config(command=studenttable.yview)
scrollbarx.pack(side=BOTTOM,fill=X)
scrollbary.pack(side=RIGHT,fill=Y)
studenttable.pack(fill=BOTH,expand=1)

studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('phone',text='phone')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='DoB')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable.config(show='headings')

studenttable.column('Id',width=50,anchor=CENTER)
studenttable.column('Name',width=300,anchor=CENTER)
studenttable.column('phone',width=300,anchor=CENTER)
studenttable.column('Email',width=300,anchor=CENTER)
studenttable.column('Address',width=300,anchor=CENTER)
studenttable.column('Gender',width=100,anchor=CENTER)
studenttable.column('D.O.B',width=100,anchor=CENTER)
studenttable.column('Added Date',width=100,anchor=CENTER)
studenttable.column('Added Time',width=100,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),background='white',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'))






root.mainloop()


