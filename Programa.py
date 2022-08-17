from Logica import Logica
import sys


class Programa:

    @classmethod
    def run(cls):
        opcion = None
        while opcion != 5:
            print("Bienvenido a Megacable\n1-Opciones disponibles:\n1-Registrar cliente\n2-Buscar cliente\n3-Eliminar cliente\n4-Salir")
            opcion = input("Ingrese su opcion: ")
            if opcion == 1:
                Logica.ingresarCliente()
            elif opcion == 2:
                Logica.buscarCliente()
            elif opcion == 3:
                Logica.eliminarCliente()
            elif opcion == 4:
                print("Saliendo...")
                sys.exit()

