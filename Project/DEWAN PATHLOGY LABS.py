from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database = 'pathlab')
cur=con.cursor()


root=Tk()
root.title('CBSE PATHLOGY LABS')
root.iconbitmap('D:/lab.ico')
root.geometry("460x520")
"""
#creating database pathlab
cur.execute("create database pathlab")

#opening database pathlab
cur.execute("use pathlab")

#creating table pat
cur.execute('''create table pat
(p_id integer primary key,
p_name varchar(30),
p_age integer,
p_gender varchar(50),
p_blood varchar(20),
p_address varchar(100),
p_tests varchar(500))''')
"""
#exit
def close1():
    root.destroy()
#about us
def about():
    ab=Tk()
    ab.title('About us')
    ab.iconbitmap('D:/info.ico')
    ab.geometry("5000x5000")

    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()

    info_label=Label(ab, text="""OUR TEAM 
As one of the top pathology labs in India, CBSE PATHLABS has a very strong focus on hiring and retaining
top quality manpower to drive our different departments within and outside the labs.
Despite our size, we maintain an environment that nurtures some of the top thinkers in India in their respective fields of expertise.
Over 3000 individuals work at the CBSE PATHLABS in India with over 55 percent of the staff in laboratory functions.
We have a qualified team of 147 pathology specialists, 8 Radiologists, 13 Microbiologists, 5 Biochemists and 11 specialists with doctorate degrees.
Also, there is a growing pool of young leadership from top institutions like AFMC, IIMs, IITs, XLRI, SP JAIN amongst others.

AN ESTABLISHED BRAND ASSOCIATED WITH QUALITY SERVICES
We focus on providing patients quality diagnostic healthcare services in India.
Through our network, we offer patients convenient locations for their diagnostic laboratory services
and efficient service. With over 3,368 diagnostic tests and related healthcare tests and services offered,
we believe we are capable of performing substantially all of the diagnostic healthcare tests
and services currently prescribed by physicians in India. By delivering most accurate reports over the years,
CBSE PATHLABS has earned the reputation of being amongst the most trustworthy and reliable pathology labs in India.

ONE OF INDIA'S TOP DIAGNOSTIC CHAINS
We have built a national network consisting of our National Reference Laboratory in New Delhi
along with 190+ other clinical / medical laboratories, 1700+ lab patient service centers
and 5,000+ pickup points as of March 31, 2017 with the widest test menu of 4500 tests and panels.
Our network has coverage across India, including metropolitan areas such as New Delhi, Mumbai,
Bengaluru, Chennai, Hyderabad and Kolkata. We offer access to one of the best diagnostic
pathology services in India through our nationwide network of clinical / medical laboratories
(including our National Reference Laboratory), lab patient service centers and pickup points.

LABORATORY ACCREDITATIONS
CBSE PATHLABS, Meerut Cantt is NABL certified pathology lab in India.
It is also among the few Indian laboratories which accredited by CAP (College of American Pathologists)
and Certified by ISO 9001 (International Organization of Standardization).""",
                     font=('Comic Sans Ms',12))
    info_label.pack()
    

    con.commit()
    con.close()

    
#updating query
def edit():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()

    pid = p_id.get()
    pname = p_name.get()
    page = p_age.get()
    pgender = p_gender.get()
    pblood = p_blood.get()
    paddress = p_address.get()
    ptests = p_tests.get()
    pid = p_id.get()
         
    
    if update_box.get() == pid:
        cur.execute("update pat set p_id=%s, p_name=%s, p_age=%s, p_gender=%s, p_blood=%s, p_address=%s, p_tests=%s where p_id = %s",
                    (pid, pname, page, pgender, pblood, paddress, ptests, pid))
        messagebox.showinfo('Updated', 'Record Successfully Updated.')

    update_box.delete(0, END)
    
    con.commit()
    con.close()

    editor.destroy()

#updating records
global update

