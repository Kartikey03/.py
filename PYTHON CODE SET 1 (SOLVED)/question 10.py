dic={}
n=int(input("Enter no. of customer:"))
for i in range(n):
    d={}
    name=input("Enter Name:")
    d[Item]=input("Enter Item:")
    d[Cost]=input("Enter Cost:")
    d[Phn]= input("Enter Phone No.:")
    dic[name]=d
print("NAME\t\tITEM\t\tCOST\t\tPHONE")
for name in dic:
    print(name,"\t\t",dic[name]["Item"],"\t\t",dic[name]["Cost"],"\t\t",dic [name]["Phn"])
