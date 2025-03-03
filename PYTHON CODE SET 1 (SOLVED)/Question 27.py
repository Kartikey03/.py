from collections import Counter
A = Counter({'a':100, 'b':200, 'c':300})
B = Counter({'a':300, 'b':200, 'd':400})
print(A + B)
'''
Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
'''
