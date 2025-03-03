t=()
n=int(input("Enter first Tuple Size:"))
for i in range(n):
    val=int(input("Enter Value:"))
    t+=(val,)
print(t)

t1=()
n1=int(input("Enter second Tuple Size:"))
for i in range(n):
    val=int(input("Enter Value:"))
    t1+=(val,)
print(t1)

sumt=t+t1
print("Addition of tuple is:",sumt)
for i in sumt:
      print(i)

print("Maximun value is:",max(sumt))
print("Minimun value is:",min(sumt))

'''
Enter first Tuple Size:5
Enter Value:76
Enter Value:87
Enter Value:98
Enter Value:99
Enter Value:43
(76, 87, 98, 99, 43)
Enter second Tuple Size:4
Enter Value:12
Enter Value:11
Enter Value:45
Enter Value:65
Enter Value:45
(12, 11, 45, 65, 45)
Addition of tuple is: (76, 87, 98, 99, 43, 12, 11, 45, 65, 45)
76
87
98
99
43
12
11
45
65
45
Maximun value is: 99
Minimun value is: 11
'''
