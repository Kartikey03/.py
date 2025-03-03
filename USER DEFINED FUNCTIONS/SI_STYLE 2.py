#style 2
def calc_si_2(p1,r1,t1):
    si=(p1*r1*t1)/100
    print("simple interest=",si)


print("in calling block")
p1=int(input("Enter the principle:"))
r1=int(input("Enter the rate:"))
t1=int(input("Enter the time:"))

calc_si_2(p1,r1,t1)
print("back in calling block")
