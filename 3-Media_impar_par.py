'''''
3 - Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes.
Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos,
Solicitou que você criasse um sistema capaz de atender ao seguinte requisito:
    O  professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e
    depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50).
O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.
Há ainda um pedido especial do mantenedor:
    Para que os professores não se confundam, ao digitar cada uma das notas, deve ser exibida uma mensagem no seguinte padrão:
         VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).
         POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.

'''

print("Prova da turma grande: cálculo de médias ímpares e pares")

# Inicializa as variáveis de soma das notas dos alunos ímpares e pares
soma_impares = 0
soma_pares = 0

# Loop para digitar as notas dos alunos ímpares
for x in range(1, 50, 2):
    nota_alunos_impares = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    soma_impares += nota_alunos_impares

# Loop para digitar as notas dos alunos pares
for x in range(2, 51, 2):
    nota_alunos_pares = float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES.\nPOR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(x)))
    soma_pares += nota_alunos_pares

# Calcula a média das notas dos alunos ímpares e pares
media_impares = soma_impares / 25
media_pares = soma_pares / 25

# Imprime as médias na tela
print("Média das notas dos alunos ímpares: {:.2f}".format(media_impares))
print("Média das notas dos alunos pares: {:.2f}".format(media_pares))

# Verifica qual metade da turma teve a maior média
if media_impares > media_pares:
    print("A metade ÍMPAR da turma teve a maior média.")
elif media_pares > media_impares:
    print("A metade PAR da turma teve a maior média.")
else:
    print("As duas metades da turma tiveram a mesma média.")
