print(f"{' RADAR ELETRÔNICO ':=^42}")
velocidade_carro =float(input("Qual a velocidade atual do carro?: "))
print("="*42)
if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 7 
    print("Você ultrapassou o limite de 80Km/h")
    print(f"você devera pagar a multa de R${multa:.2f}")
else:
    print("Tenha um bom dia! Dirija com segurança!")
print("="*42)
