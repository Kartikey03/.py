
def per_num(n):
    s = 0
    for i in range(1, n):
        if n%i == 0:
            s = s+i
    return s == n
n = int(input('Enter A Number :'))
a = per_num(n)
print(a)


# Output 1
'''
Enter A Number :6
True
'''
# Output 2
'''
Enter A Number :100
False
'''
    
