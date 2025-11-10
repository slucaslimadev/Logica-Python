#Peça duas notas e verifique se o aluno foi aprovado (média >= 7.0).
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
media = (n1 + n2)/2
if media >= 7:
    print(f"Aluno aprovado com a média: {media}")
else:
    print(f"Aluno reprovado com a média: {media}")