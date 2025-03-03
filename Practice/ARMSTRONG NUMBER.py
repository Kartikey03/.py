def armstrong(n):
    a = 0
    m = n
    while n>0:
        d = n%10
        a += d ** 3
        n = n // 10
    if m == a:
        print('armstrong')
    else:
        print('not an armstrong')
armstrong(153)
armstrong(15)
armstrong(370)
