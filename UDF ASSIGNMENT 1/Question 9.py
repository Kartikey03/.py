# QUESTION  9
# UDF that receives a list of integers L and a search key, Key as parameters. 
# The Function should search Key in L and Return the Index Position of Key if it is Found in L, -1 otherwise.

def lsearch(L, key):
    if key in L:
        p = L.index(key)
        return p
    return -1

l = [1,2,3,4,5,6,7,8,9,10]
print(''' You Have the following List :
        ''', l)
k = int(input('Please enter the Key :'))
p = lsearch(l,k)
print('The Index Position of', k, 'is :', p)


#Output 1 
'''
 You Have the following List :
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Please enter the Key : 5
The Index Position of 5 is : 4
'''

# Output 2
'''
 You Have the following List :
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Please enter the Key : 11
The Index Position of 11 is : -1
'''
