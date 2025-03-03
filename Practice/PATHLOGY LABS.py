from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database = 'pathlab')
cur=con.cursor()

root=Tk()
root.title('PATHLOGY LAB MANAGER')
root.iconbitmap('D:/lab.ico')
root.geometry("495x500")

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
p_address varchar(100))''')

#creating table ptest
cur.execute('''create table ptest
(p_id integer primary key,
p_tests varchar(500),
p_bill varchar(500) references pat(p_id))''')
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
    pid = p_id.get()
         
    
    if update_box.get() == pid:
        cur.execute("update pat set p_id=%s, p_name=%s, p_age=%s, p_gender=%s, p_blood=%s, p_address=%s where p_id = %s",
                    (pid, pname, page, pgender, pblood, paddress, pid))
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
       
        #looping through the results
        for rec in data:
            p_id.insert(0, rec[0])
            p_name.insert(0, rec[1])
            p_age.insert(0, rec[2])
            p_gender.insert(0, rec[3])
            p_blood.insert(0, rec[4])
            p_address.insert(0, rec[5])
           
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


    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()

    cur.execute("select * from pat")
    data = cur.fetchall()

    print_rec=''    
    for rec in data:  
        print_rec += str(rec[0]) + "                        " + str(rec[1]) + "\n"

    heading_id=Label(show, text='ID', font=('Comic Sans MS',13))
    heading_id.grid(row=0, column=0, padx=(20,10), pady=(30,10))

    heading_name=Label(show, text='NAME', font=('Comic Sans MS',13))
    heading_name.grid(row=0, column=1, padx=(20,10), pady=(30,10))


    data_label=Label(show, text=print_rec, font=('Comic Sans MS',12))
    data_label.grid(row=1,column=1)

    con.close()
        
#close show_one
def close2():
    show1.destroy()
    show2.destroy()
    
#show_one query
def show_one1():
    if show_box.get() == '':
        messagebox.showerror('Error !', 'Patient Id not Provided !')
        
    else:
        global show1
        show1=Tk()
        show1.title('Patient Record')
        show1.iconbitmap('D:/lab.ico')
        show1.geometry("600x700")

        con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
        cur=con.cursor()

        cur.execute("select * from pat where p_id= " + show_box.get())
        data = cur.fetchall()

         
        #creating Labels
        wel_label=Label(show1, text="RECORD OF THE PATIENT", font=('Comic Sans Ms',15))
        wel_label.grid(row=0, column=1, padx=(0,100), pady=(35,30))
            
        id_label=Label(show1, text="Patient Id :", font=('Comic Sans Ms',15))
        id_label.grid(row=1, column=0, padx=(50,0))

        name_label=Label(show1, text="Patient Name :", font=('Comic Sans Ms',15))
        name_label.grid(row=2, column=0, padx=(50,0))

        age_label=Label(show1, text="Patient Age :", font=('Comic Sans Ms',15))
        age_label.grid(row=3, column=0, padx=(50,0))

        gend_label=Label(show1, text="Patient Gender :", font=('Comic Sans Ms',15))
        gend_label.grid(row=4, column=0, padx=(50,0))

        blood_label=Label(show1, text="Patient's Blood Group :", font=('Comic Sans Ms',15))
        blood_label.grid(row=5, column=0, padx=(50,0))

        add_label=Label(show1, text="Patient Address :", font=('Comic Sans Ms',15))
        add_label.grid(row=6, column=0, padx=(50,0))

        
        record1 = ''
        for rec1 in data:
            record1 += str(rec1[0]) + "\n"
            
        record2 = ''
        for rec2 in data:
            record2 += str(rec2[1]) + "\n"
            
        record3 = ''
        for rec3 in data:
            record3 += str(rec3[2]) + "\n"
            
        record4 = ''
        for rec4 in data:
            record4 += str(rec4[3]) + "\n"
            
        record5 = ''
        for rec5 in data:
            record5 += str(rec5[4]) + "\n"
            
        record6 = ''
        for rec6 in data:
            record6 += str(rec6[5]) + "\n"

        id_label1=Label(show1, text=record1, font=('Comic Sans Ms',15))
        id_label1.grid(row=1, column=1, padx=50, pady=(20,0))

        id_label2=Label(show1, text=record2, font=('Comic Sans Ms',15))
        id_label2.grid(row=2, column=1, padx=50, pady=(20,0))

        id_label3=Label(show1, text=record3, font=('Comic Sans Ms',15))
        id_label3.grid(row=3, column=1, padx=50, pady=(20,0))

        id_label4=Label(show1, text=record4, font=('Comic Sans Ms',15))
        id_label4.grid(row=4, column=1, padx=50, pady=(20,0) )

        id_label5=Label(show1, text=record5, font=('Comic Sans Ms',15))
        id_label5.grid(row=5, column=1, padx=50, pady=(20,0) )

        id_label6=Label(show1, text=record6, font=('Comic Sans Ms',15))
        id_label6.grid(row=6, column=1, padx=50, pady=(20,0))
        
        #create close button
        b10= Button(show1, text="Close Record", command=close2)
        b10.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=80)

        show_box.delete(0, END)
        
        
        con.close()
#show_one data query
def show_one2():

    global show2
    show2=Tk()
    show2.title('Enter ID')
    show2.iconbitmap('D:/lab.ico')
    show2.geometry("500x120")

    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')

    global show_box
    show_box=Entry(show2, width=30)
    show_box.grid(row=10, column=1, pady=(20,0))
        
    show_label=Label(show2, text="Enter Patient Id to display that Record :", font=('Comic Sans Ms',10))
    show_label.grid(row=10, column=0, padx=(27,5), pady=(25,0))

    #create show_one query button
    b4= Button(show2, text="Show Record", font=('Comic Sans Ms',10), command=show_one1)
    b4.grid(row=11, column=0, columnspan=2, pady=5, padx=10, ipadx=100)
    
    
        
    con.close()

    

#submiting the details of patient
def submit():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()

    global pid
    #getting the data from the database 
    pid = p_id.get()
    pname = p_name.get()
    page = p_age.get()
    pgender = p_gender.get()
    pblood = p_blood.get()
    paddress = p_address.get()
        

    #insert the values in the table
    cur.execute("insert into pat (p_id, p_name, p_age, p_gender, p_blood, p_address) values(%s, %s, %s, %s, %s, %s)",
                (pid, pname, page, pgender, pblood, paddress))
    messagebox.showinfo('Inserted', 'Patient Record Succesfully added to Database.')

    #clearing the text boxes
    p_id.delete(0, END)
    p_name.delete(0, END)
    p_age.delete(0, END)
    p_gender.delete(0, END)
    p_blood.delete(0, END)
    p_address.delete(0, END)

    add.destroy()
        
    con.commit()
    con.close()

#list of tests in lab
def tests():
    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
    cur=con.cursor()

    if p_id.get() == '' :
        messagebox.showerror('Error !', 'information not provided !')
        
    else:
        test=Tk()
        test.title("Patient's Tests")
        test.iconbitmap('D:/lab.ico')
        test.geometry("1200x700")

        '''
        a1="Oncorpo Heredity Cancer Risk"
        a2="Allergy Comprehensive Profile"
        a3="Allergy Regional Panel"
        a4="Obesity Panel"
        a5="Enhance Liver Fibrosis"
        a6="Sugar Comprehensive"
        a7="Chronic Fatigue Syndrome"
        a8="X-Rays"
        a9="Ultrasounds"
        a10="MRIs"
        a11="HIV 1 and 2 Antibodies"
        a12="Immunity check  package"
        a13="Thyroid Comprehensive Panel"
        a14="Sugar Advance"
        a15="Culture Stool Test"

            
        b1="Culture Urine Test"
        b2="Insulin Antibodies"
        b3="Dengue Fever Antibodies"
        b4="Zinc Serum / Plasma"
        b5="Allergy Gluten"
        b6="Pregnancy Tests"
        b7="Insulin Fasting"
        b8="Heamoglobin"
        b9="Anemia Check Complete"
        b10="Red Blood Cells (RBC)"
        b11="White Blood Cells (WBC)"
        b12="Hypertension Panel"
        b13="Allergy Milk"
        b14="Allergy Mushroom"
        b15="Iron Check"
        '''

        var = IntVar()
        #creating check buttons

        c1=Checkbutton(test, text="Oncorpo Heredity Cancer Risk ", variable=var, onvalue="25000", font=('Comic Sans Ms',12))
        c1.grid(row=1, column=0, sticky=W , pady=(10,0))

        c2=Checkbutton(test, text="Allergy Comprehensive Profile", variable=var, onvalue="13000",font=('Comic Sans Ms',12))
        c2.grid(row=2, column=0, sticky=W , pady=(10,0))

        c3=Checkbutton(test, text="Allergy Regional Panel", variable=var, onvalue="10000",font=('Comic Sans Ms',12))
        c3.grid(row=3, column=0, sticky=W, pady=(10,0))

        c4=Checkbutton(test, text="Obesity Panel", variable=var, onvalue="4900",font=('Comic Sans Ms',12))
        c4.grid(row=4, column=0, sticky=W, pady=(10,0))
                        
        c5=Checkbutton(test, text="Enhance Liver Fibrosis", variable=var, onvalue="4500",font=('Comic Sans Ms',12))
        c5.grid(row=5, column=0, sticky=W, pady=(10,0))
                        
        c6=Checkbutton(test, text="Sugar Comprehensive", variable=var, onvalue="3099",font=('Comic Sans Ms',12))
        c6.grid(row=6, column=0, sticky=W, pady=(10,0))
                        
        c7=Checkbutton(test, text="Chronic Fatigue Syndrome", variable=var, onvalue="3500",font=('Comic Sans Ms',12))
        c7.grid(row=7, column=0, sticky=W, pady=(10,0))
                        
        c8=Checkbutton(test, text="X-Rays", variable=var, onvalue="800",font=('Comic Sans Ms',12))
        c8.grid(row=8, column=0, sticky=W, pady=(10,0))
                        
        c9=Checkbutton(test, text="Ultrasounds", variable=var, onvalue="1200",font=('Comic Sans Ms',12))
        c9.grid(row=9, column=0, sticky=W, pady=(10,0))
                        
        c10=Checkbutton(test, text="MRIs", variable=var, onvalue="2500",font=('Comic Sans Ms',12))
        c10.grid(row=10, column=0, sticky=W, pady=(10,0))
                        
        c11=Checkbutton(test, text="HIV 1 and 2 Antibodies", variable=var, onvalue="3350",font=('Comic Sans Ms',12))
        c11.grid(row=11, column=0, sticky=W, pady=(10,0))
                        
        c12=Checkbutton(test, text="Immunity check  package", variable=var, onvalue="4000",font=('Comic Sans Ms',12))
        c12.grid(row=12, column=0, sticky=W, pady=(10,0))
                        
        c13=Checkbutton(test, text="Thyroid Comprehensive Panel", variable=var, onvalue="3500",font=('Comic Sans Ms',12))
        c13.grid(row=13, column=0, sticky=W, pady=(10,0))
                        
        c14=Checkbutton(test, text="Sugar Advance", variable=var, onvalue="1300",font=('Comic Sans Ms',12))
        c14.grid(row=14, column=0, sticky=W, pady=(10,0))

        c15=Checkbutton(test, text="Culture Stool Test", variable=var, onvalue="1000",font=('Comic Sans Ms',12))
        c15.grid(row=15, column=0, sticky=W, pady=(10,0))
                
        #next column
        c16=Checkbutton(test, text="Culture Urine Test", variable=var, onvalue="850",font=('Comic Sans Ms',12))
        c16.grid(row=1, column=4, sticky=W, pady=(10,0))

        c17=Checkbutton(test, text="Insulin Antibodies", variable=var, onvalue="2200",font=('Comic Sans Ms',12))
        c17.grid(row=2, column=4, sticky=W, pady=(10,0))
                        
        c18=Checkbutton(test, text="Dengue Fever Antibodies", variable=var, onvalue="900",font=('Comic Sans Ms',12))
        c18.grid(row=3, column=4, sticky=W, pady=(10,0))
                        
        c19=Checkbutton(test, text="Zinc Serum / Plasma", variable=var, onvalue="3500",font=('Comic Sans Ms',12))
        c19.grid(row=4, column=4, sticky=W, pady=(10,0))
                        
        c20=Checkbutton(test, text="Allergy Gluten", variable=var, onvalue="6600",font=('Comic Sans Ms',12))
        c20.grid(row=5, column=4, sticky=W, pady=(10,0))
                        
        c21=Checkbutton(test, text="Pregnancy Tests", variable=var, onvalue="1000",font=('Comic Sans Ms',12))
        c21.grid(row=6, column=4, sticky=W, pady=(10,0))
                        
        c22=Checkbutton(test, text="Insulin Fasting", variable=var, onvalue="2500",font=('Comic Sans Ms',12))
        c22.grid(row=7, column=4, sticky=W, pady=(10,0))
                        
        c23=Checkbutton(test, text="Heamoglobin", variable=var, onvalue="600",font=('Comic Sans Ms',12))
        c23.grid(row=8, column=4, sticky=W, pady=(10,0))
                        
        c24=Checkbutton(test, text="Anemia Check Complete", variable=var, onvalue="2500",font=('Comic Sans Ms',12))
        c24.grid(row=9, column=4, sticky=W, pady=(10,0))
                        
        c25=Checkbutton(test, text="Red Blood Cells (RBC)", variable=var, onvalue="800",font=('Comic Sans Ms',12))
        c25.grid(row=10, column=4, sticky=W, pady=(10,0))
                        
        c26=Checkbutton(test, text="White Blood Cells (WBC)", variable=var, onvalue="900",font=('Comic Sans Ms',12))
        c26.grid(row=11, column=4, sticky=W, pady=(10,0))
                        
        c27=Checkbutton(test, text="Hypertension Panel", variable=var, onvalue="5000",font=('Comic Sans Ms',12))
        c27.grid(row=12, column=4, sticky=W, pady=(10,0))
                        
        c28=Checkbutton(test, text="Allergy Milk", variable=var, onvalue="1450",font=('Comic Sans Ms',12))
        c28.grid(row=13, column=4, sticky=W, pady=(10,0))
                        
        c29=Checkbutton(test, text="Allergy Mushroom", variable=var, onvalue="5500",font=('Comic Sans Ms',12))
        c29.grid(row=14, column=4, sticky=W, pady=(10,0))
                        
        c30=Checkbutton(test, text="Iron Check", variable=var, onvalue="2200",font=('Comic Sans Ms',12))
        c30.grid(row=15, column=4, sticky=W, pady=(10,0))


        #making Price Labels
        l0=Label(test, text ="PATIENTS' TESTS LIST", font=('Comic Sans Ms',15))
        l0.grid(row=0, column=3, pady=(10,0))
     
        l1=Label(test, text ="25000/-", font=('Comic Sans Ms',12))
        l1.grid(row=1, column=2, sticky=W, pady=(10,0), ipadx=(50))

        l2=Label(test, text ="13000/-", font=('Comic Sans Ms',12))
        l2.grid(row=2, column=2, sticky=W, pady=(10,0), ipadx=(50))

        l3=Label(test, text ="10000/-", font=('Comic Sans Ms',12))
        l3.grid(row=3, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l4=Label(test, text ="4900/-", font=('Comic Sans Ms',12))
        l4.grid(row=4, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l5=Label(test, text ="4500/-", font=('Comic Sans Ms',12))
        l5.grid(row=5, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l6=Label(test, text ="3099/-", font=('Comic Sans Ms',12))
        l6.grid(row=6, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l7=Label(test, text ="3500/-", font=('Comic Sans Ms',12))
        l7.grid(row=7, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l8=Label(test, text ="800/-", font=('Comic Sans Ms',12))
        l8.grid(row=8, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l9=Label(test, text ="1200/-", font=('Comic Sans Ms',12))
        l9.grid(row=9, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l10=Label(test, text ="2500/-", font=('Comic Sans Ms',12))
        l10.grid(row=10, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l11=Label(test, text ="3350/-", font=('Comic Sans Ms',12))
        l11.grid(row=11, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l12=Label(test, text ="4000/-", font=('Comic Sans Ms',12))
        l12.grid(row=12, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l13=Label(test, text ="3500/-", font=('Comic Sans Ms',12))
        l13.grid(row=13, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l14=Label(test, text ="1300/-", font=('Comic Sans Ms',12))
        l14.grid(row=14, column=2, sticky=W, pady=(10,0), ipadx=(50))
                
        l15=Label(test, text ="1000/-", font=('Comic Sans Ms',12))
        l15.grid(row=15, column=2, sticky=W, pady=(10,0), ipadx=(50))

        #next column
        l16=Label(test, text ="850/-", font=('Comic Sans Ms',12))
        l16.grid(row=1, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l17=Label(test, text ="2200/-", font=('Comic Sans Ms',12))
        l17.grid(row=2, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l18=Label(test, text ="900/-", font=('Comic Sans Ms',12))
        l18.grid(row=3, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l19=Label(test, text ="3500/-", font=('Comic Sans Ms',12))
        l19.grid(row=4, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l20=Label(test, text ="6600/-", font=('Comic Sans Ms',12))
        l20.grid(row=5, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l21=Label(test, text ="1000/-", font=('Comic Sans Ms',12))
        l21.grid(row=6, column=5, sticky=W, pady=(10,0), ipadx=(50))
                
        l22=Label(test, text ="2500/-", font=('Comic Sans Ms',12))
        l22.grid(row=7, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l23=Label(test, text ="600/-", font=('Comic Sans Ms',12))
        l23.grid(row=8, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l24=Label(test, text ="2500/-", font=('Comic Sans Ms',12))
        l24.grid(row=9, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l25=Label(test, text ="800/-", font=('Comic Sans Ms',12))
        l25.grid(row=10, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l26=Label(test, text ="900/-", font=('Comic Sans Ms',12))
        l26.grid(row=11, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l27=Label(test, text ="5000/-", font=('Comic Sans Ms',12))
        l27.grid(row=12, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l28=Label(test, text ="1450/-", font=('Comic Sans Ms',12))
        l28.grid(row=13, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l29=Label(test, text ="5500/-", font=('Comic Sans Ms',12))
        l29.grid(row=14, column=5, sticky=W, pady=(10,0), ipadx=(50))

        l30=Label(test, text ="2200/-", font=('Comic Sans Ms',12))
        l30.grid(row=15, column=5, sticky=W, pady=(10,0), ipadx=(50))


        #making next Button
        b11= Button(test, text=" NEXT ", font=('Comic Sans Ms',10), command=submit)
        b11.grid(row=6, column=6, pady=2, padx=20, ipadx=100)


        con.commit()
        con.close()

       
       
        
#add the patient data
def add_data():
    global add
    add=Tk()
    add.title('Adding Patient Record')
    add.iconbitmap('D:/lab.ico')
    add.geometry("550x350")

    con=mysql.connector.connect(host ='localhost', user ='root', password ='@kiman2003', database='pathlab')
   

    global p_id
    global p_name
    global p_age
    global p_gender
    global p_blood
    global p_address
  

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

   
    #creating Labels
        
    id_label=Label(add, text=" Enter Patient Id :", font=('Comic Sans Ms',15))
    id_label.grid(row=1, column=0, pady=(10,0))

    name_label=Label(add, text="Enter Patient Name :", font=('Comic Sans Ms',15))
    name_label.grid(row=2, column=0)

    age_label=Label(add, text="Enter Patient Age :", font=('Comic Sans Ms',15))
    age_label.grid(row=3, column=0)

    gend_label=Label(add, text="Enter Patient Gender :", font=('Comic Sans Ms',15))
    gend_label.grid(row=4, column=0)

    blood_label=Label(add, text="Enter Patient's Blood Group :", font=('Comic Sans Ms',15))
    blood_label.grid(row=5, column=0)

    add_label=Label(add, text="Enter Patient Address :", font=('Comic Sans Ms',15))
    add_label.grid(row=6, column=0)

    

    #create next Button
    b2= Button(add, text=" NEXT ", font=('Comic Sans Ms',10), command=tests)
    b2.grid(row=12, column=0, columnspan=2, pady=5, padx=10, ipadx=103)

    


    con.commit()
    con.close()


    
               
# text box
delete_box=Entry(root, width=30)
delete_box.grid(row=12, column=1, padx=(27,10), pady=(20,0))

update_box=Entry(root, width=30)
update_box.grid(row=14, column=1, padx=(27,10), pady=(20,0))

# labels
delete_label=Label(root, text="Enter Patient Id to Delete Record :", font=('Comic Sans Ms',10))
delete_label.grid(row=12, column=0, padx=(27,10), pady=(20,0))

update_label=Label(root, text="Enter Patient Id to Update Record :", font=('Comic Sans Ms',10))
update_label.grid(row=14, column=0, padx=(27,10), pady=(20,0))

#create add data Button
b1= Button(root, text="Add Patient Record", font=('Comic Sans Ms',10), command=add_data)
b1.grid(row=7, column=0, columnspan=2, pady=(20,5), padx=(27,10), ipadx=138.5)

#create show_all query button
b3= Button(root, text="Show Patients' List", font=('Comic Sans Ms',10), command=show_all)
b3.grid(row=8, column=0, columnspan=2, pady=5, padx=(27,10), ipadx=139)

#create show_one query button
b4= Button(root, text="Show Patient's Summary", font=('Comic Sans Ms',10), command=show_one2)
b4.grid(row=11, column=0, columnspan=2, pady=5, padx=(27,10), ipadx=123)

#create delete button
b5= Button(root, text="Delete Record from the Database", font=('Comic Sans Ms',10), command=delete)
b5.grid(row=13, column=0, columnspan=2, pady=5, padx=(27,10), ipadx=93)

#create update button
b6= Button(root, text="Update Record from the Database ", font=('Comic Sans Ms',10), command=update)
b6.grid(row=15, column=0, columnspan=2, pady=5, padx=(27,10), ipadx=90)

#create about button
b7= Button(root, text="(i) Learn More About our Pathlabs", font=('Comic Sans Ms',10), command=about)
b7.grid(row=17, column=0, columnspan=2, pady=(60,5), padx=(27,10), ipadx=90)

#create exit button
b8= Button(root, text="EXIT DATABASE", font=('Comic Sans Ms',10), command=close1)
b8.grid(row=18, column=0, columnspan=2, pady=5, padx=(27,10), ipadx=140)




