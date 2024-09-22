# Reto_13

### 1. Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario.
```
# Diccionario de ejemplo
mi_diccionario = {'a': 5, 'b': 2, 'c': 9, 'd': 1}

# Extrae los valores del diccionario
valores = list(mi_diccionario.values())

# Implementa el algoritmo de ordenamiento burbuja (bubble sort)
n = len(valores)
for i in range(n):
    for j in range(0, n-i-1):
        if valores[j] > valores[j+1]:
            # Intercambia si el valor actual es mayor que el siguiente
            valores[j], valores[j+1] = valores[j+1], valores[j]

# Imprime los valores ordenados
for valor in valores:
    print(valor)
```
### 2. Desarrollar una funci�on que reciba dos diccionarios como par�ametros y los mezcle, es decir, que se construya un nuevo diccionario con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.
```
def mezclar_diccionarios(dic1, dic2):
    # Crea una copia del primer diccionario
    diccionario_mezclado = dic1.copy()
    
    # Agrega las claves del segundo diccionario solo si no están en el primero
    for clave, valor in dic2.items():
        if clave not in diccionario_mezclado:
            diccionario_mezclado[clave] = valor
            
    return diccionario_mezclado

# Ejemplo
dic1 = {1: 'a', 2: 'b', 3: 'c'}
dic2 = {3: 'x', 4: 'y', 5: 'z'}

diccionario_resultado = mezclar_diccionarios(dic1, dic2)
print(diccionario_resultado)
```

### 3. Dado el JSON:
```
{
	"jadiazcoronado":{
		"nombres": "Juan Antonio",
		"apellidos": "D��az Coronado",
		"edad":19,
		"colombiano":true,
		"deportes":["F�utbol","Ajedrez","Gimnasia"]
	},
	"dmlunasol":{
		"nombres": "Dorotea Maritza",
		"apellidos": "Luna Sol",
		"edad":25,
		"colombiano":false,
		"deportes":["Baloncesto","Ajedrez","Gimnasia"]
	}
}
```
Cree un programa que lea de un archivo con dicho JSON y:

* Imprima los nombres completos (nombre y apellidos) de las personas que practican el deporte ingresado por el usuario.
* Imprima los nombres completos (nombre y apellidos) de las personas que est�en en un rango de edades dado por el usuario.
```
import json

datos_json = '''
{
    "jadiazcoronado":{
        "nombres": "Juan Antonio",
        "apellidos": "Díaz Coronado",
        "edad": 19,
        "colombiano": true,
        "deportes": ["Fútbol", "Ajedrez", "Gimnasia"]
    },
    "dmlunasol":{
        "nombres": "Dorotea Maritza",
        "apellidos": "Luna Sol",
        "edad": 25,
        "colombiano": false,
        "deportes": ["Baloncesto", "Ajedrez", "Gimnasia"]
    }
}
'''

# Función para cargar el JSON
def cargar_datos_json_desde_codigo():
    datos = json.loads(datos_json)
    return datos

# Función para encontrar a las personas por deporte
def encontrar_por_deporte(datos, deporte):
    for usuario, info in datos.items():
        if deporte in info['deportes']:
            print(f'{info["nombres"]} {info["apellidos"]} practica {deporte}')

# Función para encontrar a las personas por rango de edades
def encontrar_por_rango_edad(datos, edad_min, edad_max):
    for usuario, info in datos.items():
        if edad_min <= info['edad'] <= edad_max:
            print(f'{info["nombres"]} {info["apellidos"]} tiene {info["edad"]} años')

# Función principal
def programa_principal():
    # Cargar el JSON desde el código
    datos = cargar_datos_json_desde_codigo()

    # Pide al usuario el deporte
    deporte = input("Ingrese el deporte que desea buscar: ")
    print(f"Personas que practican {deporte}:")
    encontrar_por_deporte(datos, deporte)
    
    # Pide al usuario el rango de edades
    edad_min = int(input("Ingrese la edad mínima: "))
    edad_max = int(input("Ingrese la edad máxima: "))
    print(f"Personas en el rango de edad {edad_min}-{edad_max}:")
    encontrar_por_rango_edad(datos, edad_min, edad_max)

# Ejecuta el programa principal
programa_principal()
```
