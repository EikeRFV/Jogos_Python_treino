import random
import _random
def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_random = random.randint(1, 50)
    tentativas = 0
    pontos = 100

    print("Escolha sua dificuldade:")
    print("(1)Fácil    (2)Médio    (3)Difícil")

    nivel = int(input("Defina o nível: "))

    if (nivel == 1):
        tentativas = 15
    elif (nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = 5
    else:
        print("Insira um comando válido!!!!!!!!!!")

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 50: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)
        if (chute < 1) or (chute > 50):
            print("Digite um número válido!")
            continue
        acertou = numero_random == chute
        maior = chute > numero_random
        menor = chute < numero_random

        if (acertou):
            print("Acertou!!")
            print("Você fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! Seu chute é maior que o número.")

            elif (menor):
                print("Você errou! Seu chute é menor que o número.")
            pontos_perdidos = numero_random - chute
            pontos_perdidos = abs(pontos_perdidos)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__== "__main__"):
    jogar()