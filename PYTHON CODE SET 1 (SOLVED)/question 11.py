s=input("Enter String:")
for word in s.split():
    print(word[0].upper()+word[1:-1]+word[-1].upper(),end=" ")
'''
Enter String:hello world
HellO WorlD
'''
    
