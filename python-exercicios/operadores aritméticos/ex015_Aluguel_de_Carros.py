dias = int(input("Quantos dias alugados? "))
quilometros = int(input("Quantos Km rodados? "))
valor_dias = dias * 60
valor_quilometros = quilometros * 0.15
total = valor_quilometros + valor_dias
print(f"O total a pagar é de R${total:.2f}")
