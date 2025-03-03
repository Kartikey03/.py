#script to copy words that begin with vowels from multiple2.txt to another text file vowel.txt
def copy_word():
    fr=open("multiple2.txt",'r') #source file
    fw=open("vowel.txt","w")     #destination file

    s=fr.read()
    word=s.split()

    for w in word:
        if w[0] in 'aeiouAEIOU':
            fw.write(w + '\n')

    fr.close()
    fw.close()


def show(s):
    fr=open(s)
    s=fr.read()
    print(s)
    fr.close()


copy_word()
show("multiple2.txt")
show("vowel.txt")

    
