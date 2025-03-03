'''
print('creating text file.....')
fw = open('practice.txt','r')
print('text file created')

def display():
    r = fw.read()
    for c in r:
        c.isupper())

def write():
    fw.write(n + '')
    print('data added to your text file')

a = input('do you want to write in the file ? :')

if a == 'yes':
    n = input('enter a string :')
    write()
    fw.close()

elif a == 'no':
    fw.close()
    print('text file closed')

display()
'''

import pickle
l=[0,1,2,3,4,5,6,7,8,9]
f = open ('list.dat', 'wb')
pickle.dump(l,f)
f.close()


