distancia_km = int(input("Introduce la distancia total en km: "))
n = 0

for distancia in range(150000, distancia_km, 150000):
    print(f"Parada en el km {distancia}")
    n = n + 1

print(f"Total de paradas para repostar: {n}")