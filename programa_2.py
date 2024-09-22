def mezclar_diccionarios(dic1, dic2):
    diccionario_mezclado = dic1.copy()
    
    for clave, valor in dic2.items():
        if clave not in diccionario_mezclado:
            diccionario_mezclado[clave] = valor
            
    return diccionario_mezclado

dic1 = {1: 'a', 2: 'b', 3: 'c'}
dic2 = {3: 'x', 4: 'y', 5: 'z'}

diccionario_resultado = mezclar_diccionarios(dic1, dic2)
print(diccionario_resultado)