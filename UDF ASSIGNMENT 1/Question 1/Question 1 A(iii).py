#QUESTION  1(a)

#UDF to calculate the sum of two integers accepted at run-time
#UDF Style 3
def sum_run3():
    n=int(input('Enter First Integer :'))                 #accept the integers
    m=int(input('Enter Second Integer :'))                        
    s = m+n                                                          #processing
    return s
a = sum_run3()                                                   #function call stmnt
print('The sum of the two integers is :', a)            #show the sum

#Output
'''
Enter First Integer : 2
Enter Second Integer : 6
The sum of the two integers is : 8
'''
