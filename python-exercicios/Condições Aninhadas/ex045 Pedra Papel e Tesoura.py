from random import randint
from time import sleep
print(f"{' PEDRA PAPEL TESOURA ':=^38}")
print("""Sua opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
print("="*38)
jogador = int(input("Digite a sua opção: "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("="*38)
computador = randint(0, 2)
if jogador != computador:
    if jogador == 0 and computador == 1:
        print("Computador jogou papel \nJogador jogou Pedra")
        print("VOCÊ PERDEU")
    elif jogador == 0 and computador == 2:
        print("Compudador jogou Tesoura \nJogador jogou Pedra")
        print("VOCÊ VENCEU")
elif jogador == 0 == computador:
    print("Computador jogou Pedra \nJogador jogou Pedra")
    print("EMPATE")
if jogador != computador:
    if jogador == 1 and computador == 2:
        print("Computador jogou Papel \nJogador jogou Tesoura")
        print("VOCÊ VENCEU")
    elif jogador == 1 and computador == 0:
        print("Computador jogou Papel \nJogador jogou Pedra")
        print("VOCÊ PERDEU")
elif jogador == 1 == computador:
    print("Computador jogou Papel \nJogador jogou Papel")
    print("EMPATE")
if jogador != computador:
    if jogador == 2 and computador == 1:
        print("Computador jogou Tesoura \nJogador jogou Papel")
        print("VOCê PERDEU")
    elif jogador == 2 and computador == 0:
        print("Computador jogau Tesoura \nJogador jogou Pedra")
elif jogador == 2 == computador:
    print("Computador jogou Tesoura \nJogador jogou Tesoura")
print("="*38)

# outra solução

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA''')
jogador = int(input("Qual sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
print("-="*11)
print(f"Computado jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-="*11)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print("IMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUATADOR VENCE")
    else:
        print("JOGADA INVALIDA!")   

elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("JOGADA INVALIDA!")

elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("JOGADA INVALIDA!")
