#Script to display the entire text file with every space displayed as '#'
fw=open("capital.txt",'w')
fw.write("New Delhi is the capital of India")
fw.close()
print("Content written to file...")


fr=open("capital.txt",'r')
s=fr.read()
print("Original file",s)
print("file as required for display")
s1=''
for c in s:
    if c.isspace():
        s1+='#'
    else:
        s1+=c  #s1=s1+c

print(s1)
fr.close()

#New Delhi is the capital of India
#New#Delhi#is#the#capital#of#India
