from datetime import datetime
#**Problema 9:** Peça o ano de nascimento e calcule a idade do usuário.
print("--- **Problema 9:** Peça o ano de nascimento e calcule a idade do usuário. ---")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(datetime.now().year)
idade = ano_atual - ano_nascimento
print(f"Ano de nascimento: {ano_nascimento}\nAno Atual: {ano_atual}\nIdade: {idade} anos")