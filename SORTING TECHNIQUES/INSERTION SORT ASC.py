#Program to illustrate Insertion sort in Ascending order
l=[8,6,2,5,3]
print('Unsorted list:',l)

for i in range(1,len(l)):
    temp=l[i]
    j=i
    while j>=1 and l[j-1]>temp:
        l[j]=l[j-1]  #right shifting
        j=j-1
    #inserting the element at the right position
    l[j]=temp
    print('List in current pass',l)

print('Sorted list:',l)

"""
Unsorted list: [8, 6, 2, 5, 3]
List in current pass [6, 8, 2, 5, 3]
List in current pass [2, 6, 8, 5, 3]
List in current pass [2, 5, 6, 8, 3]
List in current pass [2, 3, 5, 6, 8]
Sorted list: [2, 3, 5, 6, 8]
"""

