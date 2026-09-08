from datetime import date
print(f"{' ALISTAMENTO MILITA ':=^42}")
dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))
data_atual = date.today()
data_nascimento = date(ano, mes, dia)
idade = data_atual.year - data_nascimento.year
print("="*42)
print(f"A sua data de nascimento e {dia:02}/{mes:02}/{ano} \nVocê tem {idade} anos de idade em {data_atual.day:02}/{data_atual.month:02}/{data_atual.year}.")
print("="*42)
if idade > 18:
    anos_alistados = idade - 18
    print(f"Você já deveria ter se alistado há {anos_alistados} anos. \nSeu alistamento foi em {data_atual.year - anos_alistados}")
    print("""Você ja fez o seu alistamento? 
[1] SIM
[2] NÃO """)
    opcao = int(input("Digite a sua opção: "))
    if opcao == 1:
        print("PARABÉNS por ja ter feito o alistamento")
    elif opcao == 2:
        print("Você ainda não fez o alistamento faça IMEDIATAMENTE.")
    else:
        print("Essa opção NÃO EXISTE!")
elif idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE")
else:
    anos_faltam = 18 - idade
    print(f"Ainda faltam {anos_faltam} para o alistamento. \nSeu alistamento será em {data_atual.year + anos_faltam}.")
print("="*42)
