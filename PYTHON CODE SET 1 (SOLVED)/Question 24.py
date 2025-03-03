dict_1={}
num=int(input("Enter dictionary range:"))
for element in range(1,num+1):
    key=element
    value=element*element
    dict_1[key]=value
print(dict_1)
'''
Enter dictionary range:15
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36,
7: 49, 8: 64, 9: 81, 10: 100, 11: 121,
12: 144, 13: 169, 14: 196, 15: 225}
'''
