l=[]
n=int(input("Enter number of entries:"))
for i in range(n):
    val=int(input("Enter Value:"))
    l.append(val)

print(l)

l.remove(10)
l.append(10)
print(l)
'''
Enter number of entries:4
Enter Value:10
Enter Value:20
Enter Value:30
Enter Value:40
[10, 20, 30, 40]
[20, 30, 40, 10]
'''
