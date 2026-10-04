T = ([""] * 100)
C = ([0] * 100)
N = int(input("Taper N: "))
while not (10 <= N <= 100):
    N = int(input("Taper N: "))
for i in range(N):                     
    num = input("Taper votre numero: ")
    while not (len(num) == 8 and num[0] == "6" and num[1] in ("5", "6")):
        num = input("Taper votre numero: ")
    T[i] = num

    C[i] = int(input("Taper votre montant: "))
c = 0
for i in range(N):
    c = c + C[i]
M = c / N
ch = "Les numeros gagnants: "
for i in range(N):
    if C[i] > M:
        ch = ch + T[i] + " - "
print("Le montant moyen des consommations est: ", M)
print(ch)