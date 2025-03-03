l=[12, 14, -54, 64, 90, 24]

print('Unsorted list:',l)
n=len(l)

for i in range(n-1): 
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j] 
    print('List in current pass',l)

    
print('Sorted list:',l)

'''
Unsorted list: [12, 14, -54, 64, 90, 24]
List in current pass [12, -54, 14, 64, 24, 90]
List in current pass [-54, 12, 14, 24, 64, 90]
List in current pass [-54, 12, 14, 24, 64, 90]
List in current pass [-54, 12, 14, 24, 64, 90]
List in current pass [-54, 12, 14, 24, 64, 90]
Sorted list: [-54, 12, 14, 24, 64, 90]
'''
