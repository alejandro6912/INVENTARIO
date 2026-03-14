# inventario.py

# Programa de inventario sencillo
# Permite registrar un producto con su precio y cantidad,
# calcula el costo total y lo muestra en pantalla.

# --- Entrada de datos ---
# Nombre del producto
producto = input("Nombre del producto: ")

# Precio del producto (validación con bucle)
precio_valido = False
while not precio_valido:
    entrada = input("Precio unitario: ")
    try:
        precio = float(entrada)
        precio_valido = True
    except ValueError:
        print("Entrada inválida. Ingrese un número decimal.")

# Cantidad del producto (validación con bucle)
cantidad_valida = False
while not cantidad_valida:
    entrada = input("Cantidad: ")
    try:
        cantidad = int(entrada)
        cantidad_valida = True
    except ValueError:
        print("Entrada inválida. Ingrese un número entero.")

# --- Operación matemática ---
# Se calcula el costo total multiplicando precio por cantidad
costo_total = precio * cantidad

# --- Salida de resultados ---
# Se muestra la información en un formato claro y ordenado
print("Producto:", producto,
      "| Precio:", f"{precio:.2f}",
      "| Cantidad:", cantidad,
      "| Total:", f"{costo_total:.2f}")

# --- Comentario final ---
# Este script solicita datos de un producto, valida que sean correctos,
# calcula el costo total y presenta la información de manera legible.