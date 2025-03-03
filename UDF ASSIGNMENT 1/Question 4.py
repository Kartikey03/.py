# QUESTION  4
# UDF that accepts an Integer n and returns the sum of all Natural numbers from 1 to n.

def sum_n(n):
        s = range(1, n+1)
        fsum = sum(s) 
        print('The Sum of the Natural Numbers is :', fsum)
n = int(input('Enter the Number till where you want to print the sum of natural numbers :'))
sum_n(n)


# Output
'''
Enter the Number till where you want to print the sum of natural numbers : 10
The Sum of the Natural Numbers is : 55
'''
        
    
