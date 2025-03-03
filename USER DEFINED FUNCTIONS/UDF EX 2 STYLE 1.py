def add_1():
    print("i m in called block now")
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))
    s=num1+num2
    print("the sum of",num1,"and",num2,"=",s)
    print("i m exiting called block now")

print("i m in calling block right now")

add_1() 
print("i m back in calling bock now")

'''
i m in calling block right now
i m in called block now
enter 1st number:2
enter 2nd number:3
the sum of 2 and 3 = 5
i m exiting called block now
i m back in calling bock now
'''
