import json
from datetime import datetime

jsonString = '''{\"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}, \"alertPrecip\": {\"0\": \"X\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertVelViento\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"X\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMax\": {\"0\": \"-\", \"1\": \"-\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"X\", \"6\": \"-\", \"7\": \"-\"}, \"alertTmpMin\": {\"0\": \"-\", \"1\": \"X\", \"2\": \"-\", \"3\": \"-\", \"4\": \"-\", \"5\": \"-\", \"6\": \"-\", \"7\": \"-\"}, \"prcp\": {\"0\": 40.0, \"1\": 1.65, \"2\": 14.01, \"3\": 5.07, \"4\": 16.55, \"5\": 2.17, \"6\": 2.77, \"7\": 1.73}, \"velViento\": {\"0\": 3.56, \"1\": 5.07, \"2\": 5.38, \"3\": 3.95, \"4\": 4.74, \"5\": 3.75, \"6\": 4.08, \"7\": 5.94}, \"tmpMax\": {\"0\": 27.16, \"1\": 31.1, \"2\": 30.2, \"3\": 29.5, \"4\": 28.87, \"5\": 29.78, \"6\": 28.96, \"7\": 28.25}, \"tmpMin\": {\"0\": 25.64, \"1\": 24.64, \"2\": 25.84, \"3\": 25.56, \"4\": 25.72, \"5\": 24.86, \"6\": 25.96, \"7\": 25.47}, \"dt\": {\"0\": 1685116800, \"1\": 1685203200, \"2\": 1685289600, \"3\": 1685376000, \"4\": 1685462400, \"5\": 1685548800, \"6\": 1685635200, \"7\": 1685721600}}'''

data = json.loads(jsonString)

def unix_a_fecha(unix_time):
    return datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d')

def revisar_alertas(data):
    alertas = ['alertPrecip', 'alertVelViento', 'alertTmpMax', 'alertTmpMin']
    
    for i in range(8):
        fecha = unix_a_fecha(data['dt'][str(i)])
        
        for alerta in alertas:
            if data[alerta][str(i)] == "X":
                if alerta == 'alertPrecip':
                    print(f'Alerta de lluvia en {fecha}: Nivel de lluvia {data["prcp"][str(i)]} mm')
                elif alerta == 'alertVelViento':
                    print(f'Alerta de viento en {fecha}: Velocidad del viento {data["velViento"][str(i)]} m/s')
                elif alerta == 'alertTmpMax':
                    print(f'Alerta de temperatura máxima en {fecha}: Máxima {data["tmpMax"][str(i)]} °C')
                elif alerta == 'alertTmpMin':
                    print(f'Alerta de temperatura mínima en {fecha}: Mínima {data["tmpMin"][str(i)]} °C')

revisar_alertas(data)