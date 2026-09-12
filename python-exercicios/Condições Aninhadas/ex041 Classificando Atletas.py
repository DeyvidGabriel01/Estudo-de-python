from datetime import date
print(f"{" CLASSIFICANDO ATLETAS ":=^38}")
ano = int(input("Digite o ano de nascimento: "))
print("="*38)
ano_atual = date.today().year
idade = ano_atual - ano
print(f"O atleta tem {idade} anos.")
if idade <= 9:
    classe = "MIRIM"
elif idade<= 14:
    classe = "INFANTIL"
elif idade <= 19:
    classe = "JUNIOR"
elif idade <= 25:
    classe = "SÊNIOR"
else:
    classe = "MASTAR"
print("="*38)
print(f"Classificação: {classe}")
print("="*38)
