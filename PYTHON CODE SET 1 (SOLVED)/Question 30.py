dict_1={1:[1,2,3],2:45,3:[5,6,7],4:54}
count=0
for element in dict_1:
    if type(dict_1[element])==list:
           count+=1

print("list as value in dict are",count)
'''
list as value in dict are 2
'''
