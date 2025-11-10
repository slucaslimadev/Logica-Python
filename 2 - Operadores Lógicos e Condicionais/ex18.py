#**Problema 18:** Simule um login. Peça usuário e senha. Se for "admin" e "1234", dê "Acesso concedido", senão "Acesso negado".
print("--- LOGIN ---")
usuario = str(input("Digite o usuario: "))
senha = str(input("Digite a senha: "))
if usuario == "admin" and senha == "1234":
    print("Acesso concedido")
else:
    print("Acesso negado!")