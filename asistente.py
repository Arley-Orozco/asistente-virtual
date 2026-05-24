# Mi asistente virtual - Dia 5
nombre = "Arley"

# Lista de tareas del dia
tareas = ["Revisar correos", "Reunion 10am", "Almuerzo", "Ejercicio"]
print("Hola " + nombre + "! Tus tareas de hoy son:")
print("---------------------------------")

#Bucle muestra cada tarea automaticamente
for tarea  in tareas:
  print("- " + tarea)

print("--------------------------------")
print("Total de tareas: " + str(len(tareas)))

