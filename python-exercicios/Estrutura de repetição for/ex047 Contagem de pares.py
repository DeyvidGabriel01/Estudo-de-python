print(f"{' CONTAGEM DE PARES ':=^38}")
for contador in range(1,51):
    if contador % 2 == 0:
        print(contador, end=" ")
print("Acabou")
print("="*38)

# outra solução
for contador in range(2, 51, 2):
    print(contador, end=" ")
