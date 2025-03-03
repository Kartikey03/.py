# QUESTION  8
# UDF that accepts a list of integers L and an integer Variable O as parameters. The UDF should use INSERTION SORT METHOD
# to sort the list in Ascending Order if the value received in O is 'A' or in Descending Order if the Value received in O is 'D'.

k = int(input('Enter number of elements to be inserted in the list :'))
l = []
for i in range(0, k):
    k = int(input('Enter the Element :'))
    l.append(k)
O = input('Enter A for ascending and D for Descending :')
print('Unsorted List :', l)
n = len(l)

#Ascending
if O.lower() == 'a':
    for i in range(1,len(l)):
        t = l[i]
        j = i
        while j >= 1 and l[j-1] > t:
            l[j] = l[j-1]
            j = j-1
        l[j] = t
    print('Sorted list:',l)
    
#Descending
elif O.lower() == 'd':
    for i in range(1,len(l)):
        t = l[i]
        j = i
        while j >= 1 and l[j-1] < t:
            l[j] = l[j-1]
            j = j-1
        l[j] = t
    print('Sorted list:',l)
    
else:
    print('Invalid Value for the order Type')


# Output 1 (Descending Order)
'''
Enter number of elements to be inserted in the list :6
Enter the Element :34
Enter the Element :56
Enter the Element :23
Enter the Element :78
Enter the Element :12
Enter the Element :67
Enter A for ascending and D for Descending :d
Unsorted List : [34, 56, 23, 78, 12, 67]
Sorted list: [78, 67, 56, 34, 23, 12]
'''

# Output 2 (Ascending Order)
'''
Enter number of elements to be inserted in the list :6
Enter the Element :45
Enter the Element :65
Enter the Element :23
Enter the Element :34
Enter the Element :43
Enter the Element :87
Enter A for ascending and D for Descending :a
Unsorted List : [45, 65, 23, 34, 43, 87]
Sorted list: [23, 34, 43, 45, 65, 87]
'''
