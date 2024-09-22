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

def cargar_datos_json_desde_codigo():
    datos = json.loads(datos_json)
    return datos

def encontrar_por_deporte(datos, deporte):
    for usuario, info in datos.items():
        if deporte in info['deportes']:
            print(f'{info["nombres"]} {info["apellidos"]} practica {deporte}')

def encontrar_por_rango_edad(datos, edad_min, edad_max):
    for usuario, info in datos.items():
        if edad_min <= info['edad'] <= edad_max:
            print(f'{info["nombres"]} {info["apellidos"]} tiene {info["edad"]} años')

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

programa_principal()