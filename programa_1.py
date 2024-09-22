mi_diccionario = {'a': 5, 'b': 2, 'c': 9, 'd': 1}

valores = list(mi_diccionario.values())

n = len(valores)
for i in range(n):
    for j in range(0, n-i-1):
        if valores[j] > valores[j+1]:
            # Intercambiar si el valor actual es mayor que el siguiente
            valores[j], valores[j+1] = valores[j+1], valores[j]

for valor in valores:
    print(valor)
