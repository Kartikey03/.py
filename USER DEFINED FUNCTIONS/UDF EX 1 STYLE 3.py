def sq_3():
    print('i m in called block now')
    import math
    n=int(input('enter a number :'))   #take input
    s=math.sqrt(n)                           #process
    print('i m existing called block now and returning the output to calling block')
    return s
print('i m in calling block right now')
print(__name__)
#first way of calling a udf with return type
ans=sq_3()        #function call statement is an expression
print('i m in calling block now and displaying the output')
print('the square root of n =',ans)   #show output
print('calling the function again. . . ')
#second way of calling a udf with return type
print(sq_3())     #function call statement is written in print() function
print('i m back in calling block now and displaying the output')
print('the square root of n =', ans)   #show output

'''
i m in calling block right now
__main__
i m in called block now
enter a number :2
i m existing called block now and returning the output to calling block
i m in calling block now and displaying the output
the square root of n = 1.4142135623730951
calling the function again. . . 
i m in called block now
enter a number :2
i m existing called block now and returning the output to calling block
1.4142135623730951
i m back in calling block now and displaying the output
the square root of n = 1.4142135623730951
'''


