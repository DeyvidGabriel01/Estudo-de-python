print(f"{' ANALISANDO TRIÂNGULO ':=^42}")
primeira = float(input("Primeira reta: "))
segunda = float(input("Segunda reta: "))
terceira = float(input("Terceira reta: "))
print("="*42)
if primeira < segunda + terceira and segunda < primeira + terceira and terceira < primeira + segunda:
    print("Os segmentos acima PODEM FORMA triângulo!")
else:
    print("Os segmentos acima NÃO PODEM FORMA triângulo")
print("="*42)
