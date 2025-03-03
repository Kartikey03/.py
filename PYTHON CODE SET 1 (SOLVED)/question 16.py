list=[]
n=int(input("Enter number of entries:"))
for entry in range(n):
    value=int(input("Enter value:"))
    list.append(value)

result=1
for element in list:
    result=result*element

print("Product of list",list,"is",result)

'''
Enter number of entries:4
Enter value:1
Enter value:2
Enter value:3
Enter value:4
Product of list [1, 2, 3, 4] is 24
'''
