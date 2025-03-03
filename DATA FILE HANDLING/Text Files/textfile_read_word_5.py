#read from a text file and display words that do not begin with an upper case or lower case vowel
fr=open("multiple2.txt","r")
s=fr.read()
word=s.split()
for w in word:
    if w[0] not in 'aeiouAEIOU':
        print(w)
        

fr.close()
