#Program to illustrate Insertion sort in Descending order
l=[8,6,2,5,3]
print('Unsorted list:',l)

for i in range(1,len(l)):
    temp=l[i]
    j=i
    while j>=1 and l[j-1]<temp:
        l[j]=l[j-1]  #right shifting
        j=j-1
    #inserting the element at the right position
    l[j]=temp
    print('List in current pass',l)

print('Sorted list:',l)

"""
Unsorted list: [8, 6, 2, 5, 3]
List in current pass [8, 6, 2, 5, 3]
List in current pass [8, 6, 2, 5, 3]
List in current pass [8, 6, 5, 2, 3]
List in current pass [8, 6, 5, 3, 2]
Sorted list: [8, 6, 5, 3, 2]
"""

