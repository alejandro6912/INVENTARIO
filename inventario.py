# Programa simple de inventario
# Este programa registra un producto con su nombre, precio y cantidad
# Luego calcula el costo total y muestra el resultado en pantalla

# Solicitar el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Solicitar el precio del producto con validación
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except:
        print("Error: debe ingresar un numero valido para el precio.")

# Solicitar la cantidad con validación
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except:
        print("Error: debe ingresar un numero entero para la cantidad.")

# Calcular el costo total multiplicando precio por cantidad
costo_total = precio * cantidad

# Mostrar los resultados en consola
print("\nResultado del inventario:")
print("Producto:", nombre, "| Precio:", precio, "| Cantidad:", cantidad, "| Total:", costo_total)

# Comentario final:
# Este programa solicita el nombre, precio y cantidad de un producto.
# Luego calcula el costo total multiplicando el precio por la cantidad
# y finalmente muestra toda la información en la consola.