fr = open("text.txt","r")

lc = 0
for i in fr.read():
    if i.islower():
        lc+=1



print("Total Lower Case Letters in Text file is",lc)