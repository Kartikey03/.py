#QUESTION  1(c)

#UDF to Calculate the Factorial of a Number
#UDF Style 2
def fact2(n):
    from math import factorial as fact
    s = fact(n)
    print('The Factorial of', n, 'is :', s)
n = int(input('Enter the Number :'))
fact2(n)

#Output
'''
Enter the Number : 10
The Factorial of 10 is : 3628800
'''
