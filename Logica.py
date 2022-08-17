from Cursor import Cursor


class Logica:

    @classmethod
    def __lanzarExcepcion(cls,e):
        print(f"Ocurrio la excepcion: {e}")

    @classmethod
    def agregarCliente(self):
        datos_cliente = (input("Ingrese los datos separados por coma: ").split(","),)
        try:
            with Cursor() as cursor:
                sentencia = "INSERT INTO clientes(nombre,apellido,dni) VALUES(%s,%s,%s)"
                cursor.execute(sentencia,datos_cliente)
                print("Se añadio el cliente")
        except Exception as e:
            Logica.__lanzarExcepcion(e)

    