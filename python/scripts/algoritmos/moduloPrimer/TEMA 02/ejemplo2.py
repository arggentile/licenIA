    # Coordenadas de puntos (x, y)
p1 = (2, 5)
p2 = (7, 1)

print("Punto 1:", p1)
print("Punto 2:", p2)

# Distancia Manhattan (muy usada en heurísticas como A*)
dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
print("Distancia Manhattan:", dist)
