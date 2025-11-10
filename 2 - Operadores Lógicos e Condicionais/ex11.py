#**Problema 11:** Verifique se um número é par ou ímpar.
print("--- **Problema 11:** Verifique se um número é par ou ímpar. ---")
numero = int(input("Digite um número: "))
verificar_numero = numero % 2
if verificar_numero == 0:
    print(f"Número {numero} é par")
else: 
    print(f"Número: {numero} é impar")