def update():
    if update_box.get() == '':
        messagebox.showerror('Error !', 'Patient Id not Provided !')

    else:
        global editor
        editor=Tk()
        editor.title('Update Patient Data')
        editor.iconbitmap('D:/lab.ico')
        editor.geometry("750x450")

        con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
        cur=con.cursor()

        cur.execute("select * from pat where p_id= " + update_box.get())
        data = cur.fetchall()

        #create global variables for text box
        global p_id
        global p_name
        global p_age
        global p_gender
        global p_blood
        global p_address
        global p_tests

        #making text boxes
        p_id=Entry(editor, width=30)
        p_id.grid(row=1, column=1, padx=60, pady=(10,0))

        p_name=Entry(editor, width=30)
        p_name.grid(row=2, column=1)

        p_age=Entry(editor, width=30)
        p_age.grid(row=3, column=1)

        p_gender=Entry(editor, width=30)
        p_gender.grid(row=4, column=1)

        p_blood=Entry(editor, width=30)
        p_blood.grid(row=5, column=1)

        p_address=Entry(editor, width=30)
        p_address.grid(row=6, column=1)

        p_tests=Entry(editor, width=30)
        p_tests.grid(row=7, column=1)

        #creating Labels
        wel_label=Label(editor, text="NOW, YOU CAN UPDATE ANYTHING HERE", font=('Comic Sans Ms',15))
        wel_label.grid(row=0, column=1, pady=50)
        
        id_label=Label(editor, text="Patient Id :", font=('Comic Sans Ms',15))
        id_label.grid(row=1, column=0, pady=(10,0))

        name_label=Label(editor, text="Patient Name :", font=('Comic Sans Ms',15))
        name_label.grid(row=2, column=0)

        age_label=Label(editor, text="Patient Age :", font=('Comic Sans Ms',15))
        age_label.grid(row=3, column=0)

        gend_label=Label(editor, text="Patient Gender :", font=('Comic Sans Ms',15))
        gend_label.grid(row=4, column=0)

        blood_label=Label(editor, text="Patient's Blood Group :", font=('Comic Sans Ms',15))
        blood_label.grid(row=5, column=0)

        add_label=Label(editor, text="Patient Address :", font=('Comic Sans Ms',15))
        add_label.grid(row=6, column=0)

        tests_label=Label(editor, text="Patient Tests :", font=('Comic Sans Ms',15))
        tests_label.grid(row=7, column=0)

        #looping throug the results
        for rec in data:
            p_id.insert(0, rec[0])
            p_name.insert(0, rec[1])
            p_age.insert(0, rec[2])
            p_gender.insert(0, rec[3])
            p_blood.insert(0, rec[4])
            p_address.insert(0, rec[5])
            p_tests.insert(0, rec[6])

        #create save button
        b9= Button(editor, text="Save Above Record", command=edit)
        b9.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=80)

        con.commit()
        con.close()

    
#deleting records
def delete():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()
    
    if delete_box.get() == '':
        messagebox.showerror('Error !', 'Patient Id not Provided !')
    else:
        msgbox2 = messagebox.askquestion('Confirm Deletion ?', 'Delete Record. Are you sure You want to Delete Record?')
        if msgbox2 == 'yes':
            cur.execute("delete from pat where p_id = " + delete_box.get())
            messagebox.showinfo('Deleted', 'Record successfully Deleted.')

        else:
            messagebox.showinfo('Canceled', 'Record Deletion Canceled.')
        
    delete_box.delete(0, END)
    con.commit()
    con.close()
    
#show_all data query
def show_all():
    show=Tk()
    show.title('Patient Data')
    show.iconbitmap('D:/lab.ico')
    show.geometry("650x300")

    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()

    cur.execute("select * from pat")
    data = cur.fetchall()

    print_rec=''
    for rec in data:
        print_rec += str(rec) + "\n"

    data_label=Label(show, text=print_rec, font=('Comic Sans MS',10))
    data_label.grid(row=1, column=0)

    con.commit()
    con.close()
    
#close show_one
def close2():
    show.destroy()
    
