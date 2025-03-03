#Menu-driven program to Create a dictionary using UDFS

d={}  #global dictionary

def append():   
    n=input('Enter name:')
    p=input('Enter phone number:')
    d[n]=p
    print("Contact added to Phonebook")
        
def showall():
    for k in d:
        print("contact:",k,"phone:",d[k])

def search():
    n=input('Enter name to look for:')
    found=False

    if n in d:
        found=True
        print(n,"has phone number:",d[n])
    
        
    if found==False:
        print(n,"not found in phonebook")

def modify():
    n=input('Enter name whose number has to be modified:')
    found=False

    if n in d:
        found=True
        p=input('Enter the new phone number:')
        d[n]=p
        print("Contact phone number updated in Phonebook")
        #showall() #nested function call
           
        
    if found==False:
        print(n,"not found in phonebook")

def delete():
    n=input('Enter name whose number has to be deleted:')
    found=False

    if n in d:
        found=True
        p=input('Confirm deletion [y/n]??')
        if p.upper()=='Y':
            del d[n]
            print("Contact phone number deleted from Phonebook")         
        
    if found==False:
        print(n,"not found in phonebook")

def erase():
    d.clear()

#Menu-driven code
while True:
    print("PHONE BOOK OPERATIONS\n")
    print("1. ADD TO PHONE BOOK")
    print("2. SHOW PHONE BOOK")
    print("3. SEARCH IN PHONE BOOK")
    print("4. MODIFY CONTACT PHONE NUMBER")
    print("5. DELETE CONTACT PHONE NUMBER")
    print("6. CLEAR PHONEBOOK")
    print("7. EXIT")
    
    c=int(input("Enter ur choice:"))
    if c==1:
        append()
    elif c==2:
        showall()
    elif c==3:
        search()
    elif c==4:
        modify()
    elif c==5:
        delete()
    elif c==6:
        erase()       
    else:
        break

    
            
        

