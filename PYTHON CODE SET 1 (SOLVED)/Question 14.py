s=" hi hi is am am is the is is am"
dict_1={}
word=s.split()
for element in word:
    print(element,s.count(element))
    dict_1[element]=s.count(element)
print(dict_1)

ind=sorted(dict_1.values(),reverse=True)
print(ind)
second=ind[1]
for i in dict_1:
    if dict_1[i]==second:
        print(i,"is the second most repeated element in string")

