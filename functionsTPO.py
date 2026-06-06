def menu ():
    '''muestra el menu y devuelve una opcion valida'''
    print ("1: Registrar nuevo producto")
    print ("2: eliminar producto")
    print ("3: modificar cantidad de stock")
    print ("4: informe general")
    print ("8: finalizar")

    op = int(input("ingrese el numero del procedimiento que desea realizar: "))
    while op > 4 and op < 1 and op == 8:
        op = int(input("porfavor ingrese una opcion valida: "))

    return op

def nuevoproducto():
    '''da de alta un producto nuevo'''

def eliminarproducto():
    '''elimina un producto del sistema'''

def modificacion():
    '''modifica un elemento del sistema'''

def informe():
    '''visualiza todos los datos del sistema'''
