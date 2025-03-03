l=[]
n=int(input("Enter No. of Subject:"))
for i in range(n):
    val=int(input("Enter Marks(Out Of 50):"))
    l.append(val)
print("Given list is:",l)
a=sum(l)
print("Total marks are:",a)
b=n*50
print("Total marks:",b)
percent=(a/b)*100
print("Percentage is",percent)
"""
Enter No. of Subject:5
Enter Marks(Out Of 50):45
Enter Marks(Out Of 50):47
Enter Marks(Out Of 50):46
Enter Marks(Out Of 50):48
Enter Marks(Out Of 50):49
Given list is: [45, 47, 46, 48, 49]
Total marks are: 235
Total marks: 250
Percentage is 94.0
"""
