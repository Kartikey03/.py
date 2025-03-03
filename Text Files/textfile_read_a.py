fr=open("demo.txt",'r')
s=fr.read()

count=0
for c in s:
    if c=='a':
        count+=1

print("count of a=",count)
        
fr.close()
