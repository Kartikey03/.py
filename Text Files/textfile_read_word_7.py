#read from a text file and display words in reverse
fr=open("multiple2.txt","r")
s=fr.read()
word=s.split()

for w in word:
    print(w[::-1])
        

fr.close()
