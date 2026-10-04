K=int(input("Donner un entier entre 1 et 999: "))
while 1>K and K>999:
    K=int(input("Donner un entier entre 1 et 999: "))
n=len(str(K))
c=K*K
chc=str(c)
chd=chc[len(chc)-n:len(chc)]
chg=chc[0:len(chc)-n]
S=int(chg)+int(chd)
if S==K:
    print("Le nombre est KAPREAKER")
else:
    print("Le nombre n'est pas KAPREAKER")