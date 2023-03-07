import random

def imprime_mensagem_abertura():
    print("***************************")
    print("Bem vindo ao jogo de Forca!")
    print("***************************")
def carregar_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()



    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta
def mostra_acertos(palavra):
    return ["_" for letra in palavra]
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():
    imprime_mensagem_abertura()
    palavra_secreta = carregar_palavra()
    letras_acertadas = mostra_acertos(palavra_secreta)

    #for letra in palavra_secreta:
        #letras_acertadas.appendi("_") < outra opção

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        else:
            erros = erros + 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas


        print(letras_acertadas)


        print("Jogando...")

    print("Fim do jogo!")
    if (enforcou == True):
        print("Enforcou! Você perdeu!")
        print("A palavra secreta era {}!".format(palavra_secreta))
    elif(acertou == True):
        print("Parabéns! Você acertou!")

if(__name__== "__main__"):
    jogar()