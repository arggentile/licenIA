"""
Módulo: menu.py
Descripción: Define la clase MenuInteractivo, que gestiona la interfaz por
consola del sistema de inventario, articulando Inventario y PredictorVentas.
"""

from datetime import datetime

from producto import Producto
from venta import Venta
from inventario import Inventario
from predictor import PredictorVentas


class MenuInteractivo:
    """
    Interfaz por consola que coordina el inventario y el predictor
    de ventas. Centraliza la interacción con el usuario.
    """

    def __init__(self):
        self._inventario = Inventario()
        self._predictor = PredictorVentas()

    # ------------------- Utilidades ------------------- #
    @staticmethod
    def _pedir_texto(mensaje):
        valor = input(mensaje).strip()
        while not valor:
            print("  >> El campo no puede estar vacío.")
            valor = input(mensaje).strip()
        return valor

    @staticmethod
    def _pedir_numero(mensaje, tipo=float, minimo=None):
        while True:
            try:
                valor = tipo(input(mensaje).strip())
                if minimo is not None and valor < minimo:
                    print(f"  >> Debe ser mayor o igual a {minimo}.")
                    continue
                return valor
            except ValueError:
                print("  >> Valor numérico inválido. Intente de nuevo.")

    # ------------------- Opciones del menú ------------------- #
    def opcion_registrar_producto(self):
        print("\n--- Registrar nuevo producto ---")
        try:
            codigo = self._pedir_texto("Código: ")
            nombre = self._pedir_texto("Nombre: ")
            categoria = self._pedir_texto("Categoría: ")
            precio = self._pedir_numero("Precio de venta: $", float, 0)
            costo = self._pedir_numero("Costo unitario: $", float, 0)
            stock = self._pedir_numero("Stock inicial: ", int, 0)

            producto = Producto(codigo, nombre, precio, costo, stock, categoria)
            self._inventario.registrar_producto(producto)
            print(f"\n Producto registrado correctamente: {producto}")
        except (ValueError, TypeError) as e:
            print(f"\n Error: {e}")

    def opcion_registrar_venta(self):
        print("\n--- Registrar venta ---")
        productos = self._inventario.listar_productos()
        if not productos:
            print(" No hay productos cargados.")
            return
        print("Productos disponibles:")
        for p in productos:
            print(f"  {p}")
        try:
            codigo = self._pedir_texto("\nCódigo del producto vendido: ")
            producto = self._inventario.obtener_producto(codigo)
            if producto is None:
                print(" Producto no encontrado.")
                return
            cantidad = self._pedir_numero("Cantidad vendida: ", int, 1)
            precio_default = producto.precio_venta
            usar_precio = input(
                f"¿Precio de venta ${precio_default:.2f}? (ENTER para aceptar, "
                f"o escriba otro): "
            ).strip()
            precio_unitario = float(usar_precio) if usar_precio else precio_default

            fecha_str = input(
                "Fecha (AAAA-MM-DD, ENTER para hoy): "
            ).strip()
            fecha = fecha_str if fecha_str else None

            venta = Venta(codigo, cantidad, precio_unitario, fecha)
            self._inventario.registrar_venta(venta)
            print(f"\n Venta registrada: {venta}")
            print(f" Stock restante del producto: {producto.stock_actual}")
        except (ValueError, TypeError) as e:
            print(f"\n Error: {e}")

    def opcion_analizar_historial(self):
        print("\n--- Análisis de ventas históricas (Pandas) ---")
        resumen = self._inventario.analizar_historial()
        if "mensaje" in resumen:
            print(resumen["mensaje"])
            return

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
    def mostrar_menu(self):
        print("\n" + "=" * 60)
        print(" SISTEMA DE GESTIÓN DE INVENTARIO CON PREDICCIÓN")
        print("=" * 60)
        print(" 1. Registrar nuevo producto")
        print(" 2. Registrar venta")
        print(" 3. Analizar datos históricos (Pandas)")
        print(" 4. Entrenar modelos de machine learning")
        print(" 5. Predecir ventas futuras")
        print(" 6. Stock recomendado y ganancias estimadas")
        print(" 7. Ver métricas de modelos entrenados")
        print(" 8. Listar productos del catálogo")
        print(" 0. Salir")
        print("=" * 60)

    def ejecutar(self):
        acciones = {
            "1": self.opcion_registrar_producto,
            "2": self.opcion_registrar_venta,
            "3": self.opcion_analizar_historial,
            "4": self.opcion_entrenar_modelos,
            "5": self.opcion_predecir_ventas,
            "6": self.opcion_stock_y_ganancias,
            "7": self.opcion_ver_metricas,
            "8": self.opcion_listar_productos,
        }
        while True:
            self.mostrar_menu()
            opcion = input("Opción: ").strip()
            if opcion == "0":
                print("\nSaliendo del sistema. ¡Hasta luego!")
                break
            accion = acciones.get(opcion)
            if accion is None:
                print(" Opción inválida.")
            else:
                accion()
