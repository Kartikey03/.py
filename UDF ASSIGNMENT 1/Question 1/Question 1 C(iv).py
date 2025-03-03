# QUESTION  1(c)

#UDF to Calculate the Factorial of a Number
#UDF Style 4
def fact4(n):
    from math import factorial as fact
    s = fact(n)
    return s
n =  int(input('Enter the Number :'))
a = fact4(n)
print('The Factorial of', n, 'is :', a)

#Output
'''
Enter the Number : 7
The Factorial of 7 is : 5040
'''
