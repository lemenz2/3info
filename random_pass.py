from random import *
mp=""
l=4
n=2
while len(mp)!=6:
    c=chr(randint(48,122))
    while not ("0"<=c<="9" or "a"<=c<="z" or "A"<=c<="Z"):
        c=chr(randint(48,122))
    if mp.find(c)==(-1):
        if "0"<=c<="9" and n!=0:
            mp=mp+c
            n-=1
        elif "A"<=c.upper()<="Z" and l!=0:
            mp+=c
            l-=1
print(mp)