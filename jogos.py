import forca #importa o codigo do arquivo forca.py
import adivinhacao_for #importa o codigo do arquivo adivinhacao_for.py

def escolhe_jogo():
    print("**********************")
    print("*Escolha o seu Jogo !*")
    print("**********************")

    print("(1) Forca (2) Adivinhação") #função que imprime na tela

    jogo = int(input("Qual o jogo ?")) # "int" transforma o valor de string(input) para inteiro e guarda na variavel

    if(jogo == 1):
        print("Jogar forca !")
        forca.jogar() # chama o outro arquivo >>>> forca|é o nome do arquivo|.jogar()| é a função criada no começo dos arquivos |
    elif(jogo == 2):
        print("Jogar Adivinhação !")
        adivinhacao_for.jogar() # chama o outro arquivo >>>> adivinhacao_for|é o nome do arquivo|.jogar()| é a função criada no começo dos arquivos |

#codigo abaixo ja esta fora da função

if(__name__ == "__main__"): #permite chamar somente este arquivo no terminal
    escolhe_jogo()