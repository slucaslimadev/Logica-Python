#**Problema 19:** Peça três lados de um triângulo e verifique se eles formam um triângulo.
lado1= float(input("Digite o 1 lado: "))
lado2= float(input("Digite o 2 lado: "))
lado3= float(input("Digite o 3 lado: "))
if (lado1+lado2 > lado3) and (lado2 +lado3 > lado1) and (lado3 + lado1 > lado2):
    print("Sim, esses lados formam um triângulo!")
else:
    print("Não, esses lados NÃO formam um triângulo.")
