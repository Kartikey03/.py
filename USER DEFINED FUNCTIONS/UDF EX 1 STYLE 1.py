#function to find the square root.
def sq_1():
    print('i m in called block now')

    import math
    n=int(input('enter a number:'))
    s=math.sqrt(n)

    print('the square root of', n, 'is =',int(s))
    print('i m existing a block right now')

print('i m in calling block right now')
print(__name__)
sq_1()

print('i m back in calling block now')

#Output
'''
i m in calling block right now
__main__
i m in called block now
enter a number:2
the square root of n is = 1.4142135623730951
i m existing a block right now
i m back in calling block now
'''
