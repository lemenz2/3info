from random import randint
from numpy import array

db=0
s=0
i=0
r=0
ch=array([""]*2)
win=False
while not win:
    d1=randint(1,6)
    d2=randint(1,6)
    r+=1
    if d1==d2:
        db+=1
        
        ch[db-1]=str(d1)+","
    else:
        db=0
    s+=d1+d2
    print("you rolled", d1,"and",d2,", total is", s)
    if db==2 or s>=50:
        win=True
        win==False
if db==2 or s>=50:
    if db==2:
        print("you won with 2 doubles of: ", ch[0], "then", ch[1])
    elif s>=50:
        print("you won by reaching score 50")
else:
    print("you lose")