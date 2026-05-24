# Mi asistente virtual - Dia 4
nombre = "Arley"
edad = 36
hora = 8

# El asiste decide el saludo segun la hora
if hora < 12:
  print("Buenos dias " + nombre + "!")
elif hora <18:
  print("Buenas tardes " + nombre + "!")
else:
  print("Buenas noches " + nombre + "!")

# El asistente decide segun la edad
if edad >=18:
 print("Eres mayor de edad, puedes usar todas las funciones")
else:
  print("Eres menor de edad")
