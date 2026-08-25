print(f"{' CONVERSOR DE BASES NUMÉRICAS ':=^42}")
numero = int(input("Digite um número inteiro: "))
print("="*42)
print('''Escolha uma das bases para a conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
print("="*42)
opçao = int(input("Sua opção: "))
print("="*42)
if opçao == 1:
    binario = bin(numero)
    print(f"{numero} convertido para HEXADECIMAL é igual a {binario[2:]}")
elif opçao == 2:
    octal = oct(numero)
    print(f"{numero} convertido para OCTAL é igual a {octal[2:]}")
elif opçao == 3:
    hexadecimal = hex(numero)
    print(f"{numero} convertido para HEXADECIMAL é igual a {hexadecimal[2:]}")
print("="*42)
