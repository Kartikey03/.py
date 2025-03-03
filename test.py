# for i in range(1, 6):
#   for j in range(i):
#     print("*", end="")
#   print()


# for i in range(1, 6):
#     print(' ' * (5 - i) + '*' * i)



# word="python language"
# l=word.split()
# print(l)
# for i in l:
#     print(i[::-1], end=" ")




# word = "hello python"
# words = word.split()
# new_words = [w[0].upper() + w[1:-1] + w[-1].upper() for w in words]
# print(new_words)
# new_word = ' '.join(new_words)
# print(new_word)

# l=[0,1,2,3]
# l[0]=6
# print(l)


# s="helo"
# s1='hello'
# s2="""
# dhfghsdlg'
# sdf
# sg
# sg
# s
# gh
# f
# gh
# fg
# h
# fgh
# f
# gh
# f
# gh"""
# s="hello"
# print(s2)




# s="My Name is Kartikey"
# print(s.istitle())
# l=s.split()
# print(l)
# l1=[]
# for i in l:
#     if i.istitle()==True:
#         l1.append(1)
#     else:
#         l1.append(0)

# if l1.count(1) == len(l):
#     print("True")
# else:
#     print("False")











# str=input("Enter string:")
# str1=""
# for i in str:
#  if i.isspace():
#     str1+="#"
#  else:
#     str1+=i
# print('output is',str1)



# l=["hello", "world"]
# print(l)
# # print(l[4])

# s="hello world"
# s1 = ' '.join(l)
# print(s1)

# print(s.index('o'))
# print(s[2:8:2])

#[start : stop : step]




# i=int(input("enter the number"))
# if i%2==0:
#     print("even")
# else:
#     print("odd")




# s={1,2,3,4}
# for i in s:
#     print(i)



# s='abcd'
# l=[1,2,3]
# r=list(zip(s,l))
# print(r)



# s="123"
# print(sum(int(i) for i in s))


# def sum_digits_in_list(lst):
#     return [sum(int(digit) for digit in str(num)) for num in lst]

# numbers = [12, 43]
# result = sum_digits_in_list(numbers)
# print(result)  # Output: [3, 7]


# s="123"
# for i in s:
#     print(i+2)


# for i in range(1,6):
#     for j in range(i):
#         print(' '*(6-j)+str(j))
# print()


# s='pythonnnnnnnnnn'
# l=list(s)
# print(l)

def count_substring(string, substring):
    count = 0
    sub_len = len(substring)
    for i in range(len(string) - sub_len + 1):
        if string[i:i+sub_len] == substring:
            count += 1
    return count

# Input
original_string = input().strip()
substring = input().strip()

# Output
result = count_substring(original_string, substring)
print(result)
