dict_1={}
n=int(input("Enter number of key value pair:"))
for elememt in range(n):
    key=input("Enter Key")
    value=input("Enter Value")
    dict_1[key]=value
print("Dictionary is",dict_1)                                
list_1=list(dict_1.items())
list_1.sort()          
dict_2=dict(list_1) 
print("Sorted Dictionary",dict_2) 
'''
Enter number of key value pair:4
Enter Keysam
Enter Value45
Enter Keyram
Enter Value56
Enter Keyjay
Enter Value56
Enter Keyajay
Enter Value12
Dictionary is {'sam': '45', 'ram': '56', 'jay': '56', 'ajay': '12'}
Sorted Dictionary {'ajay': '12', 'jay': '56', 'ram': '56', 'sam': '45'}
'''
