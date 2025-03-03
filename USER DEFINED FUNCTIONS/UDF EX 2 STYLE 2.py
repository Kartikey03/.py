def add_2(n1,n2):
    print("i m in called block now")
    s=n1+n2
    print("the sum of",num1,"and",num2,"=",s)
    print("i m exiting called block now")
print("i m in calling block right now")
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
add_2(num1,num2)
print("i m back in calling block now")

'''
i m in calling block right now
enter 1st number:2
enter 2nd number:3
i m in called block now
the sum of 2 and 3 = 5
i m exiting called block now
i m back in calling block now
'''
