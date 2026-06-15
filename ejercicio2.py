#Ejercicio 2

ingresos = [
    [10000, 15000, 20000], #vendedor 1
    [10000, 15000, 10000], #vendedor 2
    [5000, 10000, 5000]    #vendedor 3
]

totales =[]

print(f"Vendedor 1: {ingresos[0]} Vendedor 2: {ingresos[1]} Vendedor 3: {ingresos[2]}")

for vendedor in ingresos:
    total = sum(vendedor)
    totales.append(total)
mayor_vendedor = max(totales)
print(f"El mayor vendedor fue el 1 con: {mayor_vendedor}")
print(f"Total de ventas: {totales}")

if total <30000:
    print("Hay un vendedor con ingreso menor a $30000")