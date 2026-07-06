from random import choice
primeiro_aluno = str(input("Primeiro aluno: "))
segundo_aluno = str(input("Segundo aluno: "))
terceiro_aluno = str(input("Terceiro aluno: "))
quanto_aluno = str(input("Quarto aluno: "))
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quanto_aluno]
aluno_escolido = choice(lista)
print(f"O aluno escolhido foi {aluno_escolido}")
