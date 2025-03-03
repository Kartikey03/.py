def power_4(b,e):
    p=b**e
    return p
print('i m in calling block right now')
base=int(input('enter base:'))
exp=int(input('enter exponent'))
ans=power_4(base,exp)
print('i m back in calling block now')
print(base,'raised to the power of', exp, '=', ans)

'''
i m in calling block right now
enter base:5
enter exponent2
i m back in calling block now
5 raised to the power of 2 = 25
'''
