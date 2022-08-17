from Logica import Logica
import sys


class Programa:

    @classmethod
    def run(cls):
        opcion = None
        termino = False
        while termino == False:
            print("Bienvenido a Megacable\n1-Opciones disponibles:\n1-Registrar cliente\n2-Buscar cliente\n3-Eliminar cliente\n4-Salir")
            opcion = int(input("Ingrese su opcion: "))
            if opcion == 1:
                Logica.agregarCliente()
            elif opcion == 2:
                Logica.buscarCliente()
            elif opcion == 3:
                Logica.eliminarCliente()
            elif opcion == 4:
                print("Saliendo...")
                termino = True

if __name__ == "__main__":
    Programa.run()
