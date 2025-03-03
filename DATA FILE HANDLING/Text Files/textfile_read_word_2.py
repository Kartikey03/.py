#read from a text file and display words that begin with letter 'A'
fr=open("multiple2.txt","r")
s=fr.read()
word=s.split()
print(s)
for w in word:
    if w[0]=='A':
        print(w)
        

fr.close()
