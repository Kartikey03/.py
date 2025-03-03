#QUESTION  6
# UDF that accepts two Strings as parameters and compares them. The UDF should return 1, if the first string is Greater
# than the second string, 0 if both Strings are equal and -1 if the First string is smaller than the Second string.

def compare(s1, s2):
    if s1 == s2:
        return 0
    elif s1 > s2:
        return 1
    elif s1 < s2:
        return -1
s1 = input('Enter the First String :')
s2 = input('Enter the Second string :')
a = compare(s1, s2)
print('The Result is :', a)


# Output 1
'''
Enter the First String :python
Enter the Second string :pythoN
The Result is : 1
'''

#Output 2
'''
Enter the First String :Python
Enter the Second string :python
The Result is : -1
'''

#Output 3
'''
Enter the First String :python
Enter the Second string :python
The Result is : 0
'''
