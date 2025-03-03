
n = int(input("Enter a Number :"))
def perfect_n(n):
    l = []
    for i in range(1,n):
        s = 0
        for k in range(1,i):
            if i%k == 0:
                s += k
        if s == i:
            l.append(i)
    return l
print("The Perfect numbers in range 1 To", n, "are :")
for k in perfect_n(n):
    print(k)


# Output
'''
Enter a Number :10000
The Perfect numbers in range 1 To 10000 are :
6
28
496
8128
'''



