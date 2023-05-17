'''''
4 – Um grande cliente seu sofreu um ataque hacker:
    o servidor foi sequestrado por um software malicioso que criptografou todos os discos
Pede a digitação de uma senha para a liberação da máquina e é claro que os criminosos exigem um pagamento para informar a senha.
Ao analisar o código do programa deles:
  Você descobre que a senha é “LIBERDADE” seguida do fatorial dos minutos que a máquina estiver marcando no momento da digitação da senha
  (se a máquina estiver marcando 5 minutos, a senha será LIBERDADE120).
Crie um programa que receba do usuário os minutos atuais e exiba na tela a senha necessária para desbloqueio.
ATENÇÃO: seu programa não pode utilizar funções prontas para o cálculo do fatorial.
    Ele deve obrigatoriamente utilizar loop.
'''

print("Desbloqueando o servidor: gerando a senha com fatorial personalizado")

# Solicita os minutos atuais
minutos_atuais = int(input("Digite os MINUTOS atuais do horário do seu computador: "))


if minutos_atuais >= 60:
    print("O minuto inserido não existe. \nNão foi possível gerar a senha.")
else:
    # Calcula o fatorial dos minutos utilizando um loop
    fatorial = 1
    for x in range(1, minutos_atuais + 1):
        fatorial *= x

    # Exibe a senha para desbloqueio
    senha = "LIBERDADE" + str(fatorial)
    print("A senha para o desbloqueio é:{}".format(senha))

