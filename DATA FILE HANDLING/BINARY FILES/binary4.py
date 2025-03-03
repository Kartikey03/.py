#store multiple records stored as nested list to a binary file
import pickle
def Append(l):
    
    fwb=open("student.dat","ab")
    pickle.dump(l,fwb)
    fwb.close()
    print("Data written successfully to binary file")

def read():
    frb=open("student.dat","rb")
    l1=pickle.load(frb)
    l2=pickle.load(frb)
    print(l1)
    print(l2)
    frb.close
    

def readall():
    frb=open("student.dat","rb")
    while True:
        try:
            l=pickle.load(frb)
            print(l)
        except EOFError:
            break
    frb.close()

#calling the udfs

#Append(['Aakarsh'])
#Append(["Akriti"])
#Append(["Abhinav"])
read()
#readall()
