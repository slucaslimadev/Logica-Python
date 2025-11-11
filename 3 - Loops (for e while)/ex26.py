#**Problema 26:** Peça um número e calcule seu fatorial (ex: 5! = 5*4*3*2*1).
fatorial = 1
n = int(input("Digite um número: "))
for i in range(1, n + 1):
    fatorial = fatorial * i
print(f"o fatorial do número: {n} é {fatorial}")