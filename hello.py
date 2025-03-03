
def s(integer, decimal):
    while(integer>0):
        d1=integer%10
        sum1 = 0
        sum1 = sum1+d1
        integer = integer/10

    while(decimal>0):
        d2 = decimal%10
        sum2 = 0
        sum2 = sum2+d2
        decimal = decimal/10
    if sum1 == sum2:
        print("true")
    else:
        print("false")

string = "45.2232"
l = string.split(".")
print(int(l[0]))
l2= [int(l[0]), int(l[1])]
print(l2)


integer = l2[0]
decimal = l2[1]
s(integer, decimal)