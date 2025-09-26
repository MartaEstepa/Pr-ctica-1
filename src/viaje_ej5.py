respuesta = "s"

while respuesta == "s":
    distancia_km = int(input("Dime la distancia que quieres recorrer en km: "))
    velocidad_kmh = int(input("Dime a la velocidad que vas en km/h: "))
    tiempo_horas = distancia_km // velocidad_kmh
    tiempo_dias = tiempo_horas / 24
    print(f"Tardarías {tiempo_dias} días en llegar.")
    respuesta = input("Quieres hacer otra simulación? (s/n): "). lower() #lower convierte en minúsculas el input