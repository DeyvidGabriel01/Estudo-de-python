print(f"{' COMPARANDO NÚMEROS ':=^42}")
primeiro_valor = int(input("Digite o primeiro valor: "))
segundo_valor = int(input("Digite o segundo valor: "))
print("="*42)
if primeiro_valor > segundo_valor:
    print("O PRIMEIRO valor é o maior valor")
elif segundo_valor > primeiro_valor:
    print("O SEGUNDO valor é o maior valor")
else:
    print("so dois valores são IGUAIS")
print("="*42)
