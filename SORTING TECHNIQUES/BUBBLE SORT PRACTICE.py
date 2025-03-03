'''
l=[95,-1,38,2,100,65,78]

print('Unsorted list:',l)
n=len(l)

for i in range(n-1): #LOOP FOR THE PASSES
    for j in range(n-i-1):#INNER LOOP TO COMPARE ADJACENT ELEMENTS
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]  #SWAPPING 
    print('List in current pass',l)

    
print('Sorted list:',l)




l=[my ]

print('Unsorted list:',l)
n=len(l)

for i in range(n-1): 
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]  
    print('List in current pass',l)

    
print('Sorted list:',l)















l=[95,-1,38,2,100,65,78]

print('Unsorted list:',l)
n=len(l)

for i in range(n-1): #LOOP FOR THE PASSES
    for j in range(n-i-1):#INNER LOOP TO COMPARE ADJACENT ELEMENTS
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]  #SWAPPING 
    print('List in current pass',l)

    
print('Sorted list:',l)
'''














l=['is', 'fun', 'python']

print('Unsorted list:',l)
n=len(l)

for i in range(n-1): #LOOP FOR THE PASSES
    for j in range(n-i-1):#INNER LOOP TO COMPARE ADJACENT ELEMENTS
        if l[j]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]  #SWAPPING 
    print('List in current pass',l)

    
print('Sorted list:',l)
