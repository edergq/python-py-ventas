from producto import Producto

class Comprobante:
    "Clase que construye venta"
listaProductos: Producto= []

def __init__(self, cliente, direccion, importetotal, fecha, numerofactura):
        
        self.cliente = cliente        
        self.direccion = direccion        
        self.importetotal = importetotal
        self.fecha = fecha
        self.numerofactura = numerofactura
        print(self.convertir_a_cadena())

def convertir_a_cadena(self):        
        return print(" | ",self.cliente," | ", self.direccion," | ", self.importetotal," | ", self.fecha," | ", self.numerofactura )
   