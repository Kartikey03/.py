#read from a text file 
fr=open("multiple2.txt","r")
s=fr.read()
word=s.split()
print("file contents:")
print(s)


print("file words:")
print(word)

fr.close()
