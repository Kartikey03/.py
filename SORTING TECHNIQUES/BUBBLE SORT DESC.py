#BUBBLE SORT IN ASCENDING ORDER
l=[42,29,74,11,65,58]

print('Unsorted list:',l)
n=len(l)

for i in range(n-1): #LOOP FOR THE PASSES
    for j in range(n-i-1):#INNER LOOP TO COMPARE ADJACENT ELEMENTS
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]  #SWAPPING 
    print('List in current pass',l)

    
print('Sorted list:',l)
	
"""
O/P
Unsorted list: [42, 29, 74, 11, 65, 58]
List in current pass [42, 74, 29, 65, 58, 11]
List in current pass [74, 42, 65, 58, 29, 11]
List in current pass [74, 65, 58, 42, 29, 11]
List in current pass [74, 65, 58, 42, 29, 11]
List in current pass [74, 65, 58, 42, 29, 11]
Sorted list: [74, 65, 58, 42, 29, 11]
"""
