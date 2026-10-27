from funciones import *
from inventario import Inventario
from predicciones import Predicciones


def mostrar_menu(mi_inventario, mi_predicciones):
    while True:
        print("\n" + "=" * 60)
        print(" Ingrese una opción valida")
        print("=" * 60)
        print(" 1. Registrar nuevo producto")
        print(" 2. Registrar venta")
        print(" 3. Analizar datos históricos (Pandas)")
        print(" 4. Entrenar modelos de machine learning")
        print(" 5. Predecir ventas futuras")
        print(" 6. Stock recomendado y ganancias estimadas")
        print(" 7. Ver métricas de modelos entrenados")
        print(" 8. Listar productos del catálogo")
        print(" 9. Listar Ventas historicas")
        print(" S. Salir")
        print("=" * 60)

        opcion = input("Opción: ").strip().upper()
        try:                
            if opcion=="1":
                registrar_producto(mi_inventario)
            elif opcion=="2":
                registrar_venta(mi_inventario)
            elif opcion=="3":
                analizar_datos_historicos(mi_inventario)
            elif opcion=="4":
                entrenar_modelos(mi_inventario, mi_predicciones)
            elif opcion=="5":
                predecir_ventas(mi_predicciones)
            elif opcion=="6":
                stock_y_ganancias(mi_inventario, mi_predicciones)
            elif opcion=="7":
                ver_metricas(mi_predicciones)               
            elif opcion=="8":
                listar_productos_del_inventario(mi_inventario)
            elif opcion=="9":
                listar_ventas_historicas(mi_inventario)
            elif opcion=="S":
                break
            else:
                print("Opción inválida. Intente nuevamente.")
        except (ValueError, KeyError, TypeError) as e:    
            print(f"\n >> Error al procesar la opción: {e}")
        except Exception as e:                 
            print(f"\n >> Error inesperado: {e}")


if __name__ == "__main__":
    try:
        mi_inventario = Inventario()
        mi_predicciones = Predicciones()
        mostrar_menu(mi_inventario, mi_predicciones)
    except KeyboardInterrupt:
        print("\n\nInterrumpido por el usuario. Saliendo...")
