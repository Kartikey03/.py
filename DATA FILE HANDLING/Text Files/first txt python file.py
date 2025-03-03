fobj=open("first.txt","r")
fr=fobj.readlines()
print(fr)
c1=[]
c2=0
for i in fr:
    if i[0] in "aA":
        c1.append(i)
        c2+=1
print("the count of lines that begin with a/A is :", c2)
print("the lines that begin with a/A is :")
for f in c1:
    print(f)

fobj.close()
