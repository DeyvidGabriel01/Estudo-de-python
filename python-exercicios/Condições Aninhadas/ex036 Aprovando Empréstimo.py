print(f"{' APROVANDO EMPRÉSTIMO ':=^42}")
valor_casa = float(input("quanto e o valor da casa?: R$"))
salario = float(input("quanto e o seu salaro?: R$"))
ano = int(input("Em quantos anos quer pagar?: "))
print("="*42)
prestação = valor_casa / (ano * 12)
if prestação >= (salario *(30/100)):
    print(f"Para pagar uma casa de R${valor_casa:,.2f} em {ano} anos a prestação será de R${prestação:.2f}")
    print("Empréstimo NEGADO.")
else:
    print(f"Para pagar uma casa de R${valor_casa:,.2f} em {ano} anos a prestação será de R$ {prestação:.2F}")
    print("Empréstimo pode ser CONCEDIDO.")
print("="*42)
