from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import re
import sqlite3 as sql
# con=sql.connect(host="localhost",user='root',password='root',database='billManagementSystem')
con=sql.connect(database='billManagementSystem.sqlite')
cursor=con.cursor()
cursor.execute("create table if not exists registration(name varchar(20),username varchar(20) primary key,gmailid varchar(50),password varchar(30))")
def clearEntry():
            nameEntry.delete(first=0,last=100)
            usernameEntry.delete(first=0,last=100)
            gmailEntry.delete(first=0,last=100)
            passwordEntry.delete(first=0,last=100)
            repasswordEntry.delete(first=0,last=100)
def error():
            messagebox.showerror("Error","password  not same")    
def insert():
    name=nameEntry.get()
    user=usernameEntry.get()
    gmail=gmailEntry.get()
    email="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
   
    password=passwordEntry.get()
    repassword=repasswordEntry.get()
    #insert="insert into registration values('%s','%s','%s','%s')"%(name,user,gmail,password);
    # values=(nameEntry.get(),usernameEntry.get(),gmailEntry.get(),passwordEntry.get())
    if(name=='' or user==''or gmail=='' or password=='' or repassword==''):
        messagebox.showwarning('Warning',"Field Can't be empty")
    elif(password !=repassword):
        messagebox.showwarning('Warning'," password EntryField Can't be matched")
    else: 
        #gmail verification  
        if(re.search(email,gmail)):
            insertData="insert into registration(name,username,gmailid,password) values(?,?,?,?)"
            values=(name,user,gmail,password)
            c=cursor.execute(insertData,values)
            con.commit()        
            clearEntry()
            messagebox.showinfo("Database Created","your data inserted")
        else:
            messagebox.showwarning('Warning',"Wrong Email Id")

       

def signin():
    window.destroy()
    import login

#root
window=Tk()
window.geometry('1280x700+0+0')
window.title("Registration Of Admin")
window.resizable(False,False)
#background
backgroundImage=ImageTk.PhotoImage(file='images/reg.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

#frame
signupFrame=Frame(window,bg='white')
signupFrame.place(x=400,y=150)

logoImage=PhotoImage(file='images/login.png')
logoLabel=Label(signupFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

#name
namelabel=Label(signupFrame,text='Name',
font=('times new roman',20,'bold'),bg='white')
namelabel.grid(row=1,column=0,padx=20,pady=10,sticky='w')

nameVar=StringVar()
nameEntry=Entry(signupFrame,textvariable=nameVar,font=('times new roman',17),bd=5,fg='royalblue')
nameEntry.grid(row=1,column=1,padx=20,pady=10)
#username

usernamelabel=Label(signupFrame,text='User Name',
font=('times new roman',20,'bold'),bg='white')
usernamelabel.grid(row=2,column=0,padx=20,pady=10,sticky='w')

usernameVar=StringVar()
usernameEntry=Entry(signupFrame,textvariable=usernameVar,font=('times new roman',17),bd=5,fg='royalblue')
usernameEntry.grid(row=2,column=1,padx=20,pady=10)

#gmail 
gmaillabel=Label(signupFrame,text='Gmail ID',
font=('times new roman',20,'bold'),bg='white')
gmaillabel.grid(row=3,column=0,padx=20,pady=10,sticky='w')

gmailVar=StringVar()
gmailEntry=Entry(signupFrame,textvariable=gmailVar,font=('times new roman',17),bd=5,fg='royalblue')
gmailEntry.grid(row=3,column=1,padx=20,pady=10)

#password
passwordlabel=Label(signupFrame,text='Password',
font=('times new roman',20,'bold'),bg='white')
passwordlabel.grid(row=4,column=0,padx=20,pady=10,sticky='w')

passwordVar=StringVar()
passwordEntry=Entry(signupFrame,textvariable=passwordVar,font=('times new roman',17),bd=5,fg='royalblue',show="*")
passwordEntry.grid(row=4,column=1,padx=20,pady=10)

repasswordlabel=Label(signupFrame,text='Re-Password',
font=('times new roman',20,'bold'),bg='white')
repasswordlabel.grid(row=5,column=0,padx=20,pady=10,sticky='w')

repasswordVar=StringVar()
repasswordEntry=Entry(signupFrame,textvariable=repasswordVar,font=('times new roman',17),bd=5,fg='royalblue',show="*")
repasswordEntry.grid(row=5,column=1,padx=20,pady=10)
#registration
signupButton=Button(signupFrame,text="Register",command=insert,font=('time new roman',14,'bold'),
width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2')
signupButton.grid(row=6,column=0,pady=10)

loginButton=Button(signupFrame,text="Sign In",font=('time new roman',14,'bold'),
width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=signin)
loginButton.grid(row=6,column=1,pady=10)

#display for infinite times
window.mainloop()