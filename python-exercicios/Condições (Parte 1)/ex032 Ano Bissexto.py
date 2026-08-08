from datetime import date
print(f"{' ANO BISSEXTO ':=^42}")
ano = int(input("Digite um ano para a anlisar? Digite 0 para analisar o ano atual: "))
print("="*42)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(F"O ano {ano} e um ANO BISSEXTO")
else:
    print(F"O ano {ano} não e um ANO BISSEXTO")
print("="*42)
