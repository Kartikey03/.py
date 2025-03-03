
def tribo(f, s, t, n):
    d = f + s + t                
    print('Tribonacci Series :')
    i = 1
    while i <= p:
        n = f + s + t
        print(n)
        f = s
        s = t
        t = n
        i += 1
        d += n                 
    print('Sum of the Series including First 3 Terms :', d)
p = int(input('Enter the No. till how many terms you want to Print the series :'))
f = int(input('Enter the First term :'))
s = int(input('Enter the Second term :'))
t = int(input('Enter the Third term :'))
n = f + s + t  
tribo(f, s, t, n)


# Output
'''
Enter the No. till how many terms you want to Print the series :5
Enter the First term :1
Enter the Second term :1
Enter the Third term :1
Tribonacci Series :
3
5
9
17
31
Sum of the Series including First 3 Terms : 68
'''
