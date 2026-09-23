print(f"{' SOMA DE ÍMPARES ':=^38}")
contador = 0
soma = 0
for numero in range(1, 501):
    if numero % 3 == 0 and numero % 2 == 1:
        soma += numero
        contador += 1
print(f"Soma de todos os {contador} valores solicitados é {soma}")
print("="*38)

# outra solução 
soma = 0 
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f"A soma de todos os {cont} valores solicitados é {soma}")
