# QUESTION  1(d)

#UDF to accept the temperature in celsius and convert it into fahrenheit from thew formula : C*9/5+32
#UDF Style 1
def temp1():
    n = int(input('Enter the Temperature in Celsius :'))
    s = n*9/5+32
    print('The Temperature in Fahrenheit is :', s)
temp1()

#Output
'''
Enter the Temperature in Celsius : 100
The Temperature in Fahrenheit is : 212.0
'''
