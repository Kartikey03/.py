#Script to send multiple strings to a text file using write() function
print("Creating my third text file...")

#fileobjectname=open("filename.txt","mode")
fw=open("manynames.txt","a") #mode is 'a'
n=int(input("how many names:"))
for i in range(n):
    name=input("Enter the name:")
    fw.write(name + '\n')
    
#close the file
fw.close()


print("data written to file...")
