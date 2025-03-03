#ILLUSTRATION OF INSERTION SORT
l=[8,6,2,5,3]
print('unsorted list :')
for i in range (1, len(l)):
    temp=l[i]
    j=i
    while j>=1 and l[j-1]>temp:
        l[j]=l[j-1]
        j=j-1
        l[j]=temp
        print('list in current pass :',l)
print('sorted list :',l)
