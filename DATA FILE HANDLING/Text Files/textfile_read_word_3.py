#read from a text file and display words that begin with an upper case or lower case vowel
fr=open("multiple2.txt","r")
s=fr.read()
word=s.split()

print(s)

for w in word:
    if w[0] in 'aeiouAEIOU':
        print(w)
        

fr.close()
