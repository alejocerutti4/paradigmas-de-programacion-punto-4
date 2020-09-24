# Cantidad de LEDS requeridos para crear un número con LEDS
tablaValores = (6,2,5,5,4,5,6,3,7,6)

# Cantidad de Inputs
n = int(input())

# Para cada input, tomamos un valor
for i in range(n):
    # Reseteamos el total
    totalLEDS = 0
    cantidadLEDS = input()
    # Para cada número en el input, sumamos al total de LEDS la cantidad almacenada en la tupla
    for j in cantidadLEDS:
        totalLEDS += tablaValores[int(j)]
    print(f"{int(totalLEDS)} leds")

