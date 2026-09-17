print(f"{' CALCULADORA DE IMC ':=^38}")
peso = int(input("Digite o seu peso: (Kg) "))
altura = float(input("Digite a sua altura: (m) "))
print("="*38)
imc = peso / (altura*altura)
print(f"O seu IMC é de {imc:.1f}")
print("="*38)

# metodo 1
if imc <= 18.5:
    print("Você ABAIXO DO PESO normal")
elif imc <= 25:
    print("PARABÉNS, você está na faixa de PESO NORMAL")
elif imc <= 30:
    print("Você está na faixa de SOBREPESO!")
elif imc <= 40:
    print("Você está em OBESIDADE!")
else:
    print("Você está em OBESIDADE MÓRBIDA, cuidade!")
print("="*38)

# medoto 2
if imc < 18:
    print("Você está ABAIXO DO PESO normal")
elif 18 <= imc < 25:
    print("BARABÉNS, você está na faixa de PESO NORMAL")
elif 25 <= imc < 30: 
    print("Você está em SOBREPESO")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE, cuidado!")
elif imc >= 40:
    print("Você está em OBESIDADE MÓRBIDA, cuidado!")
print("="*38)
