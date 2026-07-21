frase = str(input("Digite uma frase: ")).upper().strip()
letras_A = frase.count("A")
primeiro_A = frase.find("A") + 1
ultimo_A = frase.rfind("A") + 1
print(f"A letra A aparece {letras_A} vezes na frase.")
print(f"A primeira letra A apareceu na posição {primeiro_A}")
print(f"A última letra A apareceu na posição {ultimo_A}")
