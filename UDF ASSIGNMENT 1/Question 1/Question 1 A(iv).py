#QUESTION  1(a)

#UDF to calculate the sum of two integers accepted at run-time
#UDF Style 4
def sum_run4(n,m):                                              
    s= n+m                                                      #processing
    return s                                                    #return stmnt
n=int(input('Enter First Integer :'))                 #accept the integers
m=int(input('Enter Second Integer :'))
a=sum_run4(n,m)                                          #func call stmnt                                         
print('The sum of the Integers are :', a)         #print the output

#Output
'''
Enter First Integer : 5
Enter Second Integer : 5
The sum of the Integers are : 10
'''
