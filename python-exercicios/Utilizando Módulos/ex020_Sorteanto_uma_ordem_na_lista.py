import random
primeiro_aluno = str(input("Primeiro aluno: "))
segundo_aluno = str(input("Segundo aluno: "))
Terceiro_aluno = str(input("Terceiro aluno: "))
querto_aluno = str(input("Quarto aluno: "))
lista = [primeiro_aluno, segundo_aluno, Terceiro_aluno, querto_aluno]
random.shuffle(lista)
print(f"A ordem de apresentação será\n{lista}")
