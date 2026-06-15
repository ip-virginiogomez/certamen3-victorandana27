
#EJERCICIO 3

edad = int(input("Ingrese su edad: "))
tarjeta = input("¿Tiene tarjeta de socio? si/no: ")
compra = float(input("Ingrese el monto total de su compra: "))

if compra > 10000 and (edad > 60 or tarjeta == "si"):
    descuento = (compra * 0.15)
    total_final = (compra - descuento)

    print("Obtiene un descuento del 15%")
    print(f"Descuento: ${descuento}")
    print(f"Total a pagar: ${total_final}")
else:
    print("No aplica para el descuento")
    print(f"Total a pagar: ${compra}")