#show_one data query
def show_one():
    if show_box.get() == '':
        messagebox.showerror('Error !', 'Patient Id not Provided !')

    else:
        global show
        show=Tk()
        show.title('Patient Record')
        show.iconbitmap('D:/lab.ico')
        show.geometry("600x450")

        con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
        cur=con.cursor()

        cur.execute("select * from pat where p_id= " + show_box.get())
        data = cur.fetchall()

        #create global variables for text box
        global p_id
        global p_name
        global p_age
        global p_gender
        global p_blood
        global p_address
        global p_tests

        #making text boxes
        p_id=Entry(show, width=30)
        p_id.grid(row=1, column=1, padx=60, pady=(10,0))

        p_name=Entry(show, width=30)
        p_name.grid(row=2, column=1)

        p_age=Entry(show, width=30)
        p_age.grid(row=3, column=1)

        p_gender=Entry(show, width=30)
        p_gender.grid(row=4, column=1)

        p_blood=Entry(show, width=30)
        p_blood.grid(row=5, column=1)

        p_address=Entry(show, width=30)
        p_address.grid(row=6, column=1)

        p_tests=Entry(show, width=30)
        p_tests.grid(row=7, column=1)

        #creating Labels
        wel_label=Label(show, text="RECORD OF THE PATIENT", font=('Comic Sans Ms',15))
        wel_label.grid(row=0, column=1, pady=50)
        
        id_label=Label(show, text="Patient Id :", font=('Comic Sans Ms',15))
        id_label.grid(row=1, column=0, pady=(10,0))

        name_label=Label(show, text="Patient Name :", font=('Comic Sans Ms',15))
        name_label.grid(row=2, column=0)

        age_label=Label(show, text="Patient Age :", font=('Comic Sans Ms',15))
        age_label.grid(row=3, column=0)

        gend_label=Label(show, text="Patient Gender :", font=('Comic Sans Ms',15))
        gend_label.grid(row=4, column=0)

        blood_label=Label(show, text="Patient's Blood Group :", font=('Comic Sans Ms',15))
        blood_label.grid(row=5, column=0)

        add_label=Label(show, text="Patient Address :", font=('Comic Sans Ms',15))
        add_label.grid(row=6, column=0)

        tests_label=Label(show, text="Patient Tests :", font=('Comic Sans Ms',15))
        tests_label.grid(row=7, column=0)

        #looping throug the results
        for rec in data:
            p_id.insert(0, rec[0])
            p_name.insert(0, rec[1])
            p_age.insert(0, rec[2])
            p_gender.insert(0, rec[3])
            p_blood.insert(0, rec[4])
            p_address.insert(0, rec[5])
            p_tests.insert(0, rec[6])

        #create save button
        b10= Button(show, text="Close Record", command=close2)
        b10.grid(row=15, column=0, columnspan=2, pady=10, padx=10, ipadx=80)

        show_box.delete(0, END)
        con.commit()
        con.close()

#submiting the details of patient
def submit():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()

    #getting the data from the database 
    pid = p_id.get()
    pname = p_name.get()
    page = p_age.get()
    pgender = p_gender.get()
    pblood = p_blood.get()
    paddress = p_address.get()
    ptests = p_tests.get()

    #insert the values in the table
    if pid == '':
        msg=messagebox.showerror('Error !', 'information not provided !')
    else:
        cur.execute("insert into pat (p_id, p_name, p_age, p_gender, p_blood, p_address, p_tests) values(%s, %s, %s, %s, %s, %s, %s)",
                    (pid, pname, page, pgender, pblood, paddress, ptests))
        messagebox.showinfo('Inserted', 'Patient Record Succesfully added to Database.')
    
    con.commit()
    con.close()

    #clearing the text boxes
    p_id.delete(0, END)
    p_name.delete(0, END)
    p_age.delete(0, END)
    p_gender.delete(0, END)
    p_blood.delete(0, END)
    p_address.delete(0, END)
    p_tests.delete(0, END)

    add.destroy()

