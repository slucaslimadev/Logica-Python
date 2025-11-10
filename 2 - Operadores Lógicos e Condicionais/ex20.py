#**Problema 20:** Se formarem um triângulo (exercício 19), diga se é Equilátero, Isósceles ou Escaleno.
lado1= float(input("Digite o 1 lado: "))
lado2= float(input("Digite o 2 lado: "))
lado3= float(input("Digite o 3 lado: "))
if (lado1+lado2 > lado3) and (lado2 +lado3 > lado1) and (lado3 + lado1 > lado2):
    print("Sim, esses lados formam um triângulo!")
    #Equilátero
    if (lado1 == lado2 == lado3):
        print("É um triângulo equilátero")
    #Isósceles
    elif (lado1 == lado2) or (lado2 == lado3) or (lado3 == lado1):
        print("É um triângulo isóceles")
    #Escaleno
    else:
        print("É um escaleno")

else:
    print("Não, esses lados NÃO formam um triângulo.")