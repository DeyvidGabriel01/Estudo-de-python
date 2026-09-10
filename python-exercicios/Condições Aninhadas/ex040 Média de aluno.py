print(f"{' MÉDIA DOS ALUNOS ':=^42}")
primeira_nota = float(input("\033[36mDigite a primeira nota:\033[m "))
segunda_nota = float(input("\033[36mDigite a segunda nota:\033[m "))
terceira_nota = float(input("\033[36mDigite a terceira nota:\033[m "))
quarta_nota = float(input("\033[36mDigite a quarta nota:\033[m "))
print("="*42)
media_final = (primeira_nota + segunda_nota + terceira_nota + quarta_nota) / 4
print(F"Sua média final é {media_final:.1F}")
if media_final < 5.0:
    print("\033[31mO aluno está REPROVADO.\033[m")
elif 7 > media_final >= 5:
    print("\033[33mO aluno está de RECUPERAÇÃO.\033[m")
else:
    print("\033[32mO aluno está APROVADO.\033[m")
print("="*42)
