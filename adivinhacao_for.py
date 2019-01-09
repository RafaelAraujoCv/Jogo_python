import random #adiciona biblioteca(modulo) do random, para numero aleatorio

def jogar(): #codigo abaixo vira uma função criada pelo "def" >>>> função jogar():

    print("********************")
    print("Bem vindo ao jogo de adivinhação !")
    print("********************")

    numero_secreto = random.randrange(1,101) #criação de variavel para numero ha ser acertado, sempre usando "underline" no lugar de espaço//randrange= adura a determinar limite do numero a ser gerado netre 0 e 100(1,1001)
    print(numero_secreto) #testar o numero secreto
    total_de_tentativas = 0 #criação de variavel para numero total de tentativas, sempre usando "underline" no lugar de espaço
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("(1) Fácil (2) Médio (3)Difícil")

    nivel = int(input("Defina o nível:")) # "int" transforma o valor de string(input) para inteiro e guarda na variavel

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    elif(nivel == 3):#else:
        total_de_tentativas = 5#    total_de_tentativas = 5
    else:
        print("Escolha um nivel de dificuldade - (1) Fácil (2) Médio (3)Difícil ")

    for rodada in range(1, total_de_tentativas + 1): #laço for **** in range(***, *** + 1): >>>> criando a var rodada, função range(inicio da contagem, ate o maximo)
        #print("Tentativa",rodada,"de",total_de_tentativas) #concatenação, mostra mensagem com valores das var >>> 1°opção sem função
        print("Tentativa {} de {}".format(rodada,total_de_tentativas)) #concatenação, mostra mensagem com valores das var >>> 2°opção com função
        #print("Tentativa {1} de {0}".format(rodada,total_de_tentativas)) #concatenação, mostra mensagem com valores das var >>> 2°opção com função
        #print("Tentativa {0} de {1}".format(rodada,total_de_tentativas)) #concatenação, mostra mensagem com valores das var >>> 2°opção com função
        chute_str = input("Digite um numero entre 1 e 100: ") #função input(***) mostra na tela a mensagem , numero digitado e guardado em uma variavel string(str)
        print("Você digitou ", chute_str) # função print(***) imprime na tela o numero digitado
        chute = int(chute_str) # função inf(***) trasnforma a variavel em numero inteiro

        if(chute < 1 or chute > 100): # verifica de o chute é menor< ou/OR maior> , um ou outro para ser os dois, seria e/AND
            print("Você deve digitar um numero entre 1 e 100!") #imprime erro( informação/dica )
            continue #para e continua a interação, no caso volta ao inicio

        acertou = chute == numero_secreto #condição colocada em uma var
        maior = chute > numero_secreto #condição colocada em uma var
        menor = chute < numero_secreto #condição colocada em uma var

        if(acertou): #if(******): else: >>>>> acertou é uma var onde tem uma condição salva
            print("Você acertou e fez {} pontos !".format(pontos))
            break #sai do laço
        else:
            if(maior): #>>>>> maior é uma var onde tem uma condição salva
                print("Você errou ! O seu chute foi maior que o número secreto.")
            elif(menor): #if + else >>>>> menor é uma var onde tem uma condição salva ou usar else
                print("Você errou ! O seu chute é menor que o número secreto.")
                pontos_perdidos = abs(numero_secreto - chute) #abs >>>> tarsnforma numero negativo em positivo
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1

    print("Fim do Jogo !") #função que imprime na tela

#codigo abaixo ja esta fora da função

if(__name__ == "__main__"): #permite chamar somente este arquivo no terminal
    jogar()