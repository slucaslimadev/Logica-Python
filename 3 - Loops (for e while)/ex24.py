#**Problema 24:** Peça um número e imprima a tabuada dele (de 1 a 10).
print("--- TABUADA ---")
n = int(input("Digite o número para tabuada: "))
print(f"Tabuada do número {n}")
for multiplicador in range(1, 11):
    resultado = multiplicador * n
    print(f"{n} x {multiplicador} = {resultado}\n")