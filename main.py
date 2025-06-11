from funciones import *

def main():

    nombres, codigos, stocks, precios, duraciones = hardcodearPeliculas()
    flagSeguir = 1



    while flagSeguir == 1:
        opcion = mostrar_menu()

        # Opcion 1, ingresa como administrador
        if opcion == 1:
            flagSalirAdm = 0
            #log_in()
            while flagSalirAdm == 0:
                opcionAdm = mostrarMenuAdm()
                # Opcion 1, Cargar Pelicula
                if opcionAdm == 1:
                    CargarLista(nombres, codigos, stocks, precios, duraciones)
                # Opcion 2, Actualizar Pelicula
                elif opcionAdm == 2:
                    codPeli = int(input("Ingrese el código de la película a modificar: "))
                    existe, pos = verificarDuplicado(codigos, codPeli)
                    if not existe:
                        print("Código no encontrado.")
                        input("Presione una tecla para continuar...")
                    else:
                        flagMod = 0
                        while flagMod == 0:
                            opcionMod = mostrarMenuModificar()
                            if opcionMod == 1:
                                nuevoNombre = input("Ingrese el nuevo nombre: ")
                                nombres = actualizar(nombres, nuevoNombre, codigos, codPeli)
                            elif opcionMod == 2:
                                nuevoCodigo = int(input("Ingrese el nuevo código: "))
                                codigos = actualizar(codigos, nuevoCodigo, codigos, codPeli)
                            elif opcionMod == 3:
                                nuevoStock = int(input("Ingrese el nuevo stock: "))
                                stocks = actualizar(stocks, nuevoStock, codigos, codPeli)
                            elif opcionMod == 4:
                                nuevoPrecio = int(input("Ingrese el nuevo precio: "))
                                precios = actualizar(precios, nuevoPrecio, codigos, codPeli)
                            elif opcionMod == 5:
                                nuevaDuracion = int(input("Ingrese la nueva duración: "))
                                duraciones = actualizar(duraciones, nuevaDuracion, codigos, codPeli)
                            elif opcionMod == 6:
                                flagMod = 1
                            else:
                                print("Opción inválida.")
                # Opcion 3, Mostrar peliculas, abre el menu cliente, ya que solo puede ver y no modificar
                elif opcionAdm == 3:
                    opcionMostrar = mostrarMenuCliente()
                    if opcionMostrar == 1:
                        ordenarPeliculas("precio", nombres, codigos, stocks, precios, duraciones)
                        mostrarLista(nombres, codigos, stocks, precios, duraciones)
                        input("Presione una tecla para continuar...")
                    elif opcionMostrar == 2:
                        ordenarPeliculas("nombre", nombres, codigos, stocks, precios, duraciones)
                        mostrarLista(nombres, codigos, stocks, precios, duraciones)
                        input("Presione una tecla para continuar...")
                    elif opcionMostrar == 3:
                        ordenarPeliculas("codigo", nombres, codigos, stocks, precios, duraciones)
                        mostrarLista(nombres, codigos, stocks, precios, duraciones)
                        input("Presione una tecla para continuar...")
                    elif opcionMostrar == 4:
                        buscado = input("Ingrese el nombre a buscar: ")
                        estado, posicion = verificarDuplicado(nombres, buscado)
                        if estado == True:
                            print("Nombre   Codigo   Stock   Precio   Duracion")
                            print(nombres[posicion], "  ", codigos[posicion], "   ", stocks[posicion], "    ", precios[posicion], "   ", duraciones[posicion])
                        else:
                            print("Película no encontrada.")
                        input("Presione una tecla para continuar...")
                    # Opcion 5, Salir
                    elif opcionMostrar == 5:
                        flagSalirAdm = 1
                    # Cualquier otro ingreso sera invalido
                    else:
                        print("Opción inválida")
                # Opcion 4, Salir
                elif opcionAdm == 4:
                    flagSalirAdm = 1

                else:
                    print("Opción inválida")
                    input("Presione cualquier tecla para continuar...")

        #Opcion 2, ingresa como cliente
        elif opcion == 2:
            flagSalirCliente = 0
            while flagSalirCliente == 0:
                opcionCliente = mostrarMenuCliente()
                # Listar peliculas por precio
                if opcionCliente == 1:
                    ordenarPeliculas("precio", nombres, codigos, stocks, precios, duraciones)
                    mostrarLista(nombres, codigos, stocks, precios, duraciones)
                    input("Presione una tecla para continuar...")
                # Listar peliculas por nombre
                elif opcionCliente == 2:
                    ordenarPeliculas("nombre", nombres, codigos, stocks, precios, duraciones)
                    mostrarLista(nombres, codigos, stocks, precios, duraciones)
                    input("Presione una tecla para continuar...")
                # Listar peliculas por codigo
                elif opcionCliente == 3:
                    ordenarPeliculas("codigo", nombres, codigos, stocks, precios, duraciones)
                    mostrarLista(nombres, codigos, stocks, precios, duraciones)
                    input("Presione una tecla para continuar...")
                # Buscar pelicula
                elif opcionCliente == 4:
                    buscado = input("Ingrese el nombre a buscar: ")
                    estado, posicion = verificarDuplicado(nombres, buscado)
                    if estado == True:
                        print("Nombre   Codigo   Stock   Precio   Duracion")
                        print(nombres[posicion],"  ", codigos[posicion],"   ", stocks[posicion], "    ",precios[posicion],"   ", duraciones[posicion])
                    else:
                        print("Película no encontrada.")
                    input("Presione una tecla para continuar...")
                # Salir
                elif opcionCliente == 5:
                    flagSalirCliente = 1
                else:
                    print("Opción inválida")
        # Opcion 3, Sale del bucle principal
        elif opcion == 3:
            print("Saliendo del sistema...")
            flagSeguir = 0
        # Cualquier otra opcion es invalida
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()