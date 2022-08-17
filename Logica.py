from Cursor import Cursor


class Logica:

    @classmethod
    def __lanzarExcepcion(cls,e):
        print(f"Ocurrio la excepcion: {e}")

    @classmethod
    def agregarCliente(cls):
        datos_cliente = input("Ingrese los datos separados por coma: ").split(",")
        datos_cliente_tupla = tuple(datos_cliente)
        try:
            with Cursor() as cursor:
                sentencia = "INSERT INTO clientes(nombre,apellido,dni) VALUES(%s,%s,%s)"
                cursor.execute(sentencia,datos_cliente_tupla)
                print("Se añadio el cliente")
        except Exception as e:
            Logica.__lanzarExcepcion(e)
    
    @classmethod
    def buscarCliente(cls):
        dni = int(input("Ingrese el DNI del cliente: "))
        dni_tupla = (dni,)
        try:
            with Cursor() as cursor:
                sentencia = "SELECT * FROM clientes WHERE dni=%s"
                cursor.execute(sentencia,dni_tupla)
                print(cursor.fetchone())
        except Exception as e:
            Logica.__lanzarExcepcion(e)
    
    @classmethod
    def eliminarCliente(cls):
        dni = int(input("Ingrese el DNI del cliente: "))
        dni_tupla = (dni,)
        try:
            with Cursor() as cursor:
                sentencia = "DELETE FROM clientes WHERE dni=%s"
                cursor.execute(sentencia,dni_tupla)
                print("Cliente eliminado")
        except Exception as e:
            Logica.__lanzarExcepcion(e)

    