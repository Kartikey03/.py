#QUESTION  2
# UDF that accepts an Integer as Parameter and Returns True if it is a Prime Number, False Otherwise.

def prime(n):
    if n == 1:
        return False             # False beacuse 1 is Niether Prime nor Composite 
    elif n == 2:
        return True                    # 2 is a Prime No. Therefore Returning True
    else:
        for i in range(2, n):
            if (n % i == 0):
                return False      # Returning False when the Remainder will be 0 on dividing
        else:
            return True    
n = int(input("Enter the Number :"))
a = prime(n)
print(a)                    # Printing the Output


# Output 1
'''
Enter the Number : 119
False, it is not a Prime Number
'''

# Output 2
'''
Enter the Number : 23
True, it is a Prime Number
'''
