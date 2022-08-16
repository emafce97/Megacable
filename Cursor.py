class Cursor:

    def __init__(self):
        self.conexion = None
        self.cursor = None
    
    def __enter__(self):
        self.conexion = Conexion.establecerConexion()
        self.cursor = self.conexion.cursor()
        return self.cursor
    
    def __exit__(self):
        if exc_val:
            self.conexion.rollback()
        else:
            self.conexon.commit()