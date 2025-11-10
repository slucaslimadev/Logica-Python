#**Problema 17:** Calcule o IMC (Peso / Altura²) e classifique: Abaixo do peso, Peso normal, Sobrepeso.
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / altura ** 2
if imc < 18.5:
    print(f"IMC: {imc}\nAbaixo do peso")
elif imc < 24.9:
    print(f"IMC: {imc}\nPeso normal")
elif imc <= 29.9:
    print(f"IMC: {imc}\nSobrepeso")
else:
    print(f"IMC: {imc}\nObesidade")
