def jogar(): #codigo abaixo vira uma função criada pelo "def" >>>> função jogar():

    print("******************************")
    print("*Bem vindo ao jogo de forca !*")
    print("******************************")

    palavra_secreta = "banana" #var que guarda uma palavra
    letras_acertadas = ["_","_","_","_","_","_"]

    enforcou = False #condição verdade ou falso
    acertou  = False #condição verdade ou falso

    while(not enforcou and not acertou): #laço de repetição(

        chute = input("Qual letra?") #guarda a palavra enviada pelo jogador
        chute = chute.strip() #retira espaços antes e depois da letra digitada

        index = 0
        for letra in palavra_secreta: #
            if(chute.upper() == letra.upper()): #compara letras maiusculas .upper()
                #print("Encontrei a letra {} na posição {}".format(letra,posicao))
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)










    print("Fim do Jogo !")

#codigo abaixo ja esta fora da função

if(__name__ == "__main__"): #permite chamar somente este arquivo no terminal
    jogar()