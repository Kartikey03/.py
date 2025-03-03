#QUESTION  1(c)

#UDF to Calculate the Factorial of a Number
#UDF Style 1
def fact1():
    from math import factorial
    n = int(input('Enter the number :'))
    s = factorial(n)
    print('The Factorial of', n, 'is :', s)
fact1()

#Output
'''
Enter the number : 5
The Factorial of 5 is : 120
'''
