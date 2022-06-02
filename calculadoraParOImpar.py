eleccion = str(input('Que prefieres calcular los numeros pares o impares? -->'))

count = 0;

n1 = int(input('Desde que numero quieres empezar? -->'))
n2 = int(input('Hasta que numero quieres llegar? -->'))

if eleccion == 'Par' or eleccion == 'par':
    for i in range(n1,n2):
        if i%2==0:
            count+=1
if eleccion == 'impar' or eleccion == 'impar':
    for i in range(n1,n2):
        if i%3==0:
            count+=1
                
print(count)
