#QUESTION  3
#UDF that accepts an Integer n and Displays the all Prime Numbers in ther range 1 to n.

def prime(n):
    if n <= 1:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    else:
        return True
    
n = int(input('Enter the Number till where you want to print the Prime Numbers :'))
print('The Prime Numbers in the Range 1 to', n, 'are :')
for i in range (1, n):
    if prime(i):
        print(i, end = ', ')
prime(n)


# Output
'''
Enter the Number till where you want to print the Prime Numbers : 10
The Prime Numbers in the Range 1 to 10 are :
2, 3, 5, 7
'''
