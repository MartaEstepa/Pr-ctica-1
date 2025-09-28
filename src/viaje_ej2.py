distancia_km = int(input("Dime la distancia que quieres recorrer: "))
velocidad_kmh = int(input("Dime a la velocidad que vas: "))
tiempo_horas = distancia_km // velocidad_kmh
tiempo_dias = tiempo_horas // 24
print(f"Tardarías {tiempo_dias} días en llegar.")