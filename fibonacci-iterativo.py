print('Hasta que numero quieres realizar la sucesión de Fibonacci?')
numero = int(input())

aux=0
aux2=1
aux3=0

while (aux3>numero):
    print(aux3)
    aux=aux2
    aux2=aux3
    aux3=aux+aux2
