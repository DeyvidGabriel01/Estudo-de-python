nome = str(input("Digite seu nome completo: ")).strip()
nome_separado = nome.split()
ultimo_nome = nome_separado[-1]
primeiro_nome = nome_separado[0]
print("Muito Prazer em te conhecer!")
print(f"Seu primeiro nome é {primeiro_nome}")
print(f"Seu último nome é {ultimo_nome}")
