def count_substring(string, sub_string):
    c=0
    print(sub_string[0], string[0], len(string), len(sub_string))
    for i in range(0,len(string)):
        
        if sub_string[i]==string[i]:
            c+=1
    return c
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

