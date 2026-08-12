print(f"{' AUMENTOS MÚLTIPLOS ':=^42}")
salario = float(input("Qual é o salário do funcionário?: R$"))
print("="*42)
if salario >= 1250:
    salario_novo = salario + (salario * (10/100))
else:
    salario_novo = salario + (salario * (15/100))
print(f"quem ganhava R${salario:.2f} passa a ganhar R${salario_novo:.2f} agora.")
print("="*42)
