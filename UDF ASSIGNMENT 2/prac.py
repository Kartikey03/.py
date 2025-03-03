def fibbo(f, s, n):
    print(f, s)
    i = 1
    while i <= 8:
        n = f + s
        f = s
        s = n
        i += 1
f=int(input('entr'))
s=int(input('enhjk'))
n=f+s
print(fibbo(f,s,n,))
