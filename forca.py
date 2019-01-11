import random

def jogar(): #codigo abaixo vira uma função criada pelo "def" >>>> função jogar():

    print("******************************")
    print("*Bem vindo ao jogo de forca !*")
    print("******************************")

    #palavra secreta manualmente
    #palavra_secreta = "banana".upper() #var que guarda uma palavra >>>>> palavra secreta ja sera .upper ( maiusculo )
    #letras_acertadas = ["_","_","_","_","_","_"]

    #palavra secreta dinamica >>> opção 1
    #palavra_secreta = "Maça".upper() #var que guarda uma palavra >>>>> palavra secreta ja sera .upper ( maiusculo )
    #letras_acertadas = [] #lista sem dados
    #
    #for letra in palavra_secreta: #pra cada letra dentro da palavra_secreta
    #    letras_acertadas.append("_") #adicionar o elemento "_" na lista letras_acertadas

    # palavra secreta dinamica >>> opção 2
    #palavra_secreta = "Maça".upper() #var que guarda uma palavra >>>>> palavra secreta ja sera .upper ( maiusculo )
    #letras_acertadas = ["_" for letra in palavra_secreta] # for é criado dentro da lista dinamica >>> Usa "_" para cada letra dentro da palavra_segreta

    # palavra secreta dinamica usando arquivo externo >>> opção 3
    arquivo = open("palavras.txt","r") #open= abre o arquivo palavras.txt e informa que sera leitura/reading "r" , guardando em uma var

    palavras = []
    for linha in arquivo: #laço para acessar cada linha do arquivo >>>> para cada linha dentro do arquivo:
        linha = linha.strip() # para retirar o \n(quebra de linha) no final de cada palavra
        palavras.append(linha) #adiciona cada linha na lista plavras[]

    arquivo.close() #fecha arquivo

    numero = random.randrange(0,len(palavras)) #

    palavra_secreta = palavras[numero].upper() #
    print(palavra_secreta)
    #palavra_secreta = "Maça".upper() #var que guarda uma palavra >>>>> palavra secreta ja sera .upper ( maiusculo )
    letras_acertadas = ["_" for letra in palavra_secreta] # for é criado dentro da lista dinamica >>> Usa "_" para cada letra dentro da palavra_segreta



    enforcou = False #condição verdade ou falso
    acertou  = False #condição verdade ou falso
    erros = 0

    while(not enforcou and not acertou): #laço de repetição(

        chute = input("Qual letra?") #guarda a palavra enviada pelo jogador
        chute = chute.strip().upper() #retira espaços antes e depois da letra digitada >>>>>> .strip e .upper ( ja é declarado diretamente na variavel onde recebe o chute

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra): #compara letras maiusculas .upper() >>>>>> if(chute.upper() == letra.upper()):
                    #print("Encontrei a letra {} na posição {}".format(letra,posicao))
                    letras_acertadas[index] = letra
                index += 1 #ou index = index + 1 >>>>> atribui +1
        else:
            erros += 1 #ou erros = erros + 1 >>>>> atribui +1

        enforcou = erros == 6 # se erros for igual a 6, muda p tipo da var enforcou
        acertou = "_" not in letras_acertadas #verificação: enquanto a letra "_" existe dentro da letra_acertadas >>> "-" nao deveria estar dentro de letras _acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou !")
    else:
        print("Você perdeu !")

    print("Fim do Jogo !")

#codigo abaixo ja esta fora da função

if(__name__ == "__main__"): #permite chamar somente este arquivo no terminal
    jogar()