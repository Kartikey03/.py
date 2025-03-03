str=input("Enter string:")
l=[]
for i in str:
    if str.count(i)>1and i not in l:
        l.append(i)
for i in l:
    str=str.replace(i,"")

print(str)

'''
Enter string:hello world
he wrd
'''
