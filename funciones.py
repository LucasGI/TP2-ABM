
# Función para cargar listas con la información de películas
def CargarLista(nombrePelicula, codPelicula, stockPelicula, precioPelicula, duracionPelicula):
    # Solicita el nombre de la primera película
    nombre = input("Ingrese una película (0 para salir): ")

    # Bucle principal para cargar películas mientras el usuario no ingrese "0"
    while nombre != "0":
        # Verifica si el nombre ya existe en la lista
        while verificarDuplicado(nombrePelicula, nombre):
            print("La película ya existe. Ingrese otra.")
            nombre = input("Ingrese una película (0 para salir): ")

        if nombre != "0":
            nombrePelicula.append(nombre)
            print("Película agregada con éxito.")

        # Solicita el código de la película
        codPeli = int(input("Ingrese el código de la película: "))

        # Verifica si el código ya existe en la lista
        while verificarDuplicado(codPelicula, codPeli):
            print("El código de la película ya existe. Ingrese otro.")
            codPeli = int(input("Ingrese el código de la película: "))  # Corrige la reasignación del valor
        codPelicula.append(codPeli)
        print("Código de película agregado.")

        # Solicita y agrega el stock, precio y duración
        stock = int(input("Ingrese el stock de la película: "))
        stockPelicula.append(stock)
        print("Stock de película agregado.")

        precio = int(input("Ingrese el precio de la película: "))
        precioPelicula.append(precio)
        print("Precio de película agregado.")

        duracion = int(input("Ingrese la duración de la película en minutos: "))
        duracionPelicula.append(duracion)
        print("Duración de película agregada.")

        # Solicita el nombre de la siguiente película
        nombre = input("Ingrese una película (0 para salir): ")

# Función para mostrar las listas de películas en pantalla
def mostrarLista(nombres, codigos, stocks, precios, duraciones):
    clear()
    for i in range(len(nombres)):
        
        print("Película:", nombres[i])
        print("Código:", codigos[i])
        print("Stock:", stocks[i])
        print("Precio: $", precios[i])
        print("Duración:", duraciones[i])
        print("-" * 30)

# Funcion para actualizar algun valor de una lista
def actualizar(lista, valor, codPelicula, codPeli):
    for i in range(len(lista)):
        if codPelicula[i] == codPeli:
            lista[i] = valor
    return lista

#Funcion para buscar peliculas por nombre o por codigo
def buscarPelicula(nombres, codigos, stocks, precios, duraciones, criterio):

    if criterio == "nombres":
        nombreBuscado = input("Ingrese el nombre de la película exactamente como fue cargado: ")
        i = 0
        while i < len(nombres) and nombres[i] != nombreBuscado:
            i += 1

        if i < len(nombres):
            clear()
            print(i, nombres[i])
            print("\n--- Película encontrada ---")
            print("Nombre:", nombres[i])
            print("Código:", codigos[i])
            print("Stock:", stocks[i])
            print("Precio: $", precios[i])
            print("Duración:", duraciones[i], "min")
            return i
        else:
            print("No se encontró una película con ese nombre.")
            return -1

    elif criterio == "codigos":
        codigoBuscado = input("Ingrese el código de la película (solo números): ")
        codigoBuscado = int(codigoBuscado)
        i = 0
        while i < len(codigos) and codigos[i] != codigoBuscado:
            i += 1

        if i < len(codigos):
            print("\n--- Película encontrada ---")
            print("Nombre:", nombres[i])
            print("Código:", codigos[i])
            print("Stock:", stocks[i])
            print("Precio: $", precios[i])
            print("Duración:", duraciones[i], "min")
            return i
        else:
            print("No se encontró una película con ese código.")
            return -1
    else:
        print("Opcion invalida")

# Funcion para poder ver cuanto es el precio que se espera a ganar si se venden cierta cantidad de stock de una pelicula
def ingresoEsperado(listaPrecio, cantEsperada, codigoPelicula, codPeli):
    for i in range(len(listaPrecio)):
        for i in range(len(codigoPelicula)):
            if codigoPelicula[i] == codPeli:
                valorEsperado = listaPrecio[i] * cantEsperada
    return valorEsperado

# Funcion para ordenar peliculas segun el criterio que se le pase por parametro
def ordenarPeliculas(criterio, nombres, codigos, stocks, precios, duraciones):
    if criterio == "nombre":
        clave = nombres
    elif criterio == "codigo":
        clave = codigos
    elif criterio == "precio":
        clave = precios
    else:
        print("Criterio inválido.")
        return
    for i in range(len(clave) - 1):
        for j in range(len(clave) - i - 1):
            if str(clave[j]).lower() > str(clave[j + 1]).lower():
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                codigos[j], codigos[j + 1] = codigos[j + 1], codigos[j]
                stocks[j], stocks[j + 1] = stocks[j + 1], stocks[j]
                precios[j], precios[j + 1] = precios[j + 1], precios[j]
                duraciones[j], duraciones[j + 1] = duraciones[j + 1], duraciones[j]

