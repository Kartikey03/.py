def sq_4(n):
    print('i m in called block now')
    import math
    s=math.sqrt(n)                           #process
    print('i m existing called block now and returning the output to calling block')
    return s
print('i m in calling block right now')
print(__name__)
n=int(input('enter a number :'))   #take input
#calling a udf with arguments and return type
ans=sq_4(n)        #function call statement is an expression
print('i m back in calling block now and displaying the output')
print('the square root of n =',ans)   #show output

'''
i m in calling block right now
__main__
enter a number :2
i m in called block now
i m existing called block now and returning the output to calling block
i m back in calling block now and displaying the output
the square root of n = 1.4142135623730951
'''
