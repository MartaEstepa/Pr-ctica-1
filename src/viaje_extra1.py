distancia_km = int(input("Introduce la distancia total en km: "))
n = 0

for distancia in range(150000, distancia_km + 1, 150000):
    print(f"Parada en el km {distancia}")
    n = n + 1

print(f"Total de paradas para repostar: {n}")


# range (1, 5)
# siendo 1 límite inferior y 5 el límite superior
# si solo pusieramos un número se consideraría límite superior

# range (1, 5, 2)
#siendo 2 el rango del salto