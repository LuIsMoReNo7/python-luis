# desarrollar un algoritmo que muestres los números divisibles por 5 de una lista de números.

números = [10, 14, 20, 31, 35, 40, 45, 52, 57]

divisible_por_5 = lambda x: x % 5 == 0

numeros_div_5 = filter(divisible_por_5, números)

