from datetime import datetime


from producto import Producto
from venta import Venta
from inventario import Inventario

   
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
    """ registra un nuevo producto, almacenanandolo en el archivo cvs de productos"""
    print("\n--- Ingrese los datos para registrar un nuevo producto ---")
    try:
        codigo = pedir_numero("Código: ", int, 1000)
        nombre = pedir_texto("Nombre: ")
        categoria = pedir_texto("Categoría: ")
        precio = pedir_numero("Precio de venta: $", float, 0)
        costo = pedir_numero("Costo unitario: $", float, 0)
        stock = pedir_numero("Stock inicial: ", int, 0)

        producto = Producto(codigo, nombre, categoria, precio, costo, stock)
        mi_inventario.registrar_producto(producto)
        print("\n Producto registrado correctamente")
    except (ValueError, TypeError) as e:
        print(f"\n Error: {e}")

def registrar_venta(mi_inventario):
    """ Registra una nueva venta, almacenanandolo  en el archivo cvs de ventas"""
    print("\n--- Ingrese los datos para registrar venta ---")

    mi_inventario.listar_productos() #listamos los productos para ayudar a ver que hay en el almacen
    
    try:
        codigo_proxima_venta = mi_inventario.obtener_codigo_proxima_venta() #obtenemos un numero correlativo, evitamos la carga en el cliente
        codigo_producto = pedir_numero("\nCódigo del producto vendido: ", int, 0)
        producto = mi_inventario.obtener_producto(codigo_producto)
        
        if producto is None:
            print(" Producto no encontrado.")
            return
        
        cantidad = pedir_numero("Cantidad vendida: ", int, 1) #pedimos la cantidad
        precio_referencia = producto.get_precio_venta() #obtenemos precio referencia
        costo_unitario = producto.get_costo_unitario() #obtenemos costo unitario
                
        nvo_precio_venta = pedir_numero(f"Ingrese el precio de venta del producto: valor de referencia es {precio_referencia}: ", float, 0) #pedimos el valor puede ser igual al del produto u otro solo a bases para las predicciones
                
        fecha =  datetime.now().strftime("%d-%m-%Y")#obtenemos la fecha de hoy

        venta = Venta(codigo_proxima_venta, codigo_producto, cantidad, nvo_precio_venta, costo_unitario,  fecha)
        mi_inventario.registrar_venta(venta)
        print("\n Venta registrada con éxito")
    except (ValueError, TypeError) as e:
        print(f"\n Error: {e}")

def  listar_productos_del_inventario(mi_inventario):
    """ Lista todos los productos del inventario. """
    mi_inventario.listar_productos()


def  listar_ventas_historicas(mi_inventario):
    """ Lista todas la ventas historicas del inventario """
    mi_inventario.listar_ventas_historicas()



def analizar_datos_historicos(mi_inventario):
    """ pide el analisis de las ventas historicas al inventario y las muestra por pantalla"""

    analisis = mi_inventario.analizar_datos_historicos()
    
    print("\n--- Resultado del análisis de ventas históricas (Pandas) ---")   

    print(f"Ventas registradas       : {analisis['total_ventas_registradas']}")
    print(f"Unidades totales vendidas: {analisis['total_unidades_vendidas']}")
    print(f"Facturación total        : ${analisis['facturacion_total']:.2f}")
    print(f"Ticket promedio          : ${analisis['ticket_promedio']:.2f}")
    print(f"Ticket mediano           : ${analisis['ticket_mediano']:.2f}")
    print(f"Desv. estándar ticket    : ${analisis['desviacion_estandar_ticket']:.2f}")
    print(f"Primera venta            : {analisis['fecha_primera_venta']}")
    print(f"Última venta             : {analisis['fecha_ultima_venta']}")



