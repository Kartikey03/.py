#style 3
def calc_si_3():
    p=int(input("Enter the principle:"))
    r=int(input("Enter the rate:"))
    t=int(input("Enter the time:"))

    si=(p*r*t)/100
    return si

print("in calling block")
ans=calc_si_3()
print(ans)
