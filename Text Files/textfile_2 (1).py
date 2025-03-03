#using write() function to write a single string to  text file opened in append mode

print("Creating my first text file...")

#fileobjectname=open("filename.txt","mode")
fw=open("first.txt","a") #mode is 'a'
#write data to file
fw.write("Aditya\n")
#close the file
fw.close()


print("data written to file...")
