# Lista para almacenar contactos (cada contacto es un diccionario)
agenda = []


def mostrar_menu():
  print("\n--- AGENDA DE CONTACTOS ---")
  print("1. Agregar contacto")
  print("2. Ver todos los contactos")
  print("3. Buscar contacto")
  print("4. Salir")


def agregar_contacto():
  nombre = input("Ingresa el nombre: ")
  telefono = input("Ingresa el teléfono: ")
  # Creamos un diccionario con los datos
  contacto = {"nombre": nombre, "telefono": telefono}
  agenda.append(contacto)
  print(f"¡Contacto '{nombre}' agregado con éxito!")


def ver_contactos():
  if not agenda:
    print("La agenda está vacía.")
    return

  print("\nLista de contactos:")
  for i, contacto in enumerate(agenda, start=1):
    print(f"{i}. Nombre: {contacto['nombre']} | Teléfono: {contacto['telefono']}")


def buscar_contacto():
  nombre_buscar = input("¿Qué nombre deseas buscar?: ").lower()
  encontrados = [
      c
      for c in agenda
      if nombre_buscar in c["nombre"].lower()
  ]  # Comprensión de listas

  if encontrados:
    print("\nResultados de la búsqueda:")
    for c in encontrados:
      print(f"- Nombre: {c['nombre']} | Teléfono: {c['telefono']}")
  else:
      print("No se encontró ningún contacto con ese nombre.")


# Bucle principal del programa
while True:
  mostrar_menu()
  opcion = input("Elige una opción (1-4): ")

  if opcion == "1":
    agregar_contacto()
  elif opcion == "2":
    ver_contactos()
  elif opcion == "3":
    buscar_contacto()
  elif opcion == "4":
    print("Saliendo de la agenda. ¡Hasta luego!")
    break
  else:
    print("Opción inválida. Por favor, elige un número del 1 al 4.")
