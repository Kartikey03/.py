
n = int(input("Enter the Number of elements to be entered in the list : "))
L = []
for i in range(n):
    elem = int(input("Enter the Number :"))
    L.append(elem)
print("List Before converting :", L)

def oddtoeven(L):
    for i in range(len(L)):
        if L[i]%2 !=0:
            L[i] = L[i]*2
    return L

print("List After converting :", oddtoeven(L))


# Output
'''
Enter the Number of elements to be entered in the list : 10
Enter the Number :1
Enter the Number :2
Enter the Number :3
Enter the Number :4
Enter the Number :5
Enter the Number :6
Enter the Number :7
Enter the Number :8
Enter the Number :9
Enter the Number :10
List Before converting : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
List After converting : [2, 2, 6, 4, 10, 6, 14, 8, 18, 10]
'''





