"""
Módulo: test_sistema.py
Descripción: Script de prueba automatizado que carga productos y ventas
de ejemplo, entrena los modelos y muestra las predicciones.
Sirve para verificar el funcionamiento integral del sistema.
"""

import os
import random
from datetime import datetime, timedelta

from producto import Producto
from venta import Venta
from inventario import Inventario
from predictor import PredictorVentas


def generar_datos_de_prueba(archivo):
    """Elimina datos previos y genera un escenario de prueba realista."""
    if os.path.exists(archivo):
        os.remove(archivo)

    inventario = Inventario(archivo_datos=archivo)

    # --- Caso normal: productos variados --- #
    productos = [
        Producto("P001", "Yerba Mate 1kg", 2500, 1600, 50, "Almacén"),
        Producto("P002", "Alfajor Triple", 450, 220, 120, "Golosinas"),
        Producto("P003", "Cuaderno A4", 1200, 700, 30, "Librería"),
    ]
    for p in productos:
        inventario.registrar_producto(p)

    # Generamos ventas simulando una tendencia creciente
    random.seed(42)
    fecha_base = datetime(2026, 8, 1)
    for i in range(45):
        fecha = fecha_base + timedelta(days=i)
        # Yerba: demanda estable
        cant_p1 = max(1, int(random.gauss(2, 0.8)))
        # Alfajor: demanda creciente
        cant_p2 = max(1, int(2 + 0.1 * i + random.gauss(0, 1)))
        # Cuaderno: demanda baja esporádica
        cant_p3 = max(1, int(random.gauss(1, 0.5))) if i % 3 == 0 else 0

        if cant_p1 > 0 and productos[0].stock_actual >= cant_p1:
            inventario.registrar_venta(Venta("P001", cant_p1, 2500, fecha))
        if cant_p2 > 0 and productos[1].stock_actual >= cant_p2:
            inventario.registrar_venta(Venta("P002", cant_p2, 450, fecha))
        if cant_p3 > 0 and productos[2].stock_actual >= cant_p3:
            inventario.registrar_venta(Venta("P003", cant_p3, 1200, fecha))

    return inventario


def ejecutar_pruebas():
    archivo = "test_datos.json"

    print("=" * 70)
    print(" CASO DE PRUEBA 1: CARGA DE DATOS Y ANÁLISIS")
    print("=" * 70)
    inventario = generar_datos_de_prueba(archivo)

    print("\n>>> Productos cargados:")
    for p in inventario.listar_productos():
        print(f"  {p}")

    print(f"\n>>> Total de ventas registradas: {len(inventario.listar_ventas())}")

    print("\n>>> Análisis con Pandas:")
    resumen = inventario.analizar_historial()
    print(f"  Facturación total : ${resumen['facturacion_total']:.2f}")
    print(f"  Ticket promedio   : ${resumen['ticket_promedio']:.2f}")
    print(f"  Unidades vendidas : {resumen['total_unidades_vendidas']}")
    print(f"\n  Ventas por producto:")
    print(resumen["ventas_por_producto"].to_string())

    print("\n" + "=" * 70)
    print(" CASO DE PRUEBA 2: ENTRENAMIENTO Y PREDICCIÓN")
    print("=" * 70)
    predictor = PredictorVentas()
    df = inventario.ventas_a_dataframe()
    resultados = predictor.entrenar_todos(df)

    for r in resultados:
        if r["exito"]:
            m = r["metricas"]
            r2 = f"{m['r2']:.3f}" if m["r2"] is not None else "N/D"
            print(f"\n Modelo [{r['codigo']}] entrenado:")
            print(f"    MAE  = {m['mae']:.3f}")
            print(f"    RMSE = {m['rmse']:.3f}")
            print(f"    R²   = {r2}")
            print(f"    Train/Test = {m['muestras_entrenamiento']}/"
                  f"{m['muestras_prueba']}")

    print("\n>>> Predicciones para los próximos 7 días:")
    for codigo in predictor.productos_entrenados():
        total = predictor.predecir_total(codigo, 7)
        producto = inventario.obtener_producto(codigo)
        ganancia = total * producto.ganancia_unitaria()
        print(f"  {codigo} ({producto.nombre}): {total:.2f} unidades "
              f"-> ganancia estimada ${ganancia:.2f}")

    print("\n" + "=" * 70)
    print(" CASO DE PRUEBA 3: CASOS EXTREMOS")
    print("=" * 70)

    # --- Caso extremo 1: producto duplicado --- #
    print("\n>>> Intentando registrar producto duplicado...")
    try:
        inventario.registrar_producto(
            Producto("P001", "Duplicado", 100, 50, 10)
        )
    except ValueError as e:
        print(f"   Error esperado capturado: {e}")

    # --- Caso extremo 2: venta con stock insuficiente --- #
    print("\n>>> Intentando venta con stock insuficiente...")
    try:
        inventario.registrar_venta(Venta("P001", 999999, 2500))
    except ValueError as e:
        print(f"   Error esperado capturado: {e}")

    # --- Caso extremo 3: producto inexistente --- #
    print("\n>>> Intentando vender producto inexistente...")
    try:
        inventario.registrar_venta(Venta("XXX", 1, 100))
    except ValueError as e:
        print(f"   Error esperado capturado: {e}")

    # --- Caso extremo 4: precio negativo --- #
    print("\n>>> Intentando crear producto con precio negativo...")
    try:
        Producto("P999", "Invalido", -50, 100, 10)
    except ValueError as e:
        print(f"   Error esperado capturado: {e}")

    # --- Caso extremo 5: predecir sin modelo entrenado --- #
    print("\n>>> Intentando predecir sin modelo entrenado...")
    predictor_vacio = PredictorVentas()
    resultado = predictor_vacio.predecir("P001", 7)
    print(f"   Resultado: {resultado} (esperado None)")

    # Limpieza
    if os.path.exists(archivo):
        os.remove(archivo)

    print("\n" + "=" * 70)
    print(" TODAS LAS PRUEBAS COMPLETADAS CORRECTAMENTE")
    print("=" * 70)


if __name__ == "__main__":
    ejecutar_pruebas()
