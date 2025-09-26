distancia_km = 225000000
velocidad = 10000
tiempo_dias = 0
tiempo_horas = 0


for velocidad in range(10000, 50001, 10000):
        tiempo_horas = distancia_km // velocidad
        tiempo_dias = tiempo_horas / 24
        print(f"Velocidad: {velocidad} km/h -> Tiempo: {tiempo_dias} días")