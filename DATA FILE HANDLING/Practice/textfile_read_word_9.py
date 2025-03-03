#read from a text file and display the count of is and a as separate words.
#matching can be case insensitive
fr=open("multiple2.txt","r")
s=fr.read()
word=s.split()
ic=0
ac=0
for w in word:
    if w.upper()=='IS':
        ic+=1
    elif w.upper()=='A':
        ac+=1
print("count of is=",ic)
print("count of a=",ac)

        

fr.close()
