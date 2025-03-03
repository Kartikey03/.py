#script to count and display the number of lower and upper case letters in  a text file

fr=open("multiple2.txt","r")
s=fr.read()
print(s)
lc=0
uc=0
dc=0
sp=0
ot=0

for c in s:
    if c.isupper():
        uc+=1
    elif c.islower():
        lc+=1
    elif c.isdigit():
        dc+=1
    elif c.isspace():
        sp+=1
    else:
        ot+=1

print("multiple2.txt upper case letter count=",uc)
print("multiple2.txt lower case letter count=",lc)
print("multiple2.txt digit count=",dc)
print("multiple2.txt space count=",sp)
print("multiple2.txt other charcters count=",ot)
    

fr.close()



