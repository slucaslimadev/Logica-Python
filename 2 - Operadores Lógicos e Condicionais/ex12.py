#**Problema 12:** Verifique se um número é positivo, negativo ou zero.
n = int(input("Digite um número: "))
if n > 0:
    print(f"Número: {n} é positivo")
if n == 0:
    print(f"Número: {n} é zero")
elif n < 0:
    print(f"Número: {n} é negativo")