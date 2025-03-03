#read from a text file 
fr=open("multiple2.txt","r") #read mode
s=fr.read()  #fw.write(s)
print("multiple2.txt contains:")
print(s)
fr.close()

print("reading specific number of charcters from multiple2.txt")
fr=open("multiple2.txt","r")
#1
s=fr.read(5)
print(s)
#2 read resumes from 6th
s=fr.read(9)
print(s)
#3
s=fr.read()
print(s)
fr.close()


