from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
window=Tk()
window.geometry('1280x700+0+0')
window.resizable(False,False)
window.title("login system of student management system")
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror("error","field cannot be empty")
    elif passwordEntry.get()=="1234" and usernameEntry.get()=="anu":
        messagebox.showinfo("success","login successful")
        window.destroy()
        import sms
    else:
        messagebox.showerror("error","please input correct info")


bgimage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window,image=bgimage)
bgLabel.place(x=0,y=0)

loginframe=Frame(window,bg='white')
loginframe.place(x=450,y=150)
logoimage=PhotoImage(file='logo.png')
logoLabel=Label(loginframe,image=logoimage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameimage=PhotoImage(file='user.png')
usernameLabel=Label(loginframe,image=usernameimage,bg='white',text='Username',compound=LEFT,font=('times new roman',20,'bold'))
usernameLabel.grid(row=1,column=0,pady=10,padx=10)
usernameEntry=Entry(loginframe,bd=5,fg='royalblue',font=('times new roman',20,'bold'))
usernameEntry.grid(row=1,column=1,pady=10,padx=10)

passwordimage=PhotoImage(file='password.png')
passwordLabel=Label(loginframe,image=passwordimage,bg='white',text='Password',compound=LEFT,font=('times new roman',20,'bold'))
passwordLabel.grid(row=2,column=0,pady=10,padx=10)
passwordEntry=Entry(loginframe,bd=5,fg='royalblue',font=('times new roman',20,'bold'))
passwordEntry.grid(row=2,column=1,pady=10,padx=10)

loginbutton=Button(loginframe,command=login,text='login',width=11,fg='white',activeforeground='white',activebackground='cornflowerblue',cursor='hand2',font=('times new roman',14,'bold'),bg='cornflowerblue')
loginbutton.grid(row=4,column=1)

window.mainloop()