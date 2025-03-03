#style 1
def calc_si_1():
    p=int(input("Enter the principle:"))
    r=int(input("Enter the rate:"))
    t=int(input("Enter the time:"))

    si=(p*r*t)/100

    print("simple interest=",si)


print("in calling block")
calc_si_1()
print("back in calling block")
