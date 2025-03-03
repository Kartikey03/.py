dict={}
n=int(input("No. of key value pair:"))
for i in range(n):
    key=int(input("Enter key(Numeric)"))
    value=input("Enter Value")
    dict[key]=value

search_key=int(input("Enter key you want to search"))
if search_key in dict:
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")
'''
No. of key value pair:4
Enter key(Numeric)1
Enter Valuemonday
Enter key(Numeric)2
Enter Valuetuesday
Enter key(Numeric)3
Enter Valuewednesday
Enter key(Numeric)4
Enter Valuethrusday
Enter key you want to search4
Key is present in the dictionary
'''
