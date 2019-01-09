print("Tentativa {} de {}".format(3,10)) #coloca os valores na ordem denominada
print("Tentativa {1} de {0}".format(3,10)) #digita a ordem direto nos {}, podendo mudar a ordem denominada >>>> .format(0,1) é igual a .format(3,10)
print("R$ {}".format(1.59)) #numero quebrado ou float, peso e valor moeda
print("R$ {:f}".format(1.59)) #{:f} >>> informa que esta recebendo numero de valor float
print("R$ {:.2f}".format(1.59)) #manipulando quantos numeros antes e depois, ex: depois do ponto( . ) quero 2 numeros
print("R$ {:.2f}".format(1.5)) #manipulando quantos numeros antes e depois, ex: depois do ponto( . ) quero 2 numeros
print("R$ {:.2f}".format(1234.5)) #manipulando quantos numeros antes e depois, ex: depois do ponto( . ) quero 2 numeros
print("R$ {:7.2f}".format(1234.5)) ##manipulando quantos numeros antes e depois, ex: antes do ponto ( . ) numero total de
# carasteres mesmo os depois do ponto e depois do ponto( . ) quero 2 numeros >>> total 7 = 7 onde 2 é alem do ponto
print("R$ {:7.2f}".format(4.5)) #coloca espaços antes do 4, onde totaliza 7
print("R$ {:07.2f}".format(4.5)) #coloca 0(zeros) antes do 4, onde totaliza 7
print("R$ {:08.3f}".format(4.5)) #coloca 0(zeros) antes do 4 e depois do 5(3f definido), onde totaliza 8
print("R$ {:07d}".format(4)) # para numeros inteniros utiliza o d , 7 numeros no total onde antes do 7 são zeros
print("R$ {:07d}".format(46)) #7 numeros no total onde antes do 7 são zeros
print("R$ {:7d}".format(4)) #coloca espaços antes do 4, onde totaliza 7
print("Data {:2d}/{:2d}".format(9,4))
print("Data {:02d}/{:02d}".format(9,4))
print("Data {:2d}/{:2d}".format(19,11))

pontos_perdidos = 3/2 # / divição
print(pontos_perdidos)
pontos_perdidos = 3//2 # // divide e arredonda o numero
print(pontos_perdidos)



