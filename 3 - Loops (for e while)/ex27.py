#**Problema 27:** Use um loop `while` para pedir a senha ao usuário até que ele digite a senha correta ("1234").
while True:
    senha = input("Digite uma senha: ")
    if senha == "1234":
        print("Senha correta!")
        break
    else:
        print("Senha Incorreta! Tente novamente")