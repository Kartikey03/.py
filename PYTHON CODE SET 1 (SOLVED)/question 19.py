list_1=list()
n=int(input("Enter Range:"))
for i in range(1,n+1):
    list_1.append(i**2)
print("First 5 element are:",list_1[:5])
print("Last 5 element are",list_1[-5:])
'''
Enter Range:30
First 5 element are: [1, 4, 9, 16, 25]
Last 5 element are [676, 729, 784, 841, 900]
'''
