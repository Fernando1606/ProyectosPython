print('Hasta que numero quieres realizar la sucesión de Fibonacci?')
aux=0
aux2=1
aux3=0
numero = int(input())

def fib(numero, aux, aux2, aux3):

    print(aux3)
    aux=aux2
    aux2=aux3
    aux3=aux+aux2

    if(numero>aux3):
        fib(numero, aux, aux2, aux3)
    else:
        print('Acabado')
    return aux3


        
fib(numero, aux,aux2, aux3)