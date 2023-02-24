# desarrollar un algoritmo que muestres los números divisibles por 5 de una lista de números.

números = [10, 14, 20, 31, 35, 40, 45, 52, 57]

#hacemos uso de lambda y filter
#lambda: sirve por si una función es utilizada una sola vez,
#lo mejor es usar una función lambda para evitar código innecesario y desorganizado.
#filter: sirve para filtrar de forma eficiente los elementos usando una 
#función que proporcionamos
divisible_por_5 = lambda x: x % 5 == 0

numeros_div_5 = filter(divisible_por_5, números)

#obtenemos la lista de los numeros divisibles por 5

print(list(numeros_div_5))


