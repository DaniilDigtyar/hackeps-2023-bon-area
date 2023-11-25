import itertools

def calcular_distancia(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def calcular_longitud_ruta(ruta):
    longitud = 0
    for i in range(len(ruta) - 1):
        longitud += calcular_distancia(ruta[i], ruta[i + 1])
    return longitud

def tsp_fuerza_bruta(puntos):
    puntos = [(0, 0)] + puntos + [(10, 10)]
    mejor_ruta = None
    mejor_longitud = float('inf')

    for perm in itertools.permutations(puntos[1:-1]):
        ruta_actual = [puntos[0]] + list(perm) + [puntos[-1]]
        longitud_actual = calcular_longitud_ruta(ruta_actual)

        if longitud_actual < mejor_longitud:
            mejor_longitud = longitud_actual
            mejor_ruta = ruta_actual

    return mejor_ruta, mejor_longitud

def tsp_vecino_mas_cercano(puntos):
    puntos = [(0, 0)] + puntos + [(10, 10)]
    ruta = [puntos[0]]
    puntos_restantes = set(puntos[1:])

    while puntos_restantes:
        punto_actual = ruta[-1]
        vecino_mas_cercano = min(puntos_restantes, key=lambda p: calcular_distancia(punto_actual, p))
        ruta.append(vecino_mas_cercano)
        puntos_restantes.remove(vecino_mas_cercano)

    ruta.append(puntos[-1])
    longitud_total = calcular_longitud_ruta(ruta)

    return ruta, longitud_total

def resolver_tsp(puntos_intermedios):
    if len(puntos_intermedios) <= 15:
        return tsp_fuerza_bruta(puntos_intermedios)
    else:
        return tsp_vecino_mas_cercano(puntos_intermedios)

# Ejemplo de uso
puntos_intermedios = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20)]
mejor_ruta, mejor_longitud = resolver_tsp(puntos_intermedios)

print("Mejor ruta:", mejor_ruta)
print("Longitud mínima:", mejor_longitud)

