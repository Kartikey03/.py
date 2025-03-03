#QUESTION  1(c)

#UDF to Calculate the Factorial of a Number
#UDF Style 3
def fact3():
    from math import factorial as fact
    s = fact(n)
    return s
n = int(input('Enter the Number :'))
a = fact3()
print('The Factorial of', n, 'is :', a)

#Output
'''
Enter the Number : 5
The Factorial of 5 is : 120
'''

