#QUESTION  1(a)
#UDF to calculate the sum of two integers accepted at run-time
#UDF Style 1

def sum_run():
    n=int(input('Enter First Integer :'))                 #accept the integers
    m=int(input('Enter Second Integer :'))                        
    s = m+n                                                          #processing
    print('The sum of the two integers is :', s)        #show the sum
sum_run()                                                          #function call stmnt

#Output
'''
Enter First Integer : 2
Enter Second Integer : 3
The sum of the two integers is : 5
'''
