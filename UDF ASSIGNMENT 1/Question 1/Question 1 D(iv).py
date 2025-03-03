# QUESTION  1(d)

#UDF to accept the temperature in celsius and convert it into fahrenheit from thew formula : C*9/5+32
#UDF Style 4
def temp4(n):
    s = n*9/5+32
    return s
n = float(input('Enter the Temperature in Celsius :'))
a = temp4(n)
print('The Temperature in Fahrenheit is :', a)

#Output
'''
Enter the Temperature in Celsius : 37.5
The Temperature in Fahrenheit is : 99.5
'''
     
