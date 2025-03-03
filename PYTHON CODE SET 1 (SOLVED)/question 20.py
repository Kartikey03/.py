list_1=list()
list_2=list()
n=int(input("Enter range of list:"))
for element in range(n):
    value=int(input("Enter value:"))
    list_1.append(value)
print("Given list:",list_1)
for element in list_1:
    if list_1.count(element)<2:
        list_2.append(element)
    if list_1.count(element)>=2 and element not in list_2:
        list_2.append(element)
print(list_2)
'''
Enter range of list:5
Enter value:1
Enter value:2
Enter value:2
Enter value:3
Enter value:4
Given list: [1, 2, 2, 3, 4]
[1, 2, 3, 4]
'''
