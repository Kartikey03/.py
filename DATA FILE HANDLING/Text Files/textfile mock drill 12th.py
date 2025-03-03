import os
def create_txtfile():
    if os.path.isfile("hardwork.txt"):
        def count_vowels():
            fobj=open("hardwork.txt", "r")
            fr=fobj.read()
            c=0
            for i in fr:
                if i.isalpha():
                    if i in "aeiouAEIOU":
                        c+=1
            print("The Number of upper case and lowercase letters are :", c)
            fobj.close()

        def count_is():
            fobj=open("hardwork.txt", "r")
            fr = fobj.read()
            c=0
            s=fr.split()
            for i in s:
                if i == "is":
                    c+=1
            print("The count of word 'is' is :", c)
            fobj.close()

        def show_four():
            fobj = open("hardwork.txt", "r")
            fr= fobj.read()
            c=[]
            s=fr.split()
            for i in s:
                if len(i) == 4:
                    c.append(i)
                    
            print("here is the list of all four letter words")
            for f in c:
                print(f)

            fobj.close()

        def show_tT():
            fobj=open("hardwork.txt", "r")
            fr=fobj.read()
            s=fr.split()
            c=[]

            for i in s:
                if i.isalpha():
                    if i[-1] in "tT":
                        c.append(i)
            print("words that end with letter t/T are :")
            for f in c:
                print(f)
                
            fobj.close()

        def show_aA():
            fobj=open("hardwork.txt","r")
            fr=fobj.read()
            s=fr.split()
            c=[]

            for i in s:
                if i.isalpha():
                    if i[0] in "aA":
                        c.append(i)
            print("words that begin with letter a/A are :")
            for f in c:
                print(f)

                fobj.close()

        def show_aAcount():
            fobj = open("hardwork.txt", "r")
            fr=fobj.readlines()
            c1=[]
            c2=0
            for i in fr:
                if i[0] in "aA":
                    c1.append(i)
                    c2+=1
            print("the count of lines that begin with a/A is :", c2)
            print("the lines that begin with a/A is :")
            for f in c1:
                print(f)

            fobj.close()
            
        while True:
            print("""

        -----MENU-----
        1. count no. of vowels
        2. count of word 'is'
        3. display the 4 letter words
        4. display the words that end with letter t/T
        5. display the words that begin with letter a/A
        6. display the lines and count that begin with letter a/A
        7. Exit Menu
        """)
            ch = int(input("Enter your choice :"))
            
            if ch == 1:
                count_vowels()

            elif ch ==2:
                count_is()

            elif ch == 3:
                show_four()

            elif ch == 4:
                show_tT()

            elif ch == 5:
                show_aA()

            elif ch == 6:
                show_aAcount()

            elif ch == 7:
                print("Thank You")
                break

            else:
                print("invalid input !!")
                break
    else:
        fobj=open("hardwork.txt", "a")
        fw=fobj.write("This is important to note that success is the result of hard work\nWe all are expected to do hard work\nAfter all experience comes from hard work\n")    
        fobj.close()

        def count_vowels():
            fobj=open("hardwork.txt", "r")
            fr=fobj.read()
            c=0
            for i in fr:
                if i.isalpha():
                    if i in "aeiouAEIOU":
                        c+=1
            print("The Number of upper case and lowercase letters are :", c)
            fobj.close()

        def count_is():
            fobj=open("hardwork.txt", "r")
            fr = fobj.read()
            c=0
            s=fr.split()
            for i in s:
                if i == "is":
                    c+=1
            print("The count of word 'is' is :", c)
            fobj.close()

        def show_four():
            fobj = open("hardwork.txt", "r")
            fr= fobj.read()
            c=[]
            s=fr.split()
            for i in s:
                if len(i) == 4:
                    c.append(i)
                    
            print("here is the list of all four letter words")
            for f in c:
                print(f)

            fobj.close()

        def show_tT():
            fobj=open("hardwork.txt", "r")
            fr=fobj.read()
            s=fr.split()
            c=[]

            for i in s:
                if i.isalpha():
                    if i[-1] in "tT":
                        c.append(i)
            print("words that end with letter t/T are :")
            for f in c:
                print(f)
                
            fobj.close()

        def show_aA():
            fobj=open("hardwork.txt","r")
            fr=fobj.read()
            s=fr.split()
            c=[]

            for i in s:
                if i.isalpha():
                    if i[0] in "aA":
                        c.append(i)
            print("words that begin with letter a/A are :")
            for f in c:
                print(f)

                fobj.close()

        def show_aAcount():
            fobj = open("hardwork.txt", "r")
            fr=fobj.readlines()
            c1=[]
            c2=0
            for i in fr:
                if i[0] in "aA":
                    c1.append(i)
                    c2+=1
            print("the count of lines that begin with a/A is :", c2)
            print("the lines that begin with a/A is :")
            for f in c1:
                print(f)

            fobj.close()
            
        while True:
            print("""

        -----MENU-----
        1. count no. of vowels
        2. count of word 'is'
        3. display the 4 letter words
        4. display the words that end with letter t/T
        5. display the words that begin with letter a/A
        6. display the lines and count that begin with letter a/A
        7. Exit Menu
        """)
            ch = int(input("Enter your choice :"))
            
            if ch == 1:
                count_vowels()

            elif ch ==2:
                count_is()

            elif ch == 3:
                show_four()

            elif ch == 4:
                show_tT()

            elif ch == 5:
                show_aA()

            elif ch == 6:
                show_aAcount()

            elif ch == 7:
                print("Thank You")
                break

            else:
                print("invalid input !!")
                break
create_txtfile()
        
