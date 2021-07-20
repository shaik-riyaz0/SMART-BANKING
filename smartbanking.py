import mysql.connector
import webbrowser
import time
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *
mydb=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="smartt")
mycursor=mydb.cursor()
r=tk.Tk()
def g():
    print("sucessful")
    s="insert into record(rname,phone_no) values(%s,%s)"
    n=lov.get()
    p=pav.get()
    z=(n,p)
    mycursor.execute(s,z)
    mydb.commit()
    print("this bank provides you loan and locker")
    print("the minimum amount u have to maintain is 100")
    v=int(input("if u agree with this policy press 1 else 0"))
    if(v==1):
     main()
    else:
        print("thank you")
        exit(0)
def main():
    j=tk.Tk()
    j.geometry("600x400")
    j.config(background="blue")
    x=Label(j,text="WELCOME TO ROCKING'S ATM",bg="black",fg="red",font=("Times New Roman",20,"bold"),pady=5)
    x.pack()
    Button(j,text="ADMIN",bg="red",fg="white",font=("Times New Roman",20,"bold"),command=admin).pack(pady=14)
    Button(j,text="OPERATIONS",bg="red",fg="white",font=("Times New Roman",20,"bold"),command=user).pack(pady=14)
    Button(j,text="EXIT",bg="red",fg="white",font=("Times New Roman",20,"bold"),command=exitt).pack(pady=14)
    Button(j,text="OTHERS",bg="red",fg="white",font=("Times New Roman",20,"bold"),command=other).pack(pady=14)
def other():
    l=tk.Tk()
    l.geometry("600x300")
    x=Label(l,text="WELCOME TO RR ATM",bg="black",fg="red",font=("Times New Roman",20,"bold"),pady=5)
    x.grid(row=0,column=1)
    Button(l,text="PEOPLE VISITED TO BANK",font=("Times New Roman",12,"bold"),command=check).grid(row=1,column=1)
    Button(l,text="CURRENTLY ACTIVE PEOPLE",font=("Times New Roman",12,"bold"),command=current).grid(row=2,column=1)
def check():
    x="select rname,phone_no from record"
    mycursor.execute(x)
    mye=mycursor.fetchall()
    
    win=Tk()
    frm=Frame(win)
    frm.pack(side=tk.LEFT,padx=20)
    tv=ttk.Treeview(frm,columns=(1,2),show="headings",height="10")
    tv.pack()
    tv.heading(1, text="rname")
    tv.heading(2, text="phone_no")
    
    for i in mye:
        tv.insert('','end',values=i)

    win.title("ROCKING BANK")
    win.geometry("400x200")
    win.mainloop()

def current():
    x="select wname from withdraw"
    mycursor.execute(x)
    mye=mycursor.fetchall() 
    win=Tk()
    frm=Frame(win)
    frm.pack(side=tk.LEFT,padx=40)
    tv=ttk.Treeview(frm,columns=(1),show="headings",height="30")
    tv.pack()
    tv.heading(1, text="wname")
    
    for i in mye:
        tv.insert('','end',values=i)

    win.title("ROCKING BANK")
    win.geometry("400x300")
    win.mainloop()

def exitt():
    exit(0)
def admysql():
    from datetime import datetime
    z=datetime.now()
    h="deposit"
    print("this is to add account")
    x=random.randint(1001,9999)
    w=input("enter the customer's name\n")
    wc=int(input("enter customer's amount\n"))
    wa=random.randint(1000000000,99999999999)
    l=input("enter ur phone number\n")
    c=len(l)
    while(c!=10):
        l=input("enter ur correct phone number\n")
        c=len(l)
    s="insert into withdraw(pin_id,wname,wcost,waccount_no,wphone_no)values(%s,%s,%s,%s,%s)"
    p=(x,w,wc,wa,z)
    mycursor.execute(s,p)
    mydb.commit()
    q="insert into mini(time,cost,pin_id,action) values(%s,%s,%s,%s)"
    mycursor.execute(q,(z,wc,x,h,))
    mydb.commit()    
    print("sucessfull")
    print("ur password is generating...")
    time.sleep(1)
    print("it may take more time ...do not turn off ur device")
    time.sleep(3)
    print("thanks for begin a part of rocking's bank")
    print(x,"ur password")
    print(wa,"ur account no")
    main()
def demysql():
    print("this is to delete account")
    s="delete from withdraw where pin_id=%s"
    x=int(input("enter ur pin number\n"))
    mycursor.execute(s,(x,))
    mydb.commit()
    q="delete from mini where pin_id=%s"
    mycursor.execute(q,(x,))
    mydb.commit()
    print("sucessfully removed the account")
    main()
def etmysql():
    exit(0)
def ptmysql():
    print("this page is for PIN-CHANGE")
    s="update withdraw set pin_id=%s where pin_id=%s"
    v=int(input("enter ur account number\n"))
    z=int(input("enter ur old pin\n"))
    x=int(input("enter ur new password\n"))
    b=int(input("conform ur password\n"))
    if(x==b):
        print("sucess")
    else:
        print("try again")
        admin()
    mycursor.execute(s,(x,z))
    mydb.commit()
    q="update mini set pin_id=%s where pin_id=%s"
    mycursor.execute(q,(x,z,))
    mydb.commit()
    main()
