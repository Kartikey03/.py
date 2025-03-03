def add_4(n1,n2):
    print("i m in called block now")
    s=n1+n2
    return s
print("i m in calling block right now")
num1=int(input("enter 1st number:"))
num2=int(input("enter 2nd number:"))
ans=add_4(num1,num2)
print("i m back in calling block now")
print ("sum",ans)

'''
i m in calling block right now
enter 1st number:5
enter 2nd number:6
i m in called block now
i m back in calling block now
sum 11
'''
