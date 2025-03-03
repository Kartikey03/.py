#QUESTION  7
# UDF that accepts a list of integers L and an integer Variable O as parameters. The UDF should use BUBBLE SORT METHOD
# to sort the list in Ascending Order if the value received in O is 'A' or in Descending Order if the Value received in O is 'D'.

k = int(input('Enter number of elements to be inserted in the list :'))
l = []
for i in range(0, k):
    k = int(input('Enter the Element :'))
    l.append(k)
O = input('Enter A for ascending and D for Descending :')
print('Unsorted List :', l)
n = len(l)

#Ascending Order
if O.lower() == 'a':
    for k in range(0, n-1):
        for j in range(0, n-k-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print('Sorted List is :', l)
    
# Descending Order
elif O.lower() == 'd':
    for  k in range(0, n-1):
        for j in range(0, n-k-1):
            if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print('Sorted List is :', l)
    
else:
    print('Invalid Value for the order Type')


#Output 1 (Ascending Order)
'''
Enter number of elements to be inserted in the list :6
Enter the Element :123
Enter the Element :543
Enter the Element :65
Enter the Element :2
Enter the Element :55
Enter the Element :23
Enter A for ascending and D for Descending :a
Unsorted List : [123, 543, 65, 2, 55, 23]
Sorted List is : [2, 23, 55, 65, 123, 543]
'''

# Output 2 (Descending Order)
'''
Enter number of elements to be inserted in the list :6
Enter the Element :45
Enter the Element :78
Enter the Element :89
Enter the Element :23
Enter the Element :12
Enter the Element :54
Enter A for ascending and D for Descending :d
Unsorted List : [45, 78, 89, 23, 12, 54]
Sorted List is : [89, 78, 54, 45, 23, 12]
'''
