#**Problema 28:** Peça 5 números ao usuário e, ao final, mostre a soma e a média deles.
#n1 = int(input("Digite o número 1: "))
#n2 = int(input("Digite o número 2: "))
#n3 = int(input("Digite o número 3: "))
#n4 = int(input("Digite o número 4: "))
#n5 = int(input("Digite o número 5: "))
#soma = n1 + n2 + n3 + n4 + n5
#media = soma / 5
#print(f"Soma: {soma}, média: {media}")
contador = 1
acumulador = 0
while True:
    usuario = int(input(f"Digite {contador} número: "))
    acumulador = acumulador + usuario
    contador = contador + 1
    media = acumulador / 5
    if contador == 6:
        break
print(f"soma {acumulador}, média: {media}")

