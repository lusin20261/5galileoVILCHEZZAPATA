print("===========$BIENVENIDO A MI TIENDA$===========")
vendedor = input("INGRESA EL NOMBRE DEL VENDEDOR: ")
comprador = input("INGRESA EL NOMBRE DEL COMPRADOR: ")
producto = input("INGRESA EL NOMBRE DEL PRODUCTO: ")

print("productoA")
precio = input("ingresa el precio del productoA: ")
precio = int(precio)
cantidad = input("Ingrese la cantidad del productoA: ")
cantidad = int(cantidad)


print("productoB")
precio = input("ingresa el precio del productoB: ")
precio = int(precio)
cantidad = input("ingrese la cantidad del productoB: ")
cantidad = int(cantidad)


print("productoI")
precio = input("ingresa el precio del productoI: ")
precio = int(precio)
cantidad = input("ingrese la cantidad del productoI: ")
cantidad = int(cantidad)


print("productoX")
precio = input("ingrese el precio del productoX: ")
precio = int(precio)
cantidad = input("ingrese la cantidad del productoX: ")
cantidad = int(cantidad)

print("==========================")
print("$BIENBENIDO A MI TIENDA$ :D")
print("Boleta de venta")
print("==========================")

print("")
print("VENDEDOR:",vendedor)
print("COMPRADOR:",comprador)
print("")
print("Precio:",precio)
print("cantidad:",cantidad)


print("TOTAL DE PAGAR: $/.",cantidad*precio)
print("")
print(" =======?====GRACIAS POR TU COMPRA====?======")