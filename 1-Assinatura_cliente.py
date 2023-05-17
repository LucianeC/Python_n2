'''''
1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria:
    um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade.
    O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.
Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente,
    o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês.
A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:
Basic -30%
Silver -20%
Gold -10%
Platinum -5%
'''

print("Algoritmo que receba o tipo de assinatura do cliente o e faturamento anual")

#Declara variaveis com valores iniciais vazios
assinatura = ""
bonus = 0


#Loop para solicitar o tipo de assinatura
while assinatura != ("BASIC" "SILVER" "GOLD" "PLATINUM") :

    #Recebe o tipo de assinatura do cliente e o faturamento anual
    assinatura = input("Informe qual tipo da sua assinatura 'Basic', 'Silver', 'Gold' ou 'Platinum': ")
    faturamento_anual = float (input("Informe o valor do futuramento: "))

    #Calcula a porcentagem de acordo com o tipo de assinatura
    if assinatura.upper() == "BASIC":
        bonus = faturamento_anual * 0.3
        print("Assinatura é do tipo Basic, 30% ")
    elif assinatura.upper() == "SILVER":
        bonus = faturamento_anual * 0.2
        print("Assinatura é do tipo Silver, 20%")
    elif assinatura.upper() == "GOLD":
        bonus = faturamento_anual * 0.1
        print("Assinatura é do tipo Gold, 10%")
    elif assinatura.upper() == "PLATINUM":
        bonus = faturamento_anual * 0.05
        print("Assinatura é do tipo Platinum, 5%")
    else:
        print("Tipo de assinatura inválida")
        continue
    # Exibir o valor do bonus com 2 casas decimais
    print("O valor do bônus que o cliente vai pagar é: R$ {:.2f}".format(bonus))







