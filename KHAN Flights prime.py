import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from datetime import date
import time
from PIL import ImageTk,Image

# MySQL Connecting:

mydb=mysql.connector.connect(host='localhost',user='root',password='nehal292004!',database='khan_flights')

# Treeview:

def treeview(page,h,px,py):

    global tree
    tree=ttk.Treeview(page,column=('#c1','#c2','#c3','#c4','#c5','#c6'),show='headings',height=h)

    tree.column('#1',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#2',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#3',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#4',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#5',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#6',width=140,minwidth=140,anchor=tk.CENTER)
    
    tree.heading('#1',text='FLIGHT NAME')
    tree.heading('#2',text='FROM CITY')
    tree.heading('#3',text='TO CITY')
    tree.heading('#4',text='BUSINESS CLASS PRICE')
    tree.heading('#5',text='DEPARTURE TIME')
    tree.heading('#6',text='ARRIVAL TIME')
    tree.place(relx=px,rely=py)

# cancel tree view

def cancelreeview(page,H,Px,Py):

    global ree
    ree=ttk.Treeview(page,column=('#c1','#c2','#c3','#c4','#c5','#c6'),show='headings',height=H)

    ree.column('#1',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#2',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#3',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#4',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#5',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#6',width=140,minwidth=140,anchor=tk.CENTER)
    
    ree.heading('#1',text='FLIGHT NAME')
    ree.heading('#2',text='FROM CITY')
    ree.heading('#3',text='TO CITY')
    ree.heading('#4',text='BUSINESS CLASS PRICE')
    ree.heading('#5',text='DEPARTURE TIME')
    ree.heading('#6',text='ARRIVAL TIME')
    ree.place(relx=Px,rely=Py)

# Login System:

def login():

    global username, password

    username=entry1.get()
    password=entry2.get()

    if (username==''or password==''):
        messagebox.showinfo('Error','Please fill the username and password')
    elif (username=='user' and password=='user'):
        messagebox.showinfo('Logged in','Logged in successfully')
        logwin.destroy()
    else:
        messagebox.showinfo('Error','Incorrect Username or Password - Try Again')


# Delete function

def delete():
    global f_no,pas
    f_no=a.get()
    pas=b.get()
    if (pas==password):
        rowcutter()
        messagebox.showinfo('cancel ticket','''                             Ticket canceled successfully
    Refund will be transferred to your SBI account in 5 minutes''')
        cancel.destroy()                 
    else:
        Label(cancel,text=('Enter a valid flight number or password'),font=('Arial',13),bg='pink').place(x=650,y=550)


# ROWCUTTER()
def rowcutter():
    
    if f_no=="bc":
        sq="delete from user where FLIGHT_NAME = 'bc'"
    elif f_no=="bh":
        sq="delete from user where FLIGHT_NAME = 'bh'"
    elif f_no=="bm":
        sq="delete from user where FLIGHT_NAME = 'bm'"   
    elif f_no=="cb":
        sq="delete from user where FLIGHT_NAME = 'cb'"
    elif f_no=="ch":
        sq="delete from user where FLIGHT_NAME = 'ch'"      
    elif f_no=="cm":  
        sq="delete from user where FLIGHT_NAME = 'cm'"         
    elif f_no=="hb": 
        sq="delete from user where FLIGHT_NAME = 'hb'"     
    elif f_no=="hc":
        sq="delete from user where FLIGHT_NAME = 'hc'"
    elif f_no=="hm":
        sq="delete from user where FLIGHT_NAME = 'hm'"
    elif f_no=="mb":  
        sq="delete from user where FLIGHT_NAME = 'mb'"
    elif f_no=="mc":
        sq="delete from user where FLIGHT_NAME = 'mc'"
    elif f_no=="mh":
        sq="delete from user where FLIGHT_NAME = 'mh'"

    mcursor=mydb.cursor()
    mcursor.execute(sq)
    mydb.commit()
    

# Profile Page:

def profilepage():

    userprof=tk.Toplevel()
    userprof.geometry('1366x768')
    userprof.title('Khan Flights - user Profile')
    userprof.state('zoomed')
 

    profpic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\NK FLIGHT.png"))
    profpanel=Label(userprof,image=profpic)
    profpanel.pack(side='top',fill='both',expand='yes')
    
    Label(userprof,text=('Business Class Account'),font=('Arial',16),bg='Lightsteelblue2').place(x=1080,y=50)  
    Label(userprof,text=(username),font=('Arial',16),bg='Lightsteelblue2').place(x=1080,y=100)
    Label(userprof,text=("Email : nehal292004@gmail.com"),font=('Arial',16),bg='Lightsteelblue2').place(x=1080,y=150)
    Label(userprof,text=("mobile : +91 8438394310"),font=('Arial',16),bg='Lightsteelblue2').place(x=1080,y=200)

    Label(userprof,text=('YOUR BOOKED FLIGHTS'),font=('Arial',15),bg='white').place(relx=0.1,rely=0.665)

    cancelreeview(userprof,6,0.1,0.7)

    global ROWS
    mycur=mydb.cursor()
    mycur.execute('SELECT * FROM user')
    ROWS=mycur.fetchall()
    for ROW in ROWS:
        ree.insert('',tk.END,values=ROW)

    userprof.mainloop()

# bookpageing Page:

def bookpage():

    book=tk.Toplevel()
    book.geometry('1366x768')
    book.title('Khan Flights - bookpage')
    book.state('zoomed')

    Label(book,text=('Business Class Account'),font=('Arial',16),bg='Lightsteelblue2').place(x=1080,y=50)

    bookpagepic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\NK FLIGHT.png"))
    bookpagepanel=Label(book,image=bookpagepic)
    bookpagepanel.pack(side='top',fill='both',expand='yes')

    Label(book,text='AVAILABLE FLIGHTS',bg='pink',fg='black',font=('Arial',25),borderwidth=1,
          relief='solid').place(relx=0.065,rely=0.14)

    Label(book,text='FROM',font=('Arial',16)).place(relx=0.065,rely=0.6)
    Label(book,text='TO',font=('Arial',16)).place(relx=0.065,rely=0.75)

    treeview(book,12,0.065,0.2)

    global rows
    mycur=mydb.cursor()
    mycur.execute('SELECT * FROM Flights')
    rows=mycur.fetchall()
    for row in rows:
        tree.insert('',tk.END,values=row)

    fromlist=['select']
    fromselect='SELECT DISTINCT(FROM_CITY) FROM Flights'
    mycur.execute(fromselect)
    fromdata=mycur.fetchall()
    for i in fromdata:
        fromlist.append(str(i[0]))
            
    tolist=['select']
    toselect='SELECT DISTINCT(TO_CITY) FROM Flights'
    mycur.execute(toselect)
    todata=mycur.fetchall()
    for j in todata:
        tolist.append(str(j[0]))

    def cbupdate1(*args):
        global f
        f=frombox.get()

    def cbupdate2(*args):
        global t
        t=tobox.get()

    def billing():
        global billwin

        def insert():
                sql='''insert into user(FLIGHT_NAME, FROM_CITY, TO_CITY, BUISNESS_CLASS_PRICE, DEPARTURE_TIME, ARRIVAL_TIME) 
                values(%s,%s,%s,%s,%s,%s)'''
                mycur.execute(sql,r)
                mydb.commit()
                messagebox.showinfo('Booked','Flight booked successfully')
                billwin.destroy()
                book.destroy()

        if messagebox.askokcancel('Confirm Booking','Do you want to book this flight?',parent=book):
            billwin=tk.Toplevel()
            billwin.title('Khan FLIGHTS - BILLING')
            billwin.geometry('600x354')
            billwin.resizable(False,False)
            billwin.protocol('WM_DELETE_WINDOW',billclose)

            billwinpic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\transaction.jpg"))
            billwinpanel=Label(billwin,image=billwinpic)
            billwinpanel.pack(side='top',fill='both',expand='yes')

            Label(billwin,text=('Username :',username),font=('Arial',12),bg='lavenderblush').place(x=20,y=150)
            Label(billwin,text=('UserID :',username),font=('Arial',12),bg='lavenderblush').place(x=20,y=180)
            Label(billwin,text=('Flight Name : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=210)
            Label(billwin,text=(r[0]),font=('Arial',12),bg='lavenderblush').place(x=120,y=210)
            Label(billwin,text=('From : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=240)
            Label(billwin,text=(f),font=('Arial',12),bg='lavenderblush').place(x=70,y=240)
            Label(billwin,text=('To : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=270)
            Label(billwin,text=(t),font=('Arial',12),bg='lavenderblush').place(x=50,y=270)
            Label(billwin,text=('Amount : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=300)
            Label(billwin,text=(p),font=('Arial',12),bg='lavenderblush').place(x=90,y=300)

            Button(billwin,text='Pay Now',font=('Arial',16),command=insert,height=1,width=16,bg='DarkOrchid1',
            fg='gray6',activebackground='gray12',activeforeground='thistle1').place(x=250,y=260)

            billwin.mainloop()

    def findflight():
        global rows,r,p,f,t

        mycur=mydb.cursor()
        mycur.execute('SELECT * FROM Flights')
        rows=mycur.fetchall()

        def booknone():
            Label(book,text='Select a valid destination',font=('Arial',16),bg='pink').place(relx=0.5,rely=0.66)
            

        def fftv(r):
            tree.insert('',tk.END,values=r)

        if f=='bangalore' and t=='chennai':
            r=list(rows[0])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='bangalore' and t=='hyderabad':
            r=list(rows[1])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='bangalore' and t=='mumbai':
            r=list(rows[2])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='chennai' and t=='bangalore':
            r=list(rows[3])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='chennai' and t=='hyderabad':
            r=list(rows[4])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='chennai' and t=='mumbai':
            r=list(rows[5])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='hyderabad' and t=='bangalore':
            r=list(rows[6])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='hyderabad' and t=='chennai':
            r=list(rows[7])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='hyderabad' and t=='mumbai':
            r=list(rows[8])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='mumbai' and t=='bangalore':
            r=list(rows[9])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='mumbai' and t=='chennai':
            r=list(rows[10])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)

        elif f=='mumbai' and t=='hyderabad':
            r=list(rows[11])
            treeview(book,1,0.3,0.65)
            fftv(r)
            p=r[3]
            Button(book,text='Book Now',font=('Arial',16),command=billing,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)
        

        else:
                
            Label(book,text='Select a valid destination',font=('Arial',16),bg='tomato3').place(relx=0.5,rely=0.66)
            Button(book,text='Book Now',font=('Arial',16),command=booknone,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)


    sv1=tk.StringVar()
    sv2=tk.StringVar()

    frombox=ttk.Combobox(book,state='readonly',textvariable=sv1,font=('Arial',16),width=20)
    frombox['values']=fromlist
    frombox.place(relx=0.065,rely=0.65)
    frombox.current(0)
        
    tobox=ttk.Combobox(book,state='readonly',textvariable=sv2,font=('Arial',16),width=20)
    tobox['values']=tolist
    tobox.place(relx=0.065,rely=0.8)
    tobox.current(0)

    sv1.trace('w',cbupdate1)
    sv2.trace('w',cbupdate2)
  
    Button(book,text='Find a flight',font=('Arial',16),command=findflight,height=1,width=16,bg='Lightsteelblue2',
    fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.09,rely=0.87)


   
    book.mainloop()

# Canceling Page:

def cancelpage():

    global cancel

    cancel=tk.Toplevel()
    cancel.geometry('1366x768')
    cancel.title('Khan Flights - Cancel')
    cancel.state('zoomed')

    Label(cancel,text=('Business Class Account'),font=('Arial',16),bg='snow3').place(x=1080,y=50)



    cancelpic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\NK FLIGHT.png"))
    cancelpanel=Label(cancel,image=cancelpic)
    cancelpanel.pack(side='top',fill='both',expand='yes')

    cancelreeview(cancel,6,0.065,0.2)

    global ROWS
    mycur=mydb.cursor()
    mycur.execute('SELECT * FROM user')
    ROWS=mycur.fetchall()
    for ROW in ROWS:
        ree.insert('',tk.END,values=ROW)

    Label(cancel,text="FLIGHT NAME TO BE CANCELED",bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=500)

    Label(cancel,text='ACCOUNT PASSWORD',bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=550)

    global a,b

    a=Entry(cancel)
    a.place(x=350,y=500)
    a.config(borderwidth=2,relief='sunken')

    b=Entry(cancel)
    b.place(x=350,y=550)
    b.config(borderwidth=2,relief='sunken')
    b.config(show='*')

    Button(cancel,text='Cancel Flight ticket',font=('Arial',15),command=delete,height=1,width=20,bg='pink').place(x=350,y=600)

    cancel.mainloop()

# About Page:

def aboutpage():

    about=tk.Toplevel()
    about.geometry('1366x768')
    about.title('Khan Flights - About')
    about.state('zoomed')

    aboutpic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\NK FLIGHT.png"))
    aboutpanel=Label(about,image=aboutpic)
    aboutpanel.pack(side='top',fill='both',expand='yes')

    def help():
        Label(about,text='''COSTUMER SERVICE NUMBER : Like hell I would give it to you (INDIA)''',font=('Arial',16)).place(x=750,y=550)

    Button(about,text='Contact Us',font=('Arial',20),command=help,height=1,width=16,bg='Lightsteelblue2',
    fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(x=800,y=500)

    Label(about,text=('''This program is created by Nehal Khan on 13 January 2023. With the help 
    of online classes, our mentors, and our beloved friends we were able to create this program successfuly'''),font=('Arial',15),bg='Lightsteelblue2').place(x=250,y=50)

    Label(about,text=(""),font=('Arial',16),bg='pink').place(x=150,y=345)

    Label(about,text=('''     DISCLAIMER     
    THE INFORMATION GIVEN ABOVE IN PROJECT ARE FAKE AND 
    ONLY FOR PROJECT USE'''),font=('Arial',16),bg='pink').place(x=750,y=400)


    about.mainloop()

# Page Close Confirmations (Messagebox):

def homelogout():

    messagebox.showinfo('Thank You','Logged out successfully')
    home.destroy()

def billclose():
     if messagebox.askokcancel('Quit','Do you want to quit?'):
        billwin.destroy()

def logclose():

    if messagebox.askokcancel('Quit','Do you want to quit?'):
        logwin.destroy()
        quit()
        
def homeclose():

    if messagebox.askokcancel('Quit','Do you want to logout and quit?'):
        home.destroy()
        quit()

# Login Page:

logwin=tk.Tk()
logwin.title('KHAN FLIGHTS - LOGIN')
logwin.geometry('400x120')
logwin.resizable(False,False)
logwin.protocol('WM_DELETE_WINDOW',logclose)

logwinpic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\nk login.png"))
logwinpanel=Label(logwin,image=logwinpic)
logwinpanel.pack(side='top',fill='both',expand='yes')

Label(logwin,text='USERNAME:',bg='snow3',font=('Arial',12),borderwidth=1,relief='solid').place(x=80,y=24)
Label(logwin,text='PASSWORD:',bg='snow3',font=('Arial',12),borderwidth=1,relief='solid').place(x=80,y=54)

global entry1,entry2

entry1=Entry(logwin)
entry1.place(x=200,y=25)
entry1.config(borderwidth=2,relief='sunken')

entry2=Entry(logwin)
entry2.place(x=200,y=55)
entry2.config(borderwidth=2,relief='sunken')
entry2.config(show='*')

Button(logwin,text='Login',command=login,height=1,width=10).place(x=220,y=85)

logwin.mainloop()

# Home Page:

home=tk.Tk()
home.geometry('1366x768')
home.title('Khan Flights')
home.state('zoomed')
home.protocol('WM_DELETE_WINDOW',homeclose)

currtime=time.strftime('%H:%M')
currdate=date.today().strftime("%d/%m/%Y")

homepic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\NK FLIGHT.png"))
homepanel=Label(home,image=homepic)
homepanel.pack(side='top',fill='both',expand='yes')

Label(home,text=('Business Class Account'),font=('Arial',16),bg='Lightsteelblue2').place(x=1050,y=50) 
Label(home,text=(username),font=('Arial',16),bg='Lightsteelblue2').place(x=1050,y=150) 
Label(home,text=('Logged in: '+currtime+', '+currdate),font=('Arial',16),bg='pink').place(x=1050,y=100)

Label(home,text=('''Disclaimer --- This project is totally offline and fake. This project do not indicate 
                 the original Khan flight company and its softwares. This is just for project purpose and not for
                 publishing anywhere...'''),
                 font=('Arial',12),bg='Lightsteelblue2',borderwidth=1,relief='solid').place(relx=0.25,rely=0.85)

Button(home,text='Your Profile',font=('Arial',20),command=profilepage,height=1,width=16,bg='Lightsteelblue2',
       fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(x=650,y=320)
Button(home,text='Book Flight',font=('Arial',20),command=bookpage,height=1,width=16,bg='Lightsteelblue2',
       fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(x=1030,y=320)
Button(home,text='Cancel Flight',font=('Arial',20),command=cancelpage,height=1,width=16,bg='Lightsteelblue2',
       fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(x=650,y=480)
Button(home,text='About Us',font=('Arial',20),command=aboutpage,height=1,width=16,bg='Lightsteelblue2',
       fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(x=1030,y=480)
Button(home,text='Logout',font=('Arial',20),command=homelogout,height=1,width=10,bg='pink').place(x=1100,rely=0.85)

home.mainloop()
