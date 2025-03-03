list_1=[]
list_2=[1,2]
n=int(input("Enter number of entries:"))
for entry in range(n):
    value=int(input("Enter value:"))
    list_1.append(value)
print("List is",list_1)
list_2.extend(list_1)
print(list_2)
'''
Enter number of entries:3
Enter value:3
Enter value:4
Enter value:5
List is [3, 4, 5]
[1, 2, 3, 4, 5]
'''
