#script to count and display the number of lower and upper case vowels in  a text file

fr=open("multiple2.txt","r")
s=fr.read()
print(s)
vc=0
for c in s:
    if c in 'aeiouAEIOU':
        vc+=1

print("multiple2.txt vowel count=",vc)
fr.close()



