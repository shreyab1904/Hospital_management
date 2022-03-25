import sqlite3
conn=sqlite3.connect('Hospital.db')
'''''
command= "CREATE TABLE patient(id PRIMARY KEY,name TEXT,phone INTEGER, address TEXT)"
conn.execute(command)
print("Table inserted")
'''
'''
command="INSERT INTO patient VALUES(8,'Sneha',9123411223,'Punawale')"
conn.execute(command)
conn.commit()
print("Value inserted")
'''

def add():
    id=input("enter id ")
    name=input("enter name ")
    phone=input("enter phone number ")
    address=input("enter address ")
    data=(id,name,phone,address)
    command="INSERT INTO patient VALUES(?,?,?,?)"
    c = conn.cursor()
    c.execute(command,data)
    conn.commit()
    print("Entered successfully")
    r = c.fetchall()
    for i in r:
        print(i)
    menu()


def view():
    command = "SELECT *FROM patient"
    c = conn.cursor()
    c.execute(command)
    r = c.fetchall()
    for i in r:
        print(i)

def menu():
    print("1. Add Patient Details: ")
    print("2. View Patient Details: ")
    ch=int(input("enter your choice"))
    if ch==1:
        add()
    elif ch==2:
        view()
    else: 
        print("Invalid Choice")

menu()