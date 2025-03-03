#UDF 1
def power(b,p):
    y=b**p
    return y

#UDF 2
def calcsquare(x):
    a=power(x,2)  #nested func.call
    return a

#calling block
n=5
result=calcsquare(n)+power(3,3)
print(result)

'''
52
'''
