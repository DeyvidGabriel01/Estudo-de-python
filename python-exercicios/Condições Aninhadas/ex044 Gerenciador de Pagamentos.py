print(f"{' GERANCIADOR DE PAGAMENTOS ':=^42}")
produto = float(input("Digite o valor da sua compra: R$"))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2X no cartão
[ 4 ] 3X ou mais no cartão''')
print("="*42)
opção = int(input("Qual a sua opção: "))
print("="*42)
if opção == 1:
    desconto = produto - (produto * 10/100)
    print(f"Sua compra de R${produto:.2f} com o desconto de 10% vai custar R${desconto:.2f} no final.")
elif opção == 2:
    print(f"Sua compra custara R${produto:.2f} no final.")
elif opção == 3:
    desconto = produto - (produto * 5/100)
    print(f"Sua compra de R${produto:.2f} com o desconto de 5% vai custa R${desconto:.2f} no final.")
elif opção == 4:
    numeros_parcelas = int(input("Digite o número de parcelas: "))
    juros = produto + (produto * 20/100)
    parcelas = juros / numeros_parcelas
    print(f"Sua compra será parcelada em {numeros_parcelas}X de R${parcelas:.2f} COM JUROS")
    print(f"Sua compra de R${produto:.2f} vai custar R${juros:.2f} no final.")
print("="*42)
