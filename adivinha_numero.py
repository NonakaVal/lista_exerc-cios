

import random
def jogo_adivinha_numero(mensagem):
    """Jogo adivinha numero
    numero_a_adivinhas: gera um número aleatório em um intervalo
    t: numero de tentativas
    while: cria o loop que recebe e verifica a validade do valor digitado, além de contar as tentativas
    """

    numero_a_adivinhar = (random.randint(1, 50))
    t = 5
    while t > 0:
        try:
            chute = int(input(mensagem))
            if chute > numero_a_adivinhar:
                t = t - 1
                print(f"o valor {chute} é maior que o numero certo, e restam {t} tentativas")
            elif chute < numero_a_adivinhar:
                t = t - 1
                print(f"o valor {chute} é menor que o numero certo, e restam {t} tentativas")
            else:
                print("voce acertou")
                break

        except ValueError:
            print("digite um valor valido(int)")
    print("jogo acabou")


jogo_adivinha_numero("chute um numero de 1 a 50\n")

