def add_3():
    print("i m in called block now")
    num1=int(input("enter 1st number:"))
    num2=int(input("enter 2nd number:"))
    s=num1+num2
    print("i m exiting called block now")
    return s
print("i m in calling block right now")
ans=add_3()
print("i m back in the calling block now")
print("sum=",ans)

'''
i m in calling block right now
i m in called block now
enter 1st number:2
enter 2nd number:3
i m exiting called block now
i m back in the calling block now
sum= 5
'''
