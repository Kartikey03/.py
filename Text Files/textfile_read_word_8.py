#read from a text file and display the count of is and a as separate words
#matching is case-sensitive

fr=open("multiple2.txt","r")
s=fr.read()
word=s.split()
print(s)
ic=0
ac=0

for w in word:
    if w=='is':
        ic+=1
    elif w=='a':
        ac+=1
        
print("count of is=",ic)
print("count of a=",ac)

        

fr.close()
