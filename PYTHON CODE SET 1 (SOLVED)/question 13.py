str=input("Enter String:")
sum_digit=0
for i in str:
    if i.isdigit()==True:
        a=int(i)
        sum_digit=sum_digit+a

print(sum_digit)
'''
Enter String:123abd45
15
'''
