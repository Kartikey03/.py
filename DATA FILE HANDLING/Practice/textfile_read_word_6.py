#read from a text file and display words that have length 4
fr=open("multiple2.txt","r")
s=fr.read()
word=s.split()

for w in word:
    if len(w)==4:
        print(w)
        

fr.close()
