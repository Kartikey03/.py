import csv
fr=open("stud.csv","r")
studreader=csv.reader(fr)
#print(studreader)

r=input("Enter the roll number to be searched: ")
for i in studreader:
    #print(type (i[0]),(i[0]))
    if i[0] [0]==r:
        print(i)
        
fr.close
