# Mi asistente virtual - Dia 6

# Funcion 1: Saludar
def saludar(nombre, hora):
    if hora < 12:
        print("Buenos dias " + nombre + "!")
    elif hora < 18:
        print("Buenas tardes " + nombre + "!")
    else:
        print("Buenas noches " + nombre + "!")

# Funcion 2: mostrar tareas
def mostrar_tareas(tareas):
    print("Tus tareas para hoy son:")
    print("------------------------------")
    for tarea in tareas:
        print("- " + tarea)
    print("Total: " + str(len(tareas)) + " tareas")

# Usando las funciones
saludar("Arley", 9)
tareas = ["Revisar correos", "Reunion 10am", "Almuerzo", "Ejercicio"]
mostrar_tareas(tareas)
