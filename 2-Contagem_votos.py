'''''
2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives.
Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana
(segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram,
verifique e exiba qual dia foi o escolhido.
'''

print("Contagem de votos para saber qual foi o melhor dia da live")

# Solicita a quantidade de votos para cada dia da semana e armazena os valores como inteiros
voto_segunda = int(input("Quantidade de votos para a segunda-feira: "))
voto_terca = int(input("Quantidade de votos para a terça-feira: "))
voto_quarta = int(input("Quantidade de votos para a quarta-feira: "))
voto_quinta = int(input("Quantidade de votos para a quinta-feira: "))
voto_sexta = int(input("Quantidade de votos para a sexta-feira: "))


# Verifica se houve empate entre todos os dias, caso afirmativo, imprime mensagem informando o empate
if voto_segunda == voto_terca == voto_quarta == voto_quinta == voto_sexta:
    print("Houve um empate entre todos os dias!")
else:
    # Verifica qual foi o dia com mais votos e imprime mensagem informando o dia vencedor
    if voto_segunda > voto_terca and voto_segunda > voto_quarta and voto_segunda > voto_quinta and voto_segunda > voto_sexta:
        print("O dia mais votato foi SEGUNDA com {} votos".format(voto_segunda))
    elif voto_terca > voto_segunda and voto_terca > voto_quarta and voto_terca > voto_quinta and voto_terca > voto_sexta:
        print("O dia mais votato foi TERCA com {} votos".format(voto_terca))
    elif voto_quarta > voto_segunda and voto_quarta > voto_terca and voto_quarta > voto_quinta and voto_quarta > voto_sexta:
        print("O dia mais votato foi QUARTA com {} votos".format(voto_quarta))
    elif voto_quinta > voto_segunda and voto_quinta > voto_terca and voto_quinta > voto_quarta and voto_quinta > voto_sexta:
        print("O dia mais votato foi QUINTA com {} votos".format(voto_quinta))
    elif voto_sexta > voto_segunda and voto_sexta > voto_terca and voto_sexta > voto_quarta and voto_sexta > voto_quinta:
        print("O dia mais votato foi SEXTA com {} votos".format(voto_sexta))
    else:
        # Caso haja empate entre dois ou mais dias, valores inválidos, imprime mensagem de erro
        print("Votos não computados ou um possiviel empate entre dias")



