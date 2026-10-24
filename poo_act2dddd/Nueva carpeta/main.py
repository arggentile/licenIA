"""
Módulo: main.py
Descripción: Punto de entrada del Sistema de Gestión de Inventario con
Predicción de Ventas. Instancia el menú interactivo y lo ejecuta.

Autor     : Alumno/a
Materia   : Programación para Inteligencia Artificial
Fecha     : 2026-10-19
"""

from menu import MenuInteractivo


def main():
    """Función principal: inicia la aplicación."""
    try:
        menu = MenuInteractivo()
        menu.ejecutar()
    except KeyboardInterrupt:
        print("\n\nInterrumpido por el usuario. Saliendo...")


if __name__ == "__main__":
    main()
