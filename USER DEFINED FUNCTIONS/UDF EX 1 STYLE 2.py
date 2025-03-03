def sq_2(n):
    print('i m in called block now')
    import math
    s=math.sqrt(n)
    print('the square root of n is =',s)
    print('i m existing called block now')
print('i m in calling block right now')
print(__name__)
n=int(input('enter a number :'))
sq_2(n)
print('i m back in calling block now')

'''
i m in calling block right now
__main__
enter a number :2
i m in called block now
the square root of n is = 1.4142135623730951
i m existing called block now
i m back in calling block now
'''