# Funcion que hardcodea listas paralelas
def hardcodearPeliculas():
    nombres = ["Shrek", "Matrix", "El Padrino", "Toy Story", "Titanic"]
    codigos = [101, 102, 103, 104, 105]
    stocks = [10, 5, 8, 7, 12]
    precios = [1500, 2000, 1800, 1400, 2200]
    duraciones = [90, 120, 175, 95, 195]
    print("HARDCODEO DE PELICULAS.")
    return nombres, codigos, stocks, precios, duraciones

#Ej de uso calcularEstadisticas(precioPelicula, "Precios") o calcularEstadisticas(duracionPelicula, "Duraciones")
def calcularEstadisticas(lista, nombreCampo):
    if len(lista) == 0:
        print("No hay datos para calcular estadísticas.")
        return

    minimo = lista[0]
    maximo = lista[0]
    suma = 0
    cantidad = 0

    i = 0
    while i < len(lista):
        if lista[i] < minimo:
            minimo = lista[i]
        if lista[i] > maximo:
            maximo = lista[i]
        suma = suma + lista[i]
        cantidad = cantidad + 1
        i = i + 1

    promedio = suma / cantidad
    clear()
    print("\n--- Estadísticas de", nombreCampo, "---")
    print("Cantidad:", cantidad)
    print("Mínimo:", minimo)
    print("Máximo:", maximo)
    print("Promedio:", promedio)

# simula una funcion de clear printeando 50 bajadas de linea
def clear():
    print("\n" * 50)

# Menu principal
def mostrar_menu():
    clear()
    print("\n=== Sistema de Gestión de Películas ===")
    print("1. Ingresar como administrador")
    print("2. Ingresar como cliente")
    print("3. Estadisticas")
    print("4. Salir")


    ingreso = int(input("Ingrese una opcion: "))

    if ingreso != 1 and ingreso != 2 and ingreso != 3 and ingreso != " " :
        print("Opcion Invalida")
        input("presione una tecla ")
    else:
        return ingreso

     #return int(input("Seleccione una opción: "))

# Menu del administrador
def mostrarMenuAdm():
    clear()
    print("\n=== Menú Administrador ===")
    print("1. Cargar películas")
    print("2. Modificar película")
    print("3. Mostrar peliculas")
    print("4. Volver")
    ingreso = int(input("Ingrese una opcion: "))

    if ingreso != 1 and ingreso != 2 and ingreso != 3 and ingreso != 4 and ingreso != " ":
        print("Opcion Invalida")
        input("presione una tecla ")
    else:
        return ingreso

# Menu del cliente
def mostrarMenuCliente():
    clear()
    print("\n=== Menú Mostrar ===")
    print("1. Listar películas por precio")
    print("2. Listar películas por nombre")
    print("3. Listar películas por codigo")
    print("4. Buscar película")
    print("5. Volver")
    ingreso = int(input("Ingrese una opcion: "))

    if ingreso != 1 and ingreso != 2 and ingreso != 3 and ingreso!=4 and ingreso !=5 and ingreso != " ":
        print("Opcion Invalida")
        input("presione una tecla ")
    else:
        return ingreso

#Menu del administrador seccion modificaciones
def mostrarMenuModificar():
    print("\n=== Menú Modificar Película ===")
    print("1. Modificar nombre")
    print("2. Modificar código")
    print("3. Modificar stock")
    print("4. Modificar precio")
    print("5. Modificar duración")
    print("6. Volver")
    ingreso = int(input("Ingrese una opcion: "))

    if ingreso != 1 and ingreso != 2 and ingreso != 3 and ingreso != 4 and ingreso != 5 and ingreso != 6 and ingreso != " ":
        print("Opcion Invalida")
        input("presione una tecla ")
    else:
        return ingreso
    #return int(input("Seleccione una opción: "))

#Menu de mostrar estadisticas
def mostrarMenuEstadisticas():
    clear()
    print("\n=== Menu Estadisticas ===")
    print("1. Estadisticas de precios")
    print("2. Estadisticas de duraciones")
    ingreso = int(input("Ingrese una opcion: "))

    if ingreso != 1 and ingreso != 2 and ingreso != " ":
        print("Opcion Invalida")
        input("presione una tecla ")
    else:
        return ingreso

# Menu de busqueda
def mostrarMenuBuscar():
    clear()
    print("Buscar por:")
    print("1. Nombre")
    print("2. Código")
    print("3. Salir")
    opcion = int(input("Seleccione una opción: "))

    if opcion!=1 and opcion!=2 and opcion!=3 and opcion!=" ":
        print("Opcion invalida")
    else:
        return opcion

# Funcion para logearse, si la contraseña es incorrecta no entrara al menu de administrador
def log_in():
    clear()
    print("\n=== Login ===")

    password = input("Ingrese la contraseña: ")
    while password != "admin123" :
        print("Contraseña incorrecta")
        password = input("Reintentar ")

