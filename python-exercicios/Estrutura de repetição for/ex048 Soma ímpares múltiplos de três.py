print(f"{' SOMA DE ÍMPARES ':=^38}")
contador = 0
soma = 0
for numero in range(1, 501):
    if numero % 3 == 0 and numero % 2 == 1:
        soma += numero
        contador += 1
print(f"Soma de todos os {contador} valores solicitados é {soma}")
print("="*38)
