l=[34, -6, 12, -3, 45, 25]

print('Unsorted list:',l)
n=len(l)

for i in range(n-1): 
    for j in range(n-i-1):
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j] 
    print('List in current pass',l)
print('The Status of the List after Fourth Pass is :',l)

    
print('Sorted list:',l)

'''
Unsorted list: [34, -6, 12, -3, 45, 25]
List in current pass [34, 12, -3, 45, 25, -6]
List in current pass [34, 12, 45, 25, -3, -6]
List in current pass [34, 45, 25, 12, -3, -6]
List in current pass [45, 34, 25, 12, -3, -6]
List in current pass [45, 34, 25, 12, -3, -6]
Sorted list: [45, 34, 25, 12, -3, -6]
'''
