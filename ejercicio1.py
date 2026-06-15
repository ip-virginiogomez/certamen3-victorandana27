#ejercicio 1

velocidades = []

for i in range(5):
    velocidad = int(input(f"Ingrese la velocidad {i+1} (km/h): "))
    velocidades.append(velocidad)

promedio = sum(velocidades)/ len(velocidades)
velocidad_maxima = max(velocidades)
print(f"Promedio de todas las velocidades: {promedio} km/h")
print(f"La velocidad máxima es de: {velocidad_maxima} km/h")
                      
if velocidad >60 and velocidad <120:
    print("Todas las velocidades están dentro del límite")
else:
    print("Hay velocidades fuera del límite permitido")

if velocidad >20 and velocidad <140:
    print("Advertencia: Se detectó una velocidad muy peligrosa")