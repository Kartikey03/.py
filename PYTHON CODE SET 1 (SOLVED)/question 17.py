list_1=[]
n=int(input("Enter number of entries:"))
for entry in range(n):
    value=int(input("Enter value:"))
    list_1.append(value)
print("List is",list_1)

list_1.sort()

print("Smallest Numeber is:",list_1[0])
'''
Enter number of entries:4
Enter value:23
Enter value:32
Enter value:45
Enter value:12
List is [23, 32, 45, 12]
Smallest Numeber is: 12
'''
