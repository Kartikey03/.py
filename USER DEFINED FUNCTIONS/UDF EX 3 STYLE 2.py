def power_2(b,e):
    p=b**e
    print(b,'raised to the power of', e, '=', p)
print('i m in calling block right now')
base=int(input('enter base:'))
exp=int(input('enter exponent'))
power_2(base,exp)
print('i m back in calling block now')

'''
i m in calling block right now
enter base:5
enter exponent2
5 raised to the power of 2 = 25
i m back in calling block now
'''
