#BUBBLE SORT IN ASCENDING ORDER
l=[42,29,74,11,65,58]

print('Unsorted list:',l)
n=len(l)

for i in range(n-1): #LOOP FOR THE PASSES
    for j in range(n-i-1):#INNER LOOP TO COMPARE ADJACENT ELEMENTS
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]  #SWAPPING 
    print('List in current pass',l)

    
print('Sorted list:',l)
	
"""
O/P
Unsorted list: [42, 29, 74, 11, 65, 58]
List in current pass [29, 42, 11, 65, 58, 74]
List in current pass [29, 11, 42, 58, 65, 74]
List in current pass [11, 29, 42, 58, 65, 74]
List in current pass [11, 29, 42, 58, 65, 74]
List in current pass [11, 29, 42, 58, 65, 74]
Sorted list: [11, 29, 42, 58, 65, 74]
"""
