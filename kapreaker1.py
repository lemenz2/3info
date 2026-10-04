K=int(input("Donner un entier entre 1 et 999: "))
while 1>K and K>999:
    K=int(input("Donner un entier entre 1 et 999: "))
if 1<=K<=9:
    S=(K//10)+(K%10)
elif 10<=K<=99:
    S=(K//100)+(K%100)
else:
    S=(K//100)+(K%1000)
if S==K:
    print("Le nombre est KAPREAKER")
else:
    print("Le nombre n'est pas KAPREAKER")
