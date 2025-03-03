#using write() function to write a single string to  text file opened in write mode
print("Creating my first text file...")

#fileobjectname=open("filename.txt","mode")
fw=open("first.txt","w")
#write data to file
fw.write("Aakriti\n")
#close the file
fw.close()
print("data written to file...")
