print(f"{' CUSTO DE VIAGEM ':=^42}")
viagem = float(input("Qual a distancia da viagem: "))
print("="*42)
print(f"Você está prestes a começar uma viagem de {viagem:.1f}Km.")
print("="*42)
if viagem <= 200:
    valor_viagem = viagem * 0.50
    print(f"E o preço da sua passagem será de R${valor_viagem:.2f}")
else:
    valor_viagem2 = viagem * 0.45
    print(f"E o preço da sua passagem na promoção será de R${valor_viagem2:.2f}")
print("="*42)
