# .count()
valores = [0,0,0,1,2,3,4] #conta quantas vezes repete o numero informado (0) = 3
print(valores.count(0))

# .count()
letras_acertadas = ['_','_','_','_','_','_',]
letras_faltando = print(str(letras_acertadas.count('_',))) #detecta quantas letras ainda falta para o nosso usuario preencher
letras_acertadas = ['a','b','c','_','_','_',]
letras_faltando = print(str(letras_acertadas.count('_',))) #detecta quantas letras ainda falta para o nosso usuario preencher

# .index()
frutas = ['Banana','Morango','Maçã','Uva'] #mostra o indice do elemento informado, lembrando que indice começa no 0, 1, 2,...
print(frutas.index('Uva'))

# quando o indice nao encontra o valor informado apresenta erro
#frutas = ['Banana','Morango','Maçã','Uva']
#print(frutas.index('melancia'))

#solução
frutas = ['Banana','Morango','Maçã','Uva']
#fruta_buscada = 'Melancia' #valor fixo
fruta_buscada = input('Fruta?') #utilizando interação com usuario, input()
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista de frutas'.format(fruta_buscada))

