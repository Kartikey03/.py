'''
import pickle
def Add_Mobile():
    fobj=open("Mobile.dat","ab")
    Model=input("Enter Model:")
    Company=input("Enter Company:")
    Price = int(input("Price:"))
    rec=[Model,Company,Price]
    pickle.dump(rec,fobj)
    fobj.close()

def count_company(company):
    fobj=open("Mobile.dat","rb")
    num = 0
    try:
        while True:
            rec=pickle.load(fobj)
            if company==rec[1]:
                num = num + 1
    except:
        fobj.close()
    return num

Add_Mobile()



def start_s():
    fwb=open('quotes.txt','w')
    fwb.write('Sssfghdfghfghdfghhdsadssss')

    frb=open('story.txt','r')
    fr = frb.readlines()
    print(fr)
    c=0

    for i in fr:
        if i[0]== 'S':
            c+=1
    print(c)
    fwb.close()
    frb.close()

start_s()



def word_by_word():
    fr=open("story.txt","r")
    for l in fr:
        w=l.split() 
        for wd in w:
            print(wd)
        print()
    fr.close()
word_by_word()


fr=open("story.txt","r")
s=fr.read()
l=s.split()
count_is=0
count_do=0
for w in l:
    if w=='is':
        count_is+=1
    if w=='do':
        count_do+=1
print("count of the word is=",count_is)
print("count of the word do=",count_do)
fr.close()
'''

'''
fr=open("story.txt","r")
s=fr.read()
l=s.split()
for w in l:
    print(w[::-1])
fr.close()
'''


fr=open("story.txt","r")
s=fr.read()

print(s)
fr.close()