import psycopg2

class Conexion:

    base_datos = None

    @classmethod
    def establecerConexion(cls):
        if cls.base_datos == None:
            try:
                cls.base_datos = psycopg2.connect(user="postgres", password="admin",port="5432",host="127.0.0.1",database="Megacable")
                return cls.base_datos
            except Exception as e:
                print(f"Ocurrio la excepcion: {e}")
        else:
            return cls.base_datos