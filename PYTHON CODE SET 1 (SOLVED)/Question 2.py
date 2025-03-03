l=[]

n=int(input("Enter No. of entries:"))
for i in range(n):
    val=input("Enter matter:")
    l.append(val)
print("Given list is:",l)
for i in l:
    index=l.index(i)
    if index % 2 != 0:
        print(i*2)
'''
Enter No. of entries:4
Enter matter:33
Enter matter:ANMOL
Enter matter:jain
Enter matter:3
Given list is: ['33', 'ANMOL', 'jain', '3']
ANMOLANMOL
33
'''
