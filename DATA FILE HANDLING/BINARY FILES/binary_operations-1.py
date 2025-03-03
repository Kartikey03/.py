import pickle
def Append(l):  
    fwb=open("student1.dat","ab")
    pickle.dump(l,fwb)
    fwb.close()
    print("data written succsessfully to binary file")

def read():
    frb=open("student1.dat","rb")
    l=pickle.load(frb)
    print(l)
    l=pickle.load(frb)
    print(l)
    l=pickle.load(frb)
    print(l)
    l=pickle.load(frb)
    print(l)
    frb.close()

def readall():
    frb=open("student1.dat","rb")
    while True:
        try:
            l=pickle.load(frb)
            print(l)
        except EOFError:
            break
    frb.close()

def search_rno(r):
    frb=open("student1.dat","rb")
    found=0
    while True:
        try:
            l=pickle.load(frb)
            if r==l[0]:
                print(l)
                found=1
        except EOFError:
            break
    if found==0:
        print("Roll no",r,"does not exist.")
    frb.close()

def search_name(n):
    frb=open("student1.dat","rb")
    found=0
    while True:
        try:
            l=pickle.load(frb)
            if n==l[1]:
                print(l)
                found=1
        except EOFError:
            break
    if found==0:
        print("Name",n,"does not exist.")
    frb.close()

def update(r):
    import os
    frb=open("student1.dat","rb")
    fwb=open("temp.dat","wb")
    found=0
    while True:
        try:
            l=pickle.load(frb)
            if r==l[0]:
                l[1]=input("Enter the new name")
                l[2]=int(input("Enter the marks"))
                pickle.dump(l,fwb)

                found=1
            else:
                pickle.dump(l,fwb)
                
                
        except EOFError:
            break

    frb.close()
    fwb.close()
    os.remove("student1.dat")
    os.rename("temp.dat","student1.dat")

    if found==0:
        print("Roll no",r,"does not exist.")
    else:
        print("Record updated....")
        readall()
    

def delete(r):
    import os
    frb=open("student1.dat","rb")
    fwb=open("temp.dat","wb")
    found=0
    while True:
        try:
            l=pickle.load(frb)
            if r!=l[0]:
                pickle.dump(l,fwb)
            else:
                found=1
        except EOFError:
            break
    frb.close()
    fwb.close()
    os.remove("student1.dat")
    os.rename("temp.dat","student1.dat")

    if found==0:
        print("Roll no",r,"does not exist.")
    else:
        print("Record deleted....")
        readall()

    
    


#calling the UDFs
'''
Append([1,'Aakarsh',99])
Append([2,'Aakriti',98])
Append([3,'Abhinav',98])
Append([4,'Aditya',98])
Append([5,'Akshat',98])

Append([6,'Akshat Singh',97])
'''
print("showing all records")
#read()
readall()
print("search by name")
#search_name('Aakriti')    
#search_rno(1)
#update(12)
delete(5)

