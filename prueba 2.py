#crear un programa que genere la suma el numero actual y el anterior

#solicitamos que ingrese la cantidad de series
n=int(input("ingrese la cantidad de series : "))
#ponemos los primeros valores
actual = int(input("ingrese el valor actual : "))
anterior = int(input("ingrese el valor anterior : "))
#mostramos el primer valor
print("la suma =  ",end="")
#asignamos una variable de control
s = 0
#generamos la serie
for s in range(1,n):
      print(actual,"+",actual -1, "=",actual+(anterior-1))
      
     
     
