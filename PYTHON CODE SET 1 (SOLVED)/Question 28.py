dict_1={}
n=int(input("Enter number of key value pair:"))
for elememt in range(n):
    key=input("Enter Key")
    value=input("Enter Value")
    dict_1[key]=value

sort=sorted(dict_1.values(), reverse=True)
print("highest 3 values are",sort[0],sort[1],sort[2])
'''
Enter number of key value pair:5
Enter Key1
Enter Value98
Enter Key2
Enter Value12
Enter Key3
Enter Value45
Enter Key4
Enter Value99
Enter Key5
Enter Value11
highest 3 values are 99 98 45
'''
