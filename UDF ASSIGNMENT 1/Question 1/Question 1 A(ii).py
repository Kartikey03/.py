#QUESTION  1(a)

#UDF to calculate the sum of two integers accepted at run-time
#UDF Style 2
def sum_run2(n,m):
    s = m+n                                                             #processing
    print('The Sum of the two integers is :', s)          #show the sum
n=int(input('Enter First Integer :'))                        #accept the integers
m=int(input('Enter Second Integer :'))
sum_run2(n,m)                                                      #function call stmnt

#Output
'''
Enter First Integer : 2
Enter Second Integer : 3
The Sum of the two integers is : 5
'''
    
