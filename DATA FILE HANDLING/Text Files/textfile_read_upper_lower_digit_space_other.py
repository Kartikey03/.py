fw=open("demo.txt","w")
fw.write("AbcD_123@gmail.com is my email address")
fw.close()

#script to count and display the number of lower and upper case letters in  a text file

fr=open("demo.txt","r")
s=fr.read()
print("demo.txt contents:",s)
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
fr.close()

print("multiple2.txt upper case letter count=",uc)
print("multiple2.txt lower case letter count=",lc)
print("multiple2.txt digit count=",dc)
print("multiple2.txt space count=",sp)
print("multiple2.txt other characters count=",ot)


'''
demo.txt contents: AbcD_123@gmail.com is my email address
multiple2.txt upper case letter count= 2
multiple2.txt lower case letter count= 26
multiple2.txt digit count= 3
multiple2.txt space count= 4
multiple2.txt other charcters count= 3
'''

    





