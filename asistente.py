# Mi asistente virtual - Dia 7

# Funcion 1: Saludar
def saludar(nombre, hora):
    if hora <12:
        print("Buenos dias " + nombre + "!")
    elif hora < 18:
        print("Buenas tardes " + nombre + "!")
    else:
        print("Buenas noches " + nombre + "!")

# Funcion 2: mostrar tareas
def mostrar_tareas(tareas):
    print("Tus tareas para hoy son:")
    print("----------------------------")
    for tarea in tareas:
        print("- " + tarea)
    print("Total: " + str(len(tareas)) + " tareas")

# Dia 7: Pedirle datos al usuario
nombre = input("Hola! Como te llamas? ")
hora = int(input("Que hora es? (solo el numero): "))

saludar(nombre, hora)
tareas = ["Revisar correos", "Reunion 10am", "Almuerzo", "Ejercicio"]
mostrar_tareas(tareas)
