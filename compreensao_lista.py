total = 0 #contator
palavra = "python rocks!" #palavra a ser contada
acabou = False #falso ou verdadeiro

while (not acabou): #faça isso enquanto for false
    acabou = (total == len(palavra)) # total for igual a quantidade(len) de letras da palavra é verdadeiro >>>> muda o valor da var de \false para \true
    print(len(palavra))
    print(acabou)
    total = total + 1 #contador, soma
print(total - 1) # retira um do ultimo ciclo


inteiros = [1,3,4,5,7,8,9]
pares = []
for numero in inteiros:
    if numero % 2 == 0:
        print(numero) #Para descobrir se um número é par, usamos a condição numero%2 == 0, que verifica se o resto de uma divisão por 2 é zero
        pares.append(numero)
        print(pares)

#O código usando List Comprehension relativo ficaria muito mais enxuto
inteiros = [1,3,4,5,7,8,9]
pares = [x for x in inteiros if x % 2 == 0]
print(pares)