
def armstrong(n):
    a = 0
    m = n
    while n > 0 :
        d = n % 10
        a += d ** 3
        n = n // 10
    if m == a:
        print('Yes, it is an Armstrong Number.')
    else:
        print('No, it is not an Armstrong Number.')
n = int(input('Enter a Number :'))
armstrong(n)


# Output 1
'''
Enter a Number :153
Yes, it is an Armstrong Number.
'''
# Output 2
'''
Enter a Number :35
No, it is not an Armstrong Number.
'''
