from funciones import *
from inventario import Inventario


def mostrar_menu(mi_inventario):
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
        print(" 10. Copiar archivos dataset - archivos cargados con datos de prueba")
        print(" S. Salir")
        print("=" * 60)

        opcion = input("Opción: ").strip()
                
        if opcion=="1":
            registrar_producto(mi_inventario)
        elif opcion=="2":
            registrar_venta(mi_inventario)
        elif opcion=="8":
            listar_productos_inventario(mi_inventario)
        elif opcion=="9":
            listar_ventas_historicas(mi_inventario)
        elif opcion=="10":
            copiar_archivos_base()                    
        elif opcion=="S":
            break
      


if __name__ == "__main__":
    try:
        mi_inventario = Inventario()
        mostrar_menu(mi_inventario)
    except KeyboardInterrupt:
        print("\n\nInterrumpido por el usuario. Saliendo...")
