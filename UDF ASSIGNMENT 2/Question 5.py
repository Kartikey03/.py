
def d_sum(n):
    s = 0
    while n > 0:
        d = n%10
        s+=d
        n=n//10
    return(s)

def d_count(n):
    c = 0
    while n > 0:
        d =n%10
        c+=1
        n =n//10
    return(c)

n = int(input('Enter an Integer :'))
a = d_sum(n)
b = d_count(n)
print('Sum of the Digits of', n, 'is :', a)
print('The Count of the Digits in', n, 'is :', b)


# Output
'''
Enter an Integer :35
Sum of the Digits of 35 is : 8
The Count of the Digits in 35 is : 2
'''
