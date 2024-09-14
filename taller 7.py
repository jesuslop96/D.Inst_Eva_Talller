def obtener_calificacion(num):
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación {num} (entre 1.0 y 5.0): "))
            if 1.0 <= calificacion <= 5.0:
                return calificacion
            else:
                print("La calificación debe estar entre 1.0 y 5.0. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número decimal.")

calificacion1 = obtener_calificacion(1)
calificacion2 = obtener_calificacion(2)
calificacion3 = obtener_calificacion(3)
calificacion4 = obtener_calificacion(4)
calificacion5 = obtener_calificacion(5)

Taller1 = 0.20
Taller2 = 0.15
Cuest1 = 0.22
Cuest2 = 0.10
Proyectfinal = 0.33

Notafinal = (calificacion1 * Taller1) + (calificacion2 * Taller2) + (calificacion3 * Cuest1) + (calificacion4 * Cuest2) + (calificacion5 * Proyectfinal)
print(f"Tu nota definitiva es:", round(Notafinal,2))

