#**Problema 15:** Peça três números e diga qual deles é o maior.
n1 = int(input("Digite o numero 1: "))
n2 = int(input("Digite o numero 2: "))
n3 = int(input("Digite o numero 3: "))

if (n1 > n2) and (n1 > n3):
    print("Número 1 é maior")
if (n2 > n1) and (n2 > n3):
    print("Número 2 é maior")
if (n3 > n1) and (n3 > n2):
    print("Número 3 é maior")