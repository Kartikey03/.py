student={}
n=int(input("Enter number of key value pairs:"))
for i in range(n):
    st_name=input("Enter name of student")
    st_percent=int(input("Enter percentage:"))
    student[st_name]=st_percent
print("Dictionary before deletion",student)

a=input("Enter name you want to delete")

student.pop(a)

print(student)