#add the patient data
def add_data():
    global add
    add=Tk()
    add.title('Adding Patient Record')
    add.iconbitmap('D:/lab.ico')
    add.geometry("600x450")

    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()

    global p_id
    global p_name
    global p_age
    global p_gender
    global p_blood
    global p_address
    global p_tests

    #making text boxes
    p_id=Entry(add, width=30)
    p_id.grid(row=1, column=1, padx=60, pady=(10,0))

    p_name=Entry(add, width=30)
    p_name.grid(row=2, column=1)

    p_age=Entry(add, width=30)
    p_age.grid(row=3, column=1)

    p_gender=Entry(add, width=30)
    p_gender.grid(row=4, column=1)

    p_blood=Entry(add, width=30)
    p_blood.grid(row=5, column=1)

    p_address=Entry(add, width=30)
    p_address.grid(row=6, column=1)

    p_tests=Entry(add, width=30)
    p_tests.grid(row=7, column=1)

    #creating Labels
        
    id_label=Label(add, text="Patient Id :", font=('Comic Sans Ms',15))
    id_label.grid(row=1, column=0, pady=(10,0))

    name_label=Label(add, text="Patient Name :", font=('Comic Sans Ms',15))
    name_label.grid(row=2, column=0)

    age_label=Label(add, text="Patient Age :", font=('Comic Sans Ms',15))
    age_label.grid(row=3, column=0)

    gend_label=Label(add, text="Patient Gender :", font=('Comic Sans Ms',15))
    gend_label.grid(row=4, column=0)

    blood_label=Label(add, text="Patient's Blood Group :", font=('Comic Sans Ms',15))
    blood_label.grid(row=5, column=0)

    add_label=Label(add, text="Patient Address :", font=('Comic Sans Ms',15))
    add_label.grid(row=6, column=0)

    tests_label=Label(add, text="Patient Tests :", font=('Comic Sans Ms',15))
    tests_label.grid(row=7, column=0)

    #create submit Button
    b2= Button(add, text="Add Above Data to database", font=('Comic Sans Ms',10), command=submit)
    b2.grid(row=12, column=0, columnspan=2, pady=5, padx=10, ipadx=103)


    

    
               
# text box
show_box=Entry(root, width=30)
show_box.grid(row=10, column=1, pady=(20,0))

delete_box=Entry(root, width=30)
delete_box.grid(row=12, column=1, pady=(20,0))

update_box=Entry(root, width=30)
update_box.grid(row=14, column=1, pady=(20,0))

# labels
show_label=Label(root, text="Enter Patient Id to display that Record :", font=('Comic Sans Ms',10))
show_label.grid(row=10, column=0, padx=5, pady=(20,0))

delete_label=Label(root, text="Enter Patient Id to Delete Record :", font=('Comic Sans Ms',10))
delete_label.grid(row=12, column=0, padx=5, pady=(20,0))

update_label=Label(root, text="Enter Patient Id to Update Record :", font=('Comic Sans Ms',10))
update_label.grid(row=14, column=0, padx=5, pady=(20,0))


#create add data Button
b1= Button(root, text="Add Patient Data to Database", font=('Comic Sans Ms',10), command=add_data)
b1.grid(row=7, column=0, columnspan=2, pady=(20,5), padx=10, ipadx=103)

#create show_all query button
b3= Button(root, text="Show all Records of Patients", font=('Comic Sans Ms',10), command=show_all)
b3.grid(row=8, column=0, columnspan=2, pady=5, padx=10, ipadx=105)

#create show_one query button
b4= Button(root, text="Display Record of the Patient", font=('Comic Sans Ms',10), command=show_one)
b4.grid(row=11, column=0, columnspan=2, pady=5, padx=10, ipadx=100)

#create delete button
b5= Button(root, text="Delete Record from the Database", font=('Comic Sans Ms',10), command=delete)
b5.grid(row=13, column=0, columnspan=2, pady=5, padx=10, ipadx=93)

#create update button
b6= Button(root, text="Update Record from the Database ", font=('Comic Sans Ms',10), command=update)
b6.grid(row=15, column=0, columnspan=2, pady=5, padx=10, ipadx=90)

#create about button
b7= Button(root, text="(i) Learn More About our Pathlabs", font=('Comic Sans Ms',10), command=about)
b7.grid(row=17, column=0, columnspan=2, pady=(60,5), padx=10, ipadx=90)

#create exit button
b8= Button(root, text="EXIT DATABASE", font=('Comic Sans Ms',10), command=close1)
b8.grid(row=18, column=0, columnspan=2, pady=5, padx=10, ipadx=140)






