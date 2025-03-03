fr = open("C:\\Users\\Pratham\\Desktop\\CS Everything\\reading string\\text.txt")

uc = 0
for i in fr.read():
    if i.isupper():
        uc+=1



print("Total Upper Case Letters in Text file is",uc)
        