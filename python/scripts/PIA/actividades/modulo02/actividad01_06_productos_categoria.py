# 

productos = [
    ("Laptop", "Electrónica", 850000),
    ("Mouse", "Electrónica", 5000),
    ("Escritorio", "Muebles", 120000),
    ("Silla", "Muebles", 45000),
    ("Teclado", "Electrónica", 15000),
    ("Estante", "Muebles", 65000),
]


productos_por_categoria = {} # diccionario que mantendra para cada categoria lista de nombre de productos
for nombre, categoria, precio in productos:
    if categoria in productos_por_categoria:
        productos_por_categoria[categoria].append(nombre)
    else:
        productos_por_categoria[categoria] = [nombre]

print("Productos por categoría:")
for categoria, nombres in productos_por_categoria.items():
    print(f"  {categoria}: {nombres}")

# 2) Precio promedio por categoría
precios_por_categoria = {}
for nombre, categoria, precio in productos:
    if categoria in precios_por_categoria:
        precios_por_categoria[categoria].append(precio)
    else:
        precios_por_categoria[categoria] = [precio]

promedios = {}
print("\nPrecio promedio por categoría:")
for categoria, precios in precios_por_categoria.items():
    promedio = sum(precios) / len(precios)
    promedios[categoria] = promedio
    print(f"  {categoria}: ${promedio:,.2f}")

# 3) Categoría con el promedio más alto
categoria_top = None
promedio_top = 0
for categoria, promedio in promedios.items():
    if promedio > promedio_top:
        promedio_top = promedio
        categoria_top = categoria

print(f"\nLa categoría con el precio promedio más alto es '{categoria_top}' con ${promedio_top:,.2f}")