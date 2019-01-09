print("********************")
print("Bem vindo ao jogo de adivinhação !")
print("********************")

numero_secreto = 42 #criação de variavel para numero ha ser acertado, sempre usando "_" no lugar de espaço
total_de_tentativas = 3 #criação de variavel para numero total de tentativas, sempre usando "_" no lugar de espaço
rodada = 1 #criação de variavel para numero total de tentativas, sempre usando "_" no lugar de espaço

while(rodada <= total_de_tentativas): #laço while(*****): >>>>> acertou é uma var onde tem uma condição salva
    #print("Tentativa",rodada,"de",total_de_tentativas) #concatenação, mostra mensagem com valores das var >>> 1°opção sem função
    print("Tentativa {} de {}".format(rodada,total_de_tentativas)) #concatenação, mostra mensagem com valores das var >>> 2°opção com função
    chute_str = input("Digite seu numero: ") #função input(***) mostra na tela a mensagem , numero digitado e guardado em uma variavel string(str)
    print("Você digitou ", chute_str) # função print(***) imprime na tela o numero digitado
    chute = int(chute_str) # função inf(***) trasnforma a variavel em numero inteiro

    if(chute < 1 or chute > 100): # verifica de o chute é menor< ou/OR maior> , um ou outro para ser os dois, seria e/AND
        print("Você deve digitar um numero entre 1 e 100!") #imprime erro( informação/dica )
        continue #para e continua a interação, no caso volta ao inicio

    acertou = chute == numero_secreto #condição colocada em uma var
    maior = chute > numero_secreto #condição colocada em uma var
    menor = chute < numero_secreto #condição colocada em uma var

    if(acertou): #if(******): else: >>>>> acertou é uma var onde tem uma condição salva
        print("Você acertou !")
        break #sai do laço
    else:
        if(maior): #>>>>> maior é uma var onde tem uma condição salva
            print("Você errou ! O seu chute foi maior que o número secreto.")
        elif(menor): #if + else >>>>> menor é uma var onde tem uma condição salva ou usar else
            print("Você errou ! O seu chute é menor que o número secreto.")

    rodada = rodada + 1

print("Fim do Jogo !") #função que imprime na tela