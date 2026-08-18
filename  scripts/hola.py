"""
Tu primer script en Python. ¡Bienvenido!
Ejecútalo con:  docker compose exec python python hola.py
"""

nombre = input("¿Cómo te llamas? ")
print(f"¡Hola, {nombre}! Ya estás programando en Python 🐍")

# Un pequeño ejemplo con listas y bucles
lenguajes = ["Python", "JavaScript", "Rust", "Go"]
print("\nLenguajes populares:")
for i, lang in enumerate(lenguajes, start=1):
    print(f"  {i}. {lang}")
