import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
from datetime import date
import datetime
import time
from PIL import ImageTk,Image

# MySQL Connecting:

mydb=mysql.connector.connect(host='localhost',user='root',password='nehal292004!',database='khan_flights')

mcursor = mydb.cursor()
update_query = "UPDATE flights SET FLIGHT_DATE = %s"
current_date = date.today()
mcursor.execute(update_query, (current_date,))
mydb.commit()


# Treeview:

def treeview(page,h,px,py):

    global tree
    tree=ttk.Treeview(page,column=('#c1','#c2','#c3','#c4','#c5','#c6','#c7','#c8'),show='headings',height=h)

    tree.column('#1',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#2',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#3',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#4',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#5',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#6',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#7',width=140,minwidth=140,anchor=tk.CENTER)
    tree.column('#8',width=140,minwidth=140,anchor=tk.CENTER)
    
    tree.heading('#1',text='FLIGHT NAME')
    tree.heading('#2',text='FROM CITY')
    tree.heading('#3',text='TO CITY')
    tree.heading('#4',text='BUSINESS CLASS PRICE')
    tree.heading('#5',text='DEPARTURE TIME')
    tree.heading('#6',text='ARRIVAL TIME')
    tree.heading('#7',text='FLIGHT DATE')
    tree.heading('#8',text='AVAILABLE SEATS')
    tree.place(relx=px,rely=py)
    
    
def treview(page,h,px,py):

    global tre
    
    tre=ttk.Treeview(page,column=('#c1','#c2','#c3','#c4','#c5','#c6','#c7','#c8','#c9','#c10','#c11','#c12','#c13'),show='headings',height=h)

    tre.column('#1',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#2',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#3',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#4',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#5',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#6',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#7',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#8',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#9',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#10',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#11',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#12',width=100,minwidth=100,anchor=tk.CENTER)
    tre.column('#13',width=100,minwidth=100,anchor=tk.CENTER)

    

    tre.heading('#1',text='NAME 1')
    tre.heading('#2',text='NAME 2')
    tre.heading('#3',text='NAME 3')
    tre.heading('#4',text='NAME 4')
    tre.heading('#5',text='AGE 1')
    tre.heading('#6',text='AGE 2')
    tre.heading('#7',text='AGE 3')
    tre.heading('#8',text='AGE 4')
    tre.heading('#9',text='FLIGHT NAME')
    tre.heading('#10',text='FLIGHT DATE')
    tre.heading('#11',text='PHONE')
    tre.heading('#12',text='EMAIL')
    tre.heading('#13',text='SEATS')
    
    tre.place(relx=px,rely=py)

# cancel tree view

def cancelreeview(page,H,Px,Py):

    global ree
    ree=ttk.Treeview(page,column=('#c1','#c2','#c3','#c4','#c5','#c6','#c7'),show='headings',height=H)

    ree.column('#1',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#2',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#3',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#4',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#5',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#6',width=140,minwidth=140,anchor=tk.CENTER)
    ree.column('#7',width=140,minwidth=140,anchor=tk.CENTER)
    
    ree.heading('#1',text='FLIGHT NAME')
    ree.heading('#2',text='FROM CITY')
    ree.heading('#3',text='TO CITY')
    ree.heading('#4',text='BUSINESS CLASS PRICE')
    ree.heading('#5',text='DEPARTURE TIME')
    ree.heading('#6',text='ARRIVAL TIME')
    ree.heading('#7',text='FLIGHT DATE')
    ree.place(relx=Px,rely=Py)

# Login System:

def login():

    global username, password

    username=entry1.get()
    password=entry2.get()

    if (username == '' or password == ''):
            messagebox.showinfo('Error', 'Please fill the username and password')
    else:
        mcursor = mydb.cursor()
        query_check = "SELECT * FROM accounts WHERE USERNAME='{}' AND PASSWORD='{}'".format(username, password)
        mcursor.execute(query_check)
        existing_user = mcursor.fetchone()

        if existing_user:
            messagebox.showinfo('Logged in', 'Logged in successfully')
            logwin.destroy()
        else:
            messagebox.showinfo('Error', 'Incorrect Username or Password - Try Again')


# Delete function

def delete():
    global f_no,pas,flight_found,da
    f_no=a.get()
    pas=b.get()
    da=d.get()
    if (pas==password):
        rowcutter()
        if flight_found:  
            messagebox.showinfo('cancel ticket','''                             Ticket canceled successfully
    Refund will be transferred to your SBI account in 5 minutes''')
            cancel.destroy()       
        else:
            cancel.destroy()       
    else:
        Label(cancel,text=('Enter a valid flight number or password'),font=('Arial',13),bg='pink').place(x=650,y=550)
        


# ROWCUTTER()
def rowcutter():
          
    global ROWS,flight_found
    
    sql_query = "SELECT * FROM flights WHERE Flight_name='{}' AND Flight_date = '{}'".format(f_no, da)
    mycur=mydb.cursor()
    mycur.execute(sql_query)
    ro = mycur.fetchone()
        
    sql_query = "SELECT * FROM passengers WHERE Group_ID = '{}' AND Flight_name='{}' AND Flight_date = '{}'".format(username,f_no, da)
    mycur=mydb.cursor()
    mycur.execute(sql_query)
    i = mycur.fetchone()

    if ro[0]==f_no and ro[6]==datetime.date(int(da[0:4]), int(da[5:7]), int(da[8:])):
        sql="update flights set available_seats = {} where Flight_name = '{}' and Flight_date = '{}'".format(ro[7]+i[13],f_no,da)
        mycur.execute(sql)
        mydb.commit()
    
    
    mycur=mydb.cursor()
    q = "select * from {}".format(username)
    mycur.execute(q)
    ROWS=mycur.fetchall()
    flight_found = False
    for row in ROWS:
        #print(row)
        if row[0] == f_no and row[6] == datetime.date(int(da[0:4]), int(da[5:7]), int(da[8:])):
            flight_found = True
            sq = "DELETE FROM {} WHERE FLIGHT_NAME = '{}' AND FLIGHT_DATE = '{}'".format(username, f_no, da)
            mcursor = mydb.cursor()
            mcursor.execute(sq)
            mydb.commit()
            
    q1 = "select * from passengers"
    mycur.execute(q1)
    ROWS=mycur.fetchall()
    for row in ROWS:
        if row[0] == username and row[10] == datetime.date(int(da[0:4]), int(da[5:7]), int(da[8:])):
            sq = "DELETE FROM passengers WHERE Group_ID = '{}' AND  Flight_name = '{}' AND Flight_date = '{}'".format(username, f_no, da)
            mcursor = mydb.cursor()
            mcursor.execute(sq)
            mydb.commit()

    if not flight_found:
        messagebox.showerror('Error', 'No flight found')
        
    
                



# Profile Page:

def profilepage():

    userprof=tk.Toplevel()
    userprof.geometry('1366x768')
    userprof.title('Khan Flights - user Profile')
    userprof.state('zoomed')
 

    profpic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\NK FLIGHT.png"))
    profpanel=Label(userprof,image=profpic)
    profpanel.pack(side='top',fill='both',expand='yes')
    
    Label(userprof,text=('Business Class Account'),font=('Arial',16),bg='Lightsteelblue2').place(x=1180,y=50)  
    Label(userprof,text=(username),font=('Arial',16),bg='Lightsteelblue2').place(x=1180,y=100)
    Label(userprof,text=(currdate),font=('Arial',16),bg='Lightsteelblue2').place(x=1180,y=150)

    Label(userprof,text=('YOUR BOOKED FLIGHTS'),font=('Arial',15),bg='white').place(relx=0.07,rely=0.1)
    cancelreeview(userprof,6,0.07,0.17)
    Label(userprof,text=('YOUR TICKET'),font=('Arial',15),bg='white').place(relx=0.07,rely=0.4)
    treview(userprof,6,0.07,0.47)

    global ROWS
    mycur=mydb.cursor()
    q= "select * from {}".format(username)
    mycur.execute(q)
    ROWS=mycur.fetchall()
    for ROW in ROWS:
        ree.insert('',tk.END,values=ROW)
        
    q= "select * from passengers where group_id ='{}'".format(username)
    mycur.execute(q)
    RO=mycur.fetchall()
    for R in RO:
        val = R[1:]
        tre.insert('',tk.END,values=val)

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

    def addpeople():
        global addpwin,n1,n2,n3,n4,a1,a2,a3,a4,e,ph
        
        addpwin=tk.Toplevel()
        addpwin.title('Khan FLIGHTS - Add Passengers')
        addpwin.geometry('1366x768')
        addpwin.state('zoomed')
        addpwin.protocol('WM_DELETE_WINDOW',addpclose)

        addpwinpic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\NK FLIGHT.png"))
        addpwinpanel=Label(addpwin,image=addpwinpic)
        addpwinpanel.pack(side='top',fill='both',expand='yes')
        
        Label(addpwin,text=" LEAVE SPACE for no passenger ",bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=100)
        
        Label(addpwin,text=" Person 1 Name ",bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=150)
        Label(addpwin,text=" Person 2 Name ",bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=200)
        Label(addpwin,text=' Person 3 Name ',bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=250)
        Label(addpwin,text=' Person 4 Name ',bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=300)

        n1=Entry(addpwin)
        n1.place(x=370,y=150)
        n1.config(borderwidth=2,relief='sunken')
        
        n2=Entry(addpwin)
        n2.place(x=370,y=200)
        n2.config(borderwidth=2,relief='sunken')

        n3=Entry(addpwin)
        n3.place(x=370,y=250)
        n3.config(borderwidth=2,relief='sunken')
        
        n4=Entry(addpwin)
        n4.place(x=370,y=300)
        n4.config(borderwidth=2,relief='sunken')
        
        Label(addpwin,text=" Person 1 age ",bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=350)
        Label(addpwin,text=" Person 2 age ",bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=400)
        Label(addpwin,text=' Person 3 age ',bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=450)
        Label(addpwin,text=' Person 4 age ',bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=500)

        a1=Entry(addpwin)
        a1.place(x=370,y=350)
        a1.config(borderwidth=2,relief='sunken')
        
        a2=Entry(addpwin)
        a2.place(x=370,y=400)
        a2.config(borderwidth=2,relief='sunken')

        a3=Entry(addpwin)
        a3.place(x=370,y=450)
        a3.config(borderwidth=2,relief='sunken')
        
        a4=Entry(addpwin)
        a4.place(x=370,y=500)
        a4.config(borderwidth=2,relief='sunken')
        
        Label(addpwin,text=' Phone number ',bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=550)
        Label(addpwin,text=' Email ',bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=600)

        ph=Entry(addpwin)
        ph.place(x=370,y=550)
        ph.config(borderwidth=2,relief='sunken')
        
        e=Entry(addpwin)
        e.place(x=370,y=600)
        e.config(borderwidth=2,relief='sunken')
        
        Button(addpwin,text='Add Now',font=('Arial',16),command=billing,height=1,width=16,bg='DarkOrchid1',
        fg='gray6',activebackground='gray12',activeforeground='thistle1').place(x=800,y=600)

        addpwin.mainloop()

            
            
        
         
    def billing():
        global billwin, numseats

        name1=n1.get()
        name2=n2.get()
        name3=n3.get()
        name4=n4.get()
        age1=a1.get()
        age2=a2.get()
        age3=a3.get()
        age4=a4.get()
        phone=ph.get()
        email=e.get()

        if name1!=' ':
            numseats = 1
            if name2!=' ':
                numseats = 2
                if name3!=' ':
                    numseats = 3
                    if name4!=' ':
                        numseats = 4
                        
        sql='''insert into passengers(Group_ID, Name_1, Name_2, Name_3, Name_4,  age_1,  age_2,  age_3,  age_4,  Flight_name,  Flight_date,  phone, email, total_seats)
        values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',{},'{}',{})'''.format(username,name1,name2,name3,name4,age1,age2,age3,age4,r[0],r[6],phone,email,numseats)
        mycur.execute(sql)
        mydb.commit()
        
        sql="update flights set available_seats = {} where Flight_name = '{}'".format(r[7]-numseats,r[0])
        mycur.execute(sql)
        mydb.commit()
        
        
        def insert():
                sql='''insert into {}(FLIGHT_NAME, FROM_CITY, TO_CITY, BUISNESS_CLASS_PRICE, DEPARTURE_TIME, ARRIVAL_TIME, FLIGHT_DATE)
                values(%s,%s,%s,%s,%s,%s,%s)'''.format(username)
                mycur.execute(sql,rr)
                mydb.commit()
                messagebox.showinfo('Booked','Flight booked successfully')
                addpwin.destroy()
                billwin.destroy()
                book.destroy()
                

        if messagebox.askokcancel('Confirm Booking','Do you want to book this flight?',parent=book):
            billwin=tk.Toplevel()
            billwin.title('Khan FLIGHTS - BILLING')
            billwin.geometry('600x400')
            billwin.resizable(False,False)
            billwin.protocol('WM_DELETE_WINDOW',billclose)

            billwinpic=ImageTk.PhotoImage(Image.open("E:\\NK Programs\\Python\\python save\\Khan Flights\\transaction.jpg"))
            billwinpanel=Label(billwin,image=billwinpic)
            billwinpanel.pack(side='top',fill='both',expand='yes')
            


            Label(billwin,text=('UserName : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=180)
            Label(billwin,text=(username),font=('Arial',12),bg='lavenderblush').place(x=107,y=180)
            Label(billwin,text=('Flight Name : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=210)
            Label(billwin,text=(r[0]),font=('Arial',12),bg='lavenderblush').place(x=120,y=210)
            Label(billwin,text=('Flight Date : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=240)
            Label(billwin,text=(r[6]),font=('Arial',12),bg='lavenderblush').place(x=120,y=240)
            Label(billwin,text=('From : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=270)
            Label(billwin,text=(f),font=('Arial',12),bg='lavenderblush').place(x=70,y=270)
            Label(billwin,text=('To : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=300)
            Label(billwin,text=(t),font=('Arial',12),bg='lavenderblush').place(x=50,y=300)
            Label(billwin,text=('Amount : '),font=('Arial',12),bg='lavenderblush').place(x=20,y=330)
            Label(billwin,text=(p*numseats),font=('Arial',12),bg='lavenderblush').place(x=90,y=330)

            Button(billwin,text='Pay Now',font=('Arial',16),command=insert,height=1,width=16,bg='DarkOrchid1',
            fg='gray6',activebackground='gray12',activeforeground='thistle1').place(x=250,y=260)

            billwin.mainloop()

    def findflight():
        global rows,r,p,f,t,rr

        mycur=mydb.cursor()
        mycur.execute('SELECT * FROM Flights')
        rows=mycur.fetchall()

        def booknone():
            Label(book,text='Select a valid destination',font=('Arial',16),bg='pink').place(relx=0.5,rely=0.66)
            

        def fftv(r):
            tree.insert('',tk.END,values=r)
        
        sql_query = "SELECT * FROM flights WHERE FROM_CITY='{}' AND TO_CITY='{}'".format(f,t)
        mycur=mydb.cursor()
        mycur.execute(sql_query)
        row = mycur.fetchone()
        
        if row:
            r = list(row) 
            rr = r[0:-1]
            treeview(book, 1, 0.25, 0.65)
            fftv(r)
            p = r[3]
            Button(book,text='Book Now',font=('Arial',16),command=addpeople,height=1,width=16,bg='Lightsteelblue2',
            fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(relx=0.55,rely=0.87)
        
        else:
            Label(book,text='Select a valid destination',font=('Arial',16),bg='tomato3').place(relx=0.5,rely=0.66)



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

    cancelreeview(cancel,6,0.065,0.08)
    treview(cancel,6,0.065,0.3)

        
    global ROWS
    mycur=mydb.cursor()
    q = "select * from {}".format(username)
    mycur.execute(q)
    ROWS=mycur.fetchall()
    for ROW in ROWS:
        ree.insert('',tk.END,values=ROW)
        
    
    q= "select * from passengers where group_id ='{}'".format(username)
    mycur.execute(q)
    RO=mycur.fetchall()
    for R in RO:
        val = R[1:]
        tre.insert('',tk.END,values=val)

    Label(cancel,text=" FLIGHT NAME TO BE CANCELED ",bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=450)
    Label(cancel,text=" FLIGHT DATE ( yyyy-mm-dd ) ",bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=500)
    Label(cancel,text=' ACCOUNT PASSWORD ',bg='white',font=('Arial',12),borderwidth=1,relief='solid').place(x=100,y=550)

    

    global a,b,d

    a=Entry(cancel)
    a.place(x=370,y=450)
    a.config(borderwidth=2,relief='sunken')
    
    d=Entry(cancel)
    d.place(x=370,y=500)
    d.config(borderwidth=2,relief='sunken')


    b=Entry(cancel)
    b.place(x=370,y=550)
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
        Label(about,text='''COSTUMER SERVICE NUMBER : +91 8438394310 (INDIA)
            MAIL ID                      : nehal292004@gmail.com''',font=('Arial',16)).place(x=750,y=550)

    Button(about,text='Contact Us',font=('Arial',20),command=help,height=1,width=16,bg='Lightsteelblue2',
    fg='gray6',activebackground='Skyblue',activeforeground='thistle1').place(x=800,y=500)

    Label(about,text=('''This program is created by Nehal Khan on 21 July 2023. With the help 
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
        
def addpclose():
     if messagebox.askokcancel('Quit','Do you want to cancel booking?'):
        addpwin.destroy()

def logclose():

    if messagebox.askokcancel('Quit','Do you want to quit?'):
        logwin.destroy()
        quit()
        
def homeclose():

    if messagebox.askokcancel('Quit','Do you want to logout and quit?'):
        home.destroy()
        quit()


# new user:

def newuser():
    username = entry1.get()
    query_check = "SELECT * FROM accounts WHERE USERNAME='{}'".format(username)
    mcursor = mydb.cursor()
    mcursor.execute(query_check)
    existing_user = mcursor.fetchone()

    if existing_user:
        messagebox.showerror("Error", "Username already exists. Please choose a different username.")
    else:
        password = entry2.get()
        query_insert = "INSERT INTO accounts (USERNAME, PASSWORD) VALUES ('{}', '{}')".format(username, password)
        query2 = "create table {}(FLIGHT_NAME varchar(20), FROM_CITY char(20), TO_CITY char(20), BUISNESS_CLASS_PRICE int, DEPARTURE_TIME time, ARRIVAL_TIME time, FLIGHT_DATE date)".format(entry1.get())
        mcursor.execute(query2)
        mcursor.execute(query_insert)
        mydb.commit()
        messagebox.showinfo("Success", "Account created successfully!")
     
    
    
    
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

Button(logwin,text='Create',command=newuser,height=1,width=10).place(x=100,y=85)
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

Label(home,text=('''Disclaimer --- This project is totally offline and fake. This project does not indicate 
                 the original Khan Flight company and its software. This is just for project purposes and not for
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