def admin():
    d=int(input("THIS IS ADMIN PAGE------TO ENTER INTO PAGE U HAVE TO GIVE UR PASSWORD\n"))
    z=1234
    if(z==d):
        print("*******WELCOME TO ROCKING BANK*********")
        print("this may take few minutes")
        time.sleep(4)
        k=tk.Tk()
        k.geometry("300x100")
        k.config(background="green")
        k.title("smart banking-ADMIN PAGE")
        Button(k,text="ADD ACCOUNT",bg="red",fg="white",command=admysql).grid(row=2,column=1)
        Button(k,text="EXIT",bg="red",fg="white",command=etmysql).grid(row=3,column=2)
        Button(k,text="PIN CHANGE",bg="red",fg="white",command=ptmysql).grid(row=2,column=2)
        Button(k,text="DELETE AN ACCOUNT",bg="red",fg="white",command=demysql).grid(row=3,column=1)
    else:
        print("password incorrect try again")
        admin()
def wmysql():
    try:
        print("this is withdraw page")
        from datetime import datetime
        z=datetime.now()
        g="withdraw"
        sq="update withdraw set wcost=wcost-%s where pin_id=%s"
        y=int(input("enter ur pin\n"))
        x=int(input("enter ur amount\n"))
        mycursor.execute(sq,(x,y,))
        mydb.commit()
        q="insert into mini(time,cost,pin_id,action)values(%s,%s,%s,%s)"
        mycursor.execute(q,(z,x,y,g,))
        mydb.commit()
        print("ur transaction is finished\n")
    except Exception:
        print("transaction failed due to: INSUFFICIENT FUNDS")
def dmysql():
    print("this is deposite page")
    from datetime import datetime
    z=datetime.now()
    g="deposit"
    sq="update withdraw set wcost=wcost+%s where pin_id=%s"
    y=int(input("enter ur pin\n"))
    x=int(input("enter ur amount\n"))
    mycursor.execute(sq,(x,y,))
    mydb.commit()
    q="insert into mini(time,cost,pin_id,action)values(%s,%s,%s,%s)"
    mycursor.execute(q,(z,x,y,g,))
    mydb.commit()
    print("ur transaction is sucessful")

def hmysql():
    print("this is web page help line number\n")
    time.sleep(1)
    webbrowser.open("https://sbi.co.in/web/customer-care/contact-centre")
def cmysql():
    print("this is to check the balance page")
    x=int(input("enter ur pin\n"))
    v="select wname,wcost from withdraw where pin_id=%s"
    mycursor.execute(v,(x,))
    mye=mycursor.fetchall() 
    win=Tk()
    frm=Frame(win)
    frm.pack(side=tk.LEFT,padx=20)
    tv=ttk.Treeview(frm,columns=(1,2),show="headings",height="10")
    tv.pack()
    tv.heading(1, text="wname")
    tv.heading(2, text="wcost")
    
    for i in mye:
        tv.insert('','end',values=i)

    win.title("ROCKING's BANK")
    win.geometry("400x100")
    win.mainloop()

def minis():
    x=int(input("enter ur pin\n"))
    q="select time,cost,action from mini where pin_id=%s"
    mycursor.execute(q,(x,))
    my=mycursor.fetchall()
    win=Tk()
    frm=Frame(win)
    frm.pack(side=tk.LEFT,padx=20)

    tv=ttk.Treeview(frm,columns=(1,2,3),show="headings",height="20")
    tv.pack()

    tv.heading(1, text="time")
    tv.heading(2, text="cost")
    tv.heading(3, text="action")
    for i in my:
        tv.insert('','end',values=i)

    win.title("ROCKING'S BANK")
    win.geometry("600x300")
    win.mainloop()

def user():
    t=tk.Tk()
    t.geometry("690x320")
    t.title("smart banking")
    t.config(background="black")
    x=Label(t,text="WELCOME TO RR'S ATM",bg="black",fg="red",font=("Times New Roman",20,"bold"),pady=5)
    x.grid(row=0,column=3)
    Button(t,text="WITHDRAW",bg="red",fg="white",command=wmysql).grid(row=2,column=4)
    Button(t,text="DEPOSIT",bg="red",fg="white",command=dmysql).grid(row=4,column=1)
    Button(t,text="HELP LINE NO",bg="red",fg="white",command=hmysql).grid(row=6,column=4)
    Button(t,text="CHECK BALANCE",bg="red",fg="white",command=cmysql).grid(row=8,column=1)
    Button(t,text="BACK TO ACCESS PAGE",bg="red",fg="white",command=main).grid(row=12,column=4)
    Button(t,text="MINI STATMENT",bg="red",fg="white",command=minis).grid(row=14,column=1)
    t.mainloop()
    

r.geometry("600x300")
r.title("smart banking")
x=Label(r,text="WELCOME TO RR ATM",bg="grey",fg="red",font=("Times New Roman",20,"bold"),pady=5)
x.grid(row=0,column=3)
lo=Label(r,text="NAME",pady=15)
lo.grid(row=1,column=2)
pa=Label(r,text="PHONE NUMBER",pady=15)
pa.grid(row=2,column=2)
lov=StringVar()
pav=StringVar()
checkb=IntVar()
le=Entry(r,textvariable=lov)
pe=Entry(r,textvariable=pav,show="*")
le.grid(row=1,column=3)
pe.grid(row=2,column=3)
Button(text="SUBMIT",command=g).grid(row=3,column=3)
Button(text="CLOSE",command=r.destroy).grid(row=9,column=3)
Button(text="ALREADY HAVE AN ACCOUNT",command=main).grid(row=6,column=3)
r.mainloop()
