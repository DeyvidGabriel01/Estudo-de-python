print(f"{' MAIOR E MENOR ':=^42}")
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))
print("="*42)
if valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
# maior valor
    if valor1 > valor2 and valor1 > valor3:
        maior_valor = valor1
    if valor2 > valor1 and valor2 > valor3:
        maior_valor = valor2
    if valor3 > valor2 and valor3 > valor1:
        maior_valor = valor3
    print(f"O maior valor é {maior_valor}")

# menor valor
    if valor1 < valor2 and valor1 < valor3:
        menor_valor = valor1
    if valor2 < valor1 and valor2 < valor3:
        menor_valor = valor2
    if valor3 < valor1 and valor3 < valor2:
        menor_valor = valor3
    print(f"O menor valor é {menor_valor}")
else:
    print("NÃO EXISTE MENOR OU MAIOR VALOR OS TRÊS VALORES SÃO IGUAIS.")
print("="*42)
