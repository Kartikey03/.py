# QUESTION  10
# UDF that receives a character C and an integer N as Parameters. The Function Should repeat C, N times.
# If no Value is Passed for Both the Parameters, the function should repeat the Character '*', 50 times.

def l_char(c = '*', n = 50):
    print(str(c) * int(n))
print('# l_char()')
l_char()

print('# l_char("@", 80)')
l_char('@', 80)

print('# l_char("#")')
l_char("#")

print('# l_char(4, 40)')
l_char(4, 40)


#Output
'''
# l_char()
**************************************************

# l_char('@', 80)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@

# l_char("#")
##################################################

# l_char(4, 40)
4444444444444444444444444444444444444444
'''
