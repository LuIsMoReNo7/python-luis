#ingresamos la cantidad de filas 
n = int(input("cuantas filas quieres?"))
#fila que es el mismo numeo que el de columnas
a=1
#cantidad de numeros que hay que imprimir
b=2
#numero de columnas que hay en la fila
c=3
frase =''
for a in range(1,n+1):
      for c in range(1,a+1): #c va a recorrer de 1 hasta a. ejemplo en la 4 (a=4 c=1,2,3,4)
        frase+=(str(b)+(' '))
        b+=0
        print(frase)
        frase =''
