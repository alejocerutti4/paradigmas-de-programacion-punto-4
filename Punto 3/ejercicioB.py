entrada = input()
entradaList = entrada.split()
S, T, F = int(entradaList[0]), int(entradaList[1]), int(entradaList[2])

# Si sale a las 0, lo tomamos como 24 para poder calcular más tarde la llegada.
if S == 0:
    S = 24

# Calculamos la llegada.
llegada = S + T + F

# Si llegada es mayor a 24, significa que llega el día próximo, por ende restamos 24hs.
if llegada > 24:
    llegada = llegada-24
    print(llegada)
# Si llegada es igual a 24, decimos que llego a las 0hs.
elif llegada == 24:
    llegada = 0
    print(llegada)
# Si esta entre 0 y 24, imprimimos la hora directamente.
else:
    print(llegada)