ct={}
n=int(input("Enter how many key value pair:"))
for i in range(n):
    key=input("Enter class:")
    value=input("Enter name of class teacher:")
    ct[key]=value
print(ct)

search=input("Enter class whose class teacher you want to search:")
print(ct[search])

'''
Enter how many key value pair:3
Enter class:10E
Enter name of class teacher:Mr. KK Singh
Enter class:11C
Enter name of class teacher:Mr. Pankaj Mittal
Enter class:12C
Enter name of class teacher:Mrs. Meena Dogra
{'10E': 'Mr. KK Singh', '11C': 'Mr. Pankaj Mittal', '12C': 'Mrs. Meena Dogra'}
Enter class whose class teacher you want to search:12C
Mrs. Meena Dogra
'''
