#style 4
def calc_si_2(p1,r1,t1):
    si=(p1*r1*t1)/100
    return si


print("in calling block")
p1=int(input("Enter the principle:"))
r1=int(input("Enter the rate:"))
t1=int(input("Enter the time:"))

print("Simple Interest=",calc_si_2(p1,r1,t1))
      
print("back in calling block")

'''
in calling block
Enter the principle:2
Enter the rate:5
Enter the time:10
Simple Interest= 1.0
back in calling block
'''
