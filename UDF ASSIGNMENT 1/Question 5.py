# QUESTION  5
# UDF that accepts the value of the Base and the Exponent and returns the Result of the Base Raised to the Power of exponent.
# If no value is Passed for the Exponent, then the Function should calculate Base raised to power 2.

def my_pow(base,exp=2):
    return base**exp
try :
    b=int(input("Enter the Value of base :"))
    e=int(input("Enter the Value of exponent :"))
    print(my_pow(b,e))

except ValueError:
    print(my_pow(b))


# Output 1
'''
Enter the Value of base :5
Enter the Value of exponent :3
125
'''
# Output 2
'''
Enter the Value of base :5
Enter the Value of exponent :
25
'''


