
fw=open("capital.txt",'w')
fw.write("New Delhi is the capital of India")
fw.close()
print("Content written to file...")


fr=open("capital.txt",'r')
s=fr.read()
print("Original file",s)
print("file as required for display")

for c in s:
    if c.isspace():
        print("#",end='')
    else:
        print(c,end='')

fr.close()

#New Delhi is the capital of India
#New#Delhi#is#the#capital#of#India
