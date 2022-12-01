from producto import Producto

lista_productos: Producto = []

def registrar_producto():
    codigo: str = str(input("Ingrese Codigo: "))
    nombres: str = str(input("Ingrese Nombres de Producto: "))
    precio: float = float(input("Ingrese precio: "))    
    produc : Producto = Producto(codigo, nombres, precio)
    lista_productos.append(produc)

def reporte_productos():    
    for prod in lista_productos:
        Producto.convertir_a_cadena(prod)

def buscar_producto():
    codigo: str = str(input("Ingrese CODIGO para buscar: "))
    for prod in lista_productos:
        if prod.codigo == codigo:
            Producto.convertir_a_cadena(prod)

def editar_producto():
    codigo: str = str(input("Ingrese CODIGO para Editar: "))
    for articulos in lista_productos:
        if articulos.codigo == codigo:
            articulos.nombres = str(input("Ingrese un nuevo nombre: "))

def eliminar_producto():
    codigo: str = str(input("Ingrese DNI para Eliminar: "))
    for index, producto in enumerate(lista_productos):
        if producto.codigo == codigo:
            lista_productos.pop(index)


def main():
    continuar: bool = True
    while continuar:        
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print("       1: PARA AGREGAR PRODUCTO")
        print("       2: PARA LISTAR PRODUCTO")        
        print("       3: PARA BUSCAR PRODUCTO")        
        print("       4: PARA EDITAR PRODUCTO")        
        print("       5: PARA ACTUALIZAR PRODUCTO")        
        print("       10: PARA SALIR")
        caso: str = str(input("INGRESE OPCIÓN: "))
        match caso:
            case "1":
                registrar_producto()
            case "2":
                reporte_productos()            
            case "3":
                buscar_producto()
            case "4":
                editar_producto()
            case "5":
                eliminar_producto()
            case "10":
                continuar = False


if __name__ == '__main__':
    main()
