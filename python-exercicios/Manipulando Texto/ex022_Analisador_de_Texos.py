nome = str(input("Digite seu nome completo: ")).strip()
maiuscula = nome.upper()
minuscula = nome.lower()
print("Analisando seu nome...")
print(f"Seu nome em maiúsculas é {maiuscula}")
print(f"Seu nome em minusculas é {minuscula}")
print(f"Seu nome tem ao todo {len(nome) - nome.count(" ")} letras")
print(F"Seu primeiro nome tem {nome.find(" ")} letras")

'''Outra solução'''
separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e ele tem {len(separa[0])}")
