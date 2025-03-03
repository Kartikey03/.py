def oddeven(regNo, day):
    chargeeven=0
    chargeodd=0
    for i in regNo:
        if i%2==0:
            chargeeven = chargeeven+300
        else:
            chargeodd = chargeodd+300
    if day%2==0:
        print(chargeodd)
    else:
        print(chargeeven)


regNo=[1,2,3,4,5,5,6]
day = int(input("Enter the day: "))
oddeven(regNo, day)