def entrenar_modelos(mi_inventario, mi_predicciones):
    """ Entrena modelos basados en la ventas historicas """
    df_ventas = mi_inventario.get_ventas_df_frame()
    if df_ventas.empty:
        print(" No hay ventas registradas para entrenar modelos.")
        return

    """Entrena un modelo por cada producto que haya tenido ventas."""
    resultados_entrenamiento = []
    #codigos = df_ventas["codigo_producto"] # se agrega el unique solo entra una vez el codigo
    codigos = df_ventas["codigo_producto"].unique()
    for codigo in codigos:
        resultado_x_producto = mi_predicciones.entrenar_modelo_producto(codigo, df_ventas)
        resultados_entrenamiento.append(resultado_x_producto)

    return resultados_entrenamiento
    """
    for r in resultados_entrenamiento:
        if r["exito"]:
            m = r["metricas"]
            r2 = f"{m['r2']:.3f}" if m["r2"] is not None else "N/D"
            print(f" [{r['codigo']}] Entrenado "
                    f"(MAE={m['mae']:.2f}, RMSE={m['rmse']:.2f}, R²={r2})")
        else:
            print(f" [{r['codigo']}] {r['mensaje']}")
    """
    

def predecir_ventas(predicciones):
    
    entrenados = predicciones.productos_entrenados()
    if not entrenados:
        print(" Se se puede calcular las predicciones ya que no se han entrebado los modelos para predecir ventas futuras.")
        return None

    codigo_prod_predecir = pedir_numero("Código del producto a predecir: ", int, 1000)
    if codigo_prod_predecir not in entrenados:
        print(" Codigo inexistente o no hay registros de entrenamiento disponibles.")
        return

    dias = pedir_numero("¿Cuántos días a predecir?: ", int, 1)
    prediccion_del_producto = predicciones.predecir_ventas_futuras(codigo_prod_predecir, dias)
    if (prediccion_del_producto is None):
        print(" Error. No se pudo predecir")
        return            

    print(f"\n Predicciones día x día:")
    for i, p in enumerate(prediccion_del_producto, start=1):
        print(f"  Día +{i}: {p:.2f} unidades")
    #print(f"\nTotal estimado en {dias} días: {total:.2f} unidades")


def opcion_stock_y_ganancias(mi_inventario, mi_predicciones):
    """ Calcula el stock recomendado y ganancia estimada para cada producto del modelo entrenado, en un periodo estimado de 30 dias futuros."""
    print("\n--- Stock recomendado y ganancias estimadas ---")

    modelos_entrenados = mi_predicciones.productos_entrenados()
    if not modelos_entrenados:
        print(" No hay modelos entrenados. Primero entrene los modelos (opción 4).")
        return

    # Encabezado de la tabla
    print(f"\n{'Código':<10}{'Nombre':<22} {'Demanda.Esperada':>10} {'StockRec':>10} {'Ganancia$':>14}")
    print("-" * 86)
    dias_futuros = 30
    for codigo in modelos_entrenados:
        producto = mi_inventario.obtener_producto(codigo)
        if producto is None: #chequemos que exita el producto, a los fones de imprimir los datos del mismos
            continue

        prediccion_del_producto = mi_predicciones.predecir_ventas_futuras(codigo,  dias_futuros)
        if prediccion_del_producto is None:
            continue

        demanda_estimada  = float(sum(prediccion_del_producto))       # unidades que se venderán       
        ganancia_estimada = demanda_estimada * producto.ganancia_unitaria() # ganancias  que se obtendria de la demanda estimad

        print(f"{producto.get_codigo_producto():<10}"
              f"{producto.nombre[:20]:<22}"
              f"{demanda_estimada:>10.2f}"            
              f"{ganancia_estimada:>14.2f}")

def opcion_ver_metricas(mi_predicciones):
    print("\n--- Métricas de modelos entrenados ---")
    modelos_entrenados = mi_predicciones.productos_entrenados()
    if not modelos_entrenados:
        print(" No hay modelos entrenados.")
        return
    for codigo in modelos_entrenados:
        m = mi_predicciones.obtener_metricas(codigo)
        r2 = f"{m['r2']:.3f}" if m["r2"] is not None else "N/D"
        print(f"\nProducto {codigo}")
        print(f"  MAE                 : {m['mae']:.3f}")
        print(f"  RMSE                : {m['rmse']:.3f}")
        print(f"  R²                  : {r2}")
        print(f"  Coeficiente         : {m['coeficiente']:.3f}")
        print(f"  Intercepto          : {m['intercepto']:.3f}")
        print(f"  Muestras train/test :  {m['muestras_entrenamiento']}/{m['muestras_prueba']}")

    