print(f"{' PAR OU ÍMPAR ':=^42}")
numero = int(input("Me diga um número qualquer: "))
print("="*42)
if numero % 2 == 0:
    print(f"O número {numero} e um núemro PAR")
else:
    print(f"O número {numero} e um número ÍMPAR")
print("="*42)
