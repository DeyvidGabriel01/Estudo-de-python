from random import randint
print(f"{' JOGO DE ADIVINHAÇÃO ':=^42}")
numero = int(input("Digite um número entre 0 e 5: "))
computador = randint(0,5)
print("="*42)
print(f"Você escolheu {numero} o computador escolheu {computador} ")
print("="*42)
if numero == computador:
    print("VOCÊ VENCEU PARABENS!")
else:
    print("VOCÊ PERDEU")
print("="*42)
