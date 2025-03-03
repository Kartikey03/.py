from tkinter import *
import mysql.connector

def show_one1():
    global show1
    show1=Tk()
    show1.title('Patient Record')
    show1.iconbitmap('D:/lab.ico')

    button=Button(show1, text='Show', command=show_one2)
    button.pack()

def show_one2():
    global show2
    show2=Toplevel()
    show2.title('Search Patient Records')
    show2.iconbitmap('D:/lab.ico')

    button2=Button(show2, text='Search Patient by ID', command=show_one3)
    button2.pack()

    button3=Button(show2, text='Search Patient by Name', command=show_one4)
    button3.pack()

    button4=Button(show2, text='Search Patient by Blood Group', command=show_one5)
    button4.pack()

    button5=Button(show2, text='Search Patient by Age', command=show_one6)
    button5.pack()

def show_one3():
    global show3
    show3=Toplevel()
    show3.title('Search by ID')
    show3.iconbitmap('D:/lab.ico')

    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()

    cur.execute("select * from pat where id= " + show_box.get())
    data = cur.fetchall()
    cur.execute ("select * from pat where id=" + show_box.get())



show_one1()      