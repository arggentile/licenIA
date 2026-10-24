from datetime import datetime

from producto import Producto
from venta import Venta
from inventario import Inventario
# from predictor import PredictorVentas


def copiar_archivos_base():

    
def pedir_texto(mensaje):
    valor = input(mensaje).strip()
    while not valor:
        print("  >> El campo no puede estar vacío.")
        valor = input(mensaje).strip()
    return valor

   
def pedir_numero(mensaje, tipo=float, minimo=None):
    while True:
        try:
            valor = tipo(input(mensaje).strip())
            if minimo is not None and valor < minimo:
                print(f"  >> Debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("  >> Valor numérico inválido. Intente de nuevo.")

   
def registrar_producto(mi_inventario):
    print("\n--- Ingrese los datos para un nuevo producto ---")
    try:
        codigo = pedir_numero("Código: ", int, 1000)
        nombre = pedir_texto("Nombre: ")
        categoria = pedir_texto("Categoría: ")
        precio = pedir_numero("Precio de venta: $", float, 0)
        costo = pedir_numero("Costo unitario: $", float, 0)
        stock = pedir_numero("Stock inicial: ", int, 0)

        producto = Producto(codigo, nombre, categoria, precio, costo, stock)
        mi_inventario.registrar_producto(producto)
        print(f"\n Producto registrado correctamente: {producto}")
    except (ValueError, TypeError) as e:
        print(f"\n Error: {e}")

def registrar_venta(mi_inventario):
    print("\n--- Ingrese los datos para registrar venta ---")
    mi_inventario.listar_productos()
    
    try:
        codigo_proxima_venta = mi_inventario.obtener_codigo_proxima_venta()
        codigo_producto = pedir_numero("\nCódigo del producto vendido: ", int, 0)
        producto = mi_inventario.obtener_producto(codigo_producto)
        
        if producto is None:
            print(" Producto no encontrado.")
            return
        print(f"El producto es: {producto.info()}")   
        cantidad = pedir_numero("Cantidad vendida: ", int, 1) #pedimos la cantidad
        precio_referencia = producto.get_precio_venta() #obtenemos precio referencia
        costo_unitario = producto.get_costo_unitario() #obtenemos costo unitario
                
        precio_nvo_venta = pedir_numero(f"Ingrese el precio de venta del producto: valor de referencia es {precio_referencia}: ", float, 0) #pedimos el valor puede ser igual al del produto u otro solo a bases para las predicciones
                
        fecha =  datetime.now().strftime("%d-%m-%Y")#obtenemos la fecha de hoy

        venta = Venta(codigo_proxima_venta, codigo_producto, cantidad, precio_nvo_venta, costo_unitario,  fecha)
        mi_inventario.registrar_venta(venta)
        print("\n Venta registrada")
    except (ValueError, TypeError) as e:
        print(f"\n Error: {e}")

def  listar_productos_inventario(mi_inventario):
    # Lsia todos los productos del inventario.
    mi_inventario.listar_productos()


def  listar_ventas_historicas(mi_inventario):
    # Lsia todos los productos del inventario.
    mi_inventario.listar_ventas_historicas()



def analizar_datos_historicos(mi_inventario):
    mi_inventario.analizar_datos_historicos()
    print("\n--- Análisis de ventas históricas (Pandas) ---")
   

    print(f"Ventas registradas       : {resumen['total_ventas_registradas']}")
    print(f"Unidades totales vendidas: {resumen['total_unidades_vendidas']}")
    print(f"Facturación total        : ${resumen['facturacion_total']:.2f}")
    print(f"Ticket promedio          : ${resumen['ticket_promedio']:.2f}")
    print(f"Ticket mediano           : ${resumen['ticket_mediano']:.2f}")
    print(f"Desv. estándar ticket    : ${resumen['desviacion_estandar_ticket']:.2f}")
    print(f"Primera venta            : {resumen['fecha_primera_venta']}")
    print(f"Última venta             : {resumen['fecha_ultima_venta']}")

    print("\n>> Ventas por producto:")
    print(resumen["ventas_por_producto"].to_string())

    print("\n>> Ventas por mes:")
    print(resumen["ventas_por_mes"].to_string())

"""
    def opcion_entrenar_modelos(self):
        print("\n--- Entrenamiento de modelos de ML ---")
        df_ventas = self._inventario.ventas_a_dataframe()
        if df_ventas.empty:
            print(" No hay ventas registradas para entrenar modelos.")
            return

        resultados = self._predictor.entrenar_todos(df_ventas)
        for r in resultados:
            if r["exito"]:
                m = r["metricas"]
                r2 = f"{m['r2']:.3f}" if m["r2"] is not None else "N/D"
                print(f" [{r['codigo']}] Entrenado "
                      f"(MAE={m['mae']:.2f}, RMSE={m['rmse']:.2f}, R²={r2})")
            else:
                print(f" [{r['codigo']}] {r['mensaje']}")

    def opcion_predecir_ventas(self):
        print("\n--- Predicción de ventas futuras ---")
        entrenados = self._predictor.productos_entrenados()
        if not entrenados:
            print(" No hay modelos entrenados. Elija primero la opción 4.")
            return

        print(f"Modelos entrenados: {', '.join(entrenados)}")
        codigo = self._pedir_texto("Código del producto a predecir: ")
        if codigo.upper() not in entrenados:
            print(" No existe modelo entrenado para ese producto.")
            return

        dias = self._pedir_numero("¿Cuántos días predecir?: ", int, 1)
        predicciones = self._predictor.predecir(codigo, dias)
        total = self._predictor.predecir_total(codigo, dias)

        print(f"\nPredicciones día a día (unidades):")
        for i, p in enumerate(predicciones, start=1):
            print(f"  Día +{i}: {p:.2f} unidades")
        print(f"\nTotal estimado en {dias} días: {total:.2f} unidades")

    def opcion_stock_y_ganancias(self):
        print("\n--- Stock recomendado y ganancias estimadas ---")
        entrenados = self._predictor.productos_entrenados()
        if not entrenados:
            print(" No hay modelos entrenados. Elija primero la opción 4.")
            return

        dias = self._pedir_numero(
            "Horizonte de planificación (días): ", int, 1
        )
        factor_seguridad = self._pedir_numero(
            "Factor de seguridad (ej. 1.2 = 20% extra): ", float, 1.0
        )

        print(f"\n{'Código':<10}{'Nombre':<22}{'Dem.Esp':>10}"
              f"{'StockRec':>10}{'StockAct':>10}{'ReponerU':>10}{'Ganancia$':>12}")
        print("-" * 84)

        for codigo in entrenados:
            producto = self._inventario.obtener_producto(codigo)
            if producto is None:
                continue
            demanda = self._predictor.predecir_total(codigo, dias)
            stock_recomendado = int(demanda * factor_seguridad) + 1
            reponer = max(stock_recomendado - producto.stock_actual, 0)
            ganancia_estimada = demanda * producto.ganancia_unitaria()

            print(f"{producto.codigo:<10}{producto.nombre[:20]:<22}"
                  f"{demanda:>10.2f}{stock_recomendado:>10d}"
                  f"{producto.stock_actual:>10d}{reponer:>10d}"
                  f"{ganancia_estimada:>12.2f}")

    def opcion_ver_metricas(self):
        print("\n--- Métricas de modelos entrenados ---")
        entrenados = self._predictor.productos_entrenados()
        if not entrenados:
            print(" No hay modelos entrenados.")
            return
        for codigo in entrenados:
            m = self._predictor.obtener_metricas(codigo)
            r2 = f"{m['r2']:.3f}" if m["r2"] is not None else "N/D"
            print(f"\nProducto {codigo}")
            print(f"  MAE                 : {m['mae']:.3f}")
            print(f"  RMSE                : {m['rmse']:.3f}")
            print(f"  R²                  : {r2}")
            print(f"  Coeficiente         : {m['coeficiente']:.3f}")
            print(f"  Intercepto          : {m['intercepto']:.3f}")
            print(f"  Muestras train/test : "
                  f"{m['muestras_entrenamiento']}/{m['muestras_prueba']}")

    def opcion_listar_productos(self):
        print("\n--- Catálogo de productos ---")
        productos = self._inventario.listar_productos()
        if not productos:
            print(" No hay productos cargados.")
            return
        for p in productos:
            print(f"  {p} | Ganancia unit: ${p.ganancia_unitaria():.2f} "
                  f"| Margen: {p.margen_porcentaje():.1f}%")

    # ------------------- Bucle principal ------------------- #
    """