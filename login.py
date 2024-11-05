from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3 as sql

try:
    con=sql.connect(database='billManagementSystem.sqlite')
except:
    print("Connection is not created")
cursor=con.cursor()
#log in
def logIn():
    s=usernameEntry.get()
    


    select="select username,password from registration where username=? and password=?"
    values=(usernameEntry.get(),passwordEntry.get())
    e=cursor.execute(select,values)
    resultSet=e.fetchall()
    if(usernameEntry.get()=='' or passwordEntry==''):
        messagebox.showerror('Error',"Field Can't be empty")
    elif(resultSet):
    # elif(usernameEntry.get()=="vikas" or passwordEntry.get()=='1234'):
        messagebox.showinfo('Success',"Welcome")
        #close login window after login
        window.destroy()
        import bill        
    else:
        messagebox.showerror('Error',"Please Enter correct login info")

def signUp():
    window.destroy()
    import adminreg
window=Tk()
window.geometry('1280x700+0+0')
window.title("Log In Billing Management System")
window.resizable(False,False)
backgroundImage=ImageTk.PhotoImage(file='images/login-bg.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

#frame
loginFrame=Frame(window,bg ='white')
loginFrame.place(x=400,y=150)
# Load Image
logoImage=ImageTk.PhotoImage(file='images/login.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)


usernameImage=ImageTk.PhotoImage(file='images/stu.png')
#username

usernamelabel=Label(loginFrame,image=usernameImage,text='Username',
compound=LEFT,font=('times new roman',20,'bold'),bg='white')
usernamelabel.grid(row=1,column=0,padx=20,pady=10)

usernameEntry=Entry(loginFrame,font=('times new roman',20),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,padx=20,pady=10)

#password
passwordImage=PhotoImage(file='images/pwd.png')
passwordlabel=Label(loginFrame,image=passwordImage,text='Password',
compound=LEFT,font=('times new roman',20,'bold'),bg='white')
passwordlabel.grid(row=2,column=0,padx=20,pady=10)

passwordEntry=Entry(loginFrame,font=('times new roman',20),bd=5,fg='royalblue',show="*")
passwordEntry.grid(row=2,column=1,padx=20,pady=10)

signupButton=Button(loginFrame,text="Sign Up",font=('time new roman',12,'bold'),width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=signUp)
signupButton.grid(row=3,column=0,pady=10)

loginButton=Button(loginFrame,text="Log In",font=('time new roman',12,'bold'),
width=15,fg='white',bg='cornflowerblue',activeforeground='red',cursor='hand2',command=logIn)
loginButton.grid(row=3,column=1,pady=10)
window.mainloop()
# if(__name__=='__main__'):
#     user=usernameEntry.get()