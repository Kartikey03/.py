def fibo(f, s, n):
    print('Fibonacci Series :')
    i = 1
    while i <= p:
        n = f + s
        print(n)
        f = s
        s = n
        i += 1
              
p = int(input('Enter the No. till how many terms you want to Print the series :'))
f = int(input('Enter the First term :'))
s = int(input('Enter the Second term :'))
n = f+ s  
fibo(f, s, n)


# Output
'''
Enter the No. till how many terms you want to Print the series : 5
Enter the First term : 1
Enter the Second term : 1
Fibonacci Series :
2
3
5
8
13
'''
    
