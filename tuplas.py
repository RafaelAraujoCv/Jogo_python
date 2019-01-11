lista = [2,5,2,8,5]
palavra = "banana"

print(len(lista)) #len mostra quantidade de caracteres/numero da lista
print(len(palavra)) #len mostra quantidade de caracteres/numero da lista
print(min(lista)) #mostra o numero minimo dalista, menor numero
print(min(palavra)) #mostra a letra minima, mais baixa
print(lista[3]) #printa o valor na posição terceiro(3) elemento da lista
serie = range(0,10) #lista de 0 ate 9, inicio e fim
print(serie)
print(serie[0]) #mostra o valor na posição zero(0)
dias = ["S","T","Q","Q","S","S","D"] #lista comdiasda semana, string
print(type(dias))
print(dias)
dias.append("D2") #add elemento novo na lista
print(dias)
dias.pop() #deleta o ultimo valor da lista
print(dias)
dias = ("S","T","Q","Q","S","S","D")
print(type(dias)) #mostra o tipo da variavel
ponto = (3,5)

ponto = (3,5) #sequencia fixa
p1 = (3,5)
p2 = (4,6)
p3 = (5,7)
line = [p1,p2,p3] #var de lista dinamica, onde guarda valores de variareis de lista fixa. duas lista em uma var
print(line)

p1 = ('Nico',39) #var lista fixa com dois valores diferente - str e numero
p2 = ('Flavio',37) #var lista fixa com dois valores diferente - str e numero
instrutores = [p1,p2] #var lista dinamica que guarad dois var lista fixa
print(instrutores)
print(instrutores[0]) #busca o indice da lista dinamica
print(instrutores[0][1]) #busca o indice da lista dinamica e depois busca o indice da lista fixa dentro do primeiro indice

palavras = [] #nova lista dinamica []
palavras.append("banana") #adiciona nova palavra na lista  .append
palavras.append("abacaxi") #adiciona nova palavra na lista  .append
nova = tuple(palavras) #transforma a lista em uma lista imutavel () ( fixa ) e guarda em uma var
print(nova)

outra = list(nova) #transforma a lista fixa () em lista dinamica []
print(outra)


lista = [11122233344, 22233344455, 33344455566] #nova lista criada
print(lista)
lista.append(11122233344) #funciona! #lista permite valor duplicado
print(lista)
colecao = {11122233344, 22233344455, 33344455566}
print(colecao)
colecao.add(44455566677) #vai adicionar pois não existe ainda
print(colecao)
colecao.add(11122233344) #nao vai adicionar pois este CPF já existe!
print(colecao)





# utilizar [] significa lista - sequencia dinamica, pode colocar valor ou remover ( .append e .pop )
# utilizar () significa tuple - sequencia fixa, nao pode mudar
# utilizar {} significa set -  sequencia dinamica que não aceita valor duplicado, pode colocar valor usando .add >>>> não tem índice. E como não temos um índice não sabemos em qual ordem vem os valores