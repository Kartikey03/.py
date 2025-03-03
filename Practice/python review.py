# unary operator = + and - (used to represent the sign of a number)
'''
import keyword
print(keyword.kwlist)

x=1
x=2
print(x)
'''

l=[]
n=int(input('num of entries:'))
for i in range(n):
    v=int(input('enter value:'))
    l.append(v)
print("l=",l)
l.insert(0,l.pop())
print(l)