class Producto:
    "Clase que construye producto"

    def __init__(self, codigo, nombres, precio):
        self.codigo = codigo
        self.nombres = nombres        
        self.precio = precio        
        print(self.convertir_a_cadena())

    def convertir_a_cadena(self):        
        return print(" | " ,self.codigo," | " ,self.nombres," | ", self.precio )       
   