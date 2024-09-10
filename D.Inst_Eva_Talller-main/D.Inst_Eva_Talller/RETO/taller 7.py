calificacion1 = float(input("Ingrese la primera calificación:"))
calificacion2 = float(input("Ingrese la segunda calificación:"))
calificacion3 = float(input("Ingrese la tercera calificación:"))
calificacion4 = float(input("Ingrese la cuarta calificación:"))
calificacion5 = float(input("Ingrese la quinta calificación:"))

Taller1 = 0.20
Taller2 = 0.15
Cuest1 = 0.22
Cuest2 = 0.10
Proyectfinal = 0.33

Notafinal = (calificacion1 * Taller1) + (calificacion2 * Taller2) + (calificacion3 * Cuest1) + (calificacion4 * Cuest2) + (calificacion5 * Proyectfinal)
print(f"Tu nota definitiva es:", round(Notafinal,2))
