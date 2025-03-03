# QUESTION  1(d)

#UDF to accept the temperature in celsius and convert it into fahrenheit from thew formula : C*9/5+32
#UDF Style 2
def temp2(n):
    s = n*9/5+32
    print('The Temperature in Fahrenheit is :', s)
n = int(input('Enter the Temperature in Celsius :'))
temp2(n)

#Output
'''
Enter the Temperature in Celsius : 37
The Temperature in Fahrenheit is : 98.6
'''
     
