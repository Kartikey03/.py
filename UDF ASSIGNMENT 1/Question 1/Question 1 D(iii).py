# QUESTION  1(d)

#UDF to accept the temperature in celsius and convert it into fahrenheit from thew formula : C*9/5+32
#UDF Style 3
def temp1():
    n = int(input('Enter the Temperature in Celsius :'))
    s = n*9/5+32
    return s
a = temp1()
print('The Temperature in Fahrenheit is :', a)

#Output
'''
Enter the Temperature in Celsius : 50
The Temperature in Fahrenheit is : 122.0
'''
