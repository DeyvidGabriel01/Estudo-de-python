print(f"{' CALCULADORA DE IMC ':=^38}")
peso = int(input("Digite o seu peso: (Kg) "))
altura = float(input("Digite a sua altura: (m) "))
print("="*38)
imc = peso / (altura*altura)
print(f"O seu IMC é de {imc:.1f}")
print("="*38)
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
