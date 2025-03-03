
def armstrong(n):
    a = 0
    m = n
    while n>0:
        d = n%10
        a += d ** 3
        n = n // 10
    if m == a:
        return True
    else:
        return False
n = int(input('Enter a Number :'))
for i in range(1, n+1):
    if armstrong(i):
        print(i, end = ', ')
armstrong(n)


# Output
'''
Enter a Number :500
1, 153, 370, 371, 407
'''
