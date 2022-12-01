class Persona:
    "Clase que construye persona"

    def __init__(self, dni, nombres, apellido_paterno,apellido_materno, direccion, telefono):
        self.dni = dni
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.direccion = direccion
        self.telefono = telefono
        print(self.convertir_a_string())

    def convertir_a_string(self):
        #return print("| {} | {} | {} | {} | {} | {} |".format(self.dni, self.nombres, self.apellido_paterno,self.apellido_materno, self.apellido_materno, self.direccion, self.telefono))
        return print(" | " ,self.dni," | " ,self.nombres," | " )       

#   varnombre : str(input("ingrese nombre"))
#   print( self.dni,"   |    ", self.nombres)