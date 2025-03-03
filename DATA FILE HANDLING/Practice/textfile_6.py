fw=open("multiple3.txt","w")
lines=[]
n=int(input("Enter how many lines:"))
for i in range(n):
    l=input("Enter a line:")
    lines.append(l+'\n')
    
fw.writelines(lines)
fw.close()
print("lines written to file")
