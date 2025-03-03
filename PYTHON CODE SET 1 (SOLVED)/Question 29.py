num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
sorted_dict = {x: sorted(y) for x, y in num.items()}
print(sorted_dict)
"""
{'n1': [1, 2, 3], 'n2': [1, 2, 5], 'n3': [2, 3, 4]}
"""
