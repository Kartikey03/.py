#Q1
# m=input() #hello
# n=input() #world

# l=[]
# for i in m:
#     for j in n:
#         if i!=j:
#             l.append(i)        
# print(l)


#Q2
# def are_anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)

# print(are_anagrams("listen", "silent"))  # Output: True
# print(are_anagrams("hello", "world"))  # Output: False


#Q3
def are_rotations(str1, str2):
    return str2 in str1 + str1

print(are_rotations("abcde", "deabc"))  # Output: True
print(are_rotations("abcde", "edcba"))  # Output: False