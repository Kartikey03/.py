def add_data():
    fw = open('story.txt','a')

    #send data to file
    s = 'Once upon a time there wsa a boy named Alex\nHe was very very naughty\n'
    fw.write(s) # used to send a string to the file
    fw.close()

def show_data():
    fr = open('story.txt','r')
    s=fr.read() # used to return all the data stored in the file in the form of string 
    print(s)
    fr.close()

def data_readlines():
    fr = open('story.txt','r')
    l = fr.readlines() 
    print(l,end='')
    #['Once upon a time there wsa a boy named Alex\n', 'He was very very naughty\n']
    fr.close()

#bakwaas method
def data_readline1(): 
    fr = open('story.txt','r')
    l = fr.readline() 
    print(l)
    l = fr.readline() 
    print(l)
    fr.close()

#with readline() in a loop
def data_readline2():
    fr = open('story.txt','r')
    s = ' '
    while s :
        if len(s) == 0:
            break
        l = fr.readline() 
        print(l, end='')
    fr.close()

#without readline()
def data_readline3():
    fr = open('story.txt','r')
    for l in fr:
        print(l, end='')
    fr.close()



#add_data()
#show_data()
#data_readlines()
#data_readline1()
#data_readline2()
data_readline3()

'''
Text Files:
write() - sends a string to the text file.
writelines() - sends a list used to store multiple lines in text files.

Binary files:
dump()

CSV Files:
write()
writerows()
'''