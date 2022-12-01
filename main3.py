from venta import Comprobante

listaComprobantes: Comprobante = []

def registrarVenta():
    
    cliente: str = str(input("Ingrese Cliente: "))
    direccion: str = str(input("Ingrese Direccion: "))
    importetotal: str = str(input("Ingrese Importe: "))
    fecha: str = str(input("Ingrese Fecha: "))
    numerofactura: str = str(input("Ingrese numero factura: ")) 
    venta: Comprobante = Comprobante(  cliente, direccion, importetotal, fecha, numerofactura )
    listaComprobantes.append(venta)

def listar_Comprobantes(): 
    for comp in listaComprobantes:
        Comprobante.convertir_a_cadena(comp)

def buscar_comprobante():
    numero: str = str(input("Ingrese Numero para buscar: "))
    for comprobant in listaComprobantes:
        if comprobant.numero == numero:
            Comprobante.convertir_a_cadena(comprobant)

def actualizarComprobante():
    numero: str = str(input("Ingrese NUMERO para Editar: "))
    for comprobant in listaComprobantes:
        if comprobant.numero == numero:
            comprobant.numero = str(input("Ingrese un nuevo Numero: "))
            comprobant.importetotal = str(input("Ingrese un nuevo importe: "))

def main():
    continuar: bool = True
    while continuar:
        print("*****************************************")
        print("***********SISTEMA DE VENTAS*************")
        print("                                         ")
        print("===================MENÚ==================")
        print("**************INGRESE OPCIONES***********")
        print("       1: PARA REGISTRAR VENTA")
        print("       2: PARA REPORTAR VENTAS")
        print("       3: PARA BUSCAR VENTAS")        
        print("       4: PARA ACTUALIZAR VENTAS")   
        print("       10: PARA SALIR")
        opcion: str = str(input("INGRESE OPCIÓN: "))
        match opcion:
            case "1":
                registrarVenta()
            case "2":
                listar_Comprobantes()
            case "3":
                buscar_comprobante()
            case "4":
                actualizarComprobante()            
            case "10":
                continuar = False

if __name__ == '__main__':
    main()
