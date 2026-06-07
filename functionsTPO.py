def menu ():
    '''muestra el menu y devuelve una opcion valida'''
    print ("1: Registrar nuevo producto")
    print ("2: eliminar producto")
    print ("3: modificar cantidad de stock")
    print ("4: informe general")
    print ("8: finalizar")

    op = int(input("ingrese el numero del procedimiento que desea realizar: "))
    while op > 4 and op < 1 and op != 8:
        op = int(input("porfavor ingrese una opcion valida: "))

    return op

def nuevoproducto(lista_stock,lista_id,lista_desc,lista_cat,lista_precio,Lista_marca):
    id=input("Ingrese el ID del producto:")
    while id in lista_id:
        print("Error este ID ya existe para otro producto.Por favor ingrese otro ID:")
        id = input("Ingrese el ID del producto:")
    descripcion=input("Ingrese la descripcion del producto:")
    categoria=input("Ingrese la cantegoria del producto:")
    precio=float(input("Ingrese el precio del producto:"))
    while precio <0:
        print("Error el precio ingresado no es valido.Por favor ingrese otro precio:")
        precio = float(input("Ingrese el precio del producto:"))
    stock=int(input("Ingrese el stock del producto:"))
    while stock<0:
        print("Error, el stock ingresado no es valido.Por favor ingrese otro:")
        stock = int(input("Ingrese el stock del producto:"))
    marca=input("Ingrese la marca del producto:")
    lista_id.append(id)
    lista_desc.append(descripcion)
    lista_cat.append(categoria)
    lista_precio.append(precio)
    lista_stock.append(stock)
    Lista_marca.append(marca)
    return lista_stock,lista_id,lista_desc,lista_cat,lista_precio,Lista_marca
    '''da de alta un producto nuevo'''

def eliminar_producto(lista_stock,lista_id,lista_desc,lista_cat,lista_precio,lista_marca):
    '''Elimina un producto según su identificador'''
    busqueda = input("Ingrese el identificador del producto que desea eliminar: ")
    posicion = 0
    for i in range(len(lista_id)):       
        if lista_id[i] == busqueda:
            posicion = i
    if lista_id[posicion] == busqueda:      
        print("Se encontró el producto: ",lista_desc[posicion],"\n")        
        if lista_stock[posicion] == 0:            
            confirmar = str(input("¿Está seguro que desea eliminar el producto seleccionado?\n¿Si o No?")).upper()
            if confirmar == "SI" or confirmar == "SÍ":
                lista_id.pop(posicion)
                lista_stock.pop(posicion)
                lista_desc.pop(posicion)
                lista_cat.pop(posicion)
                lista_precio.pop(posicion)
                lista_marca.pop(posicion)
                print("El producto ha sido eliminado correctamente.")                
            elif confirmar == "NO":
                print("El producto no fue eliminado.")       
        else:
            
            print("El producto encontrado, no puede ser eliminado porque aún tiene stock.")    
    else:

        print("No se encontró el identificador de producto ingresado.")

def modificacion():
    '''modifica un elemento del sistema'''

def informe(lstid,lstdesc,lstcat,lstprecio,lststock,lstmarca):
    '''visualiza todos los datos del sistema y los ordena de mayor a menor segun el stock'''
    for i in range (len(lststock)):
        for j in range (i+1 , len(lststock)):

            if lststock [i] < lststock [j]:
                # por stock
                aux = lststock[i]
                lststock[i] = lststock[j]
                lststock[j] = aux

                aux = lstid[i]
                lstid[i] = lstid[j]
                lstid[j] = aux

                aux = lstdesc[i]
                lstdesc[i] = lstdesc[j]
                lstdesc[j] = aux

                aux = lstcat[i]
                lstcat[i] = lstcat[j]
                lstcat[j] = aux
                 
                aux = lstprecio[i]
                lstprecio[i] = lstprecio[j]
                lstprecio[j] = aux

                aux = lstmarca[i]
                lstmarca[i] = lstmarca[j]
                lstmarca[j] = aux

            # si el stock es igual, ordenar por orden alfabetico
            elif lststock [i] == lststock [j]:
                if lstdesc[i] > lstdesc[j]:   
                    aux = lststock[i]
                    lststock[i] = lststock[j]
                    lststock[j] = aux

                    aux = lstid[i]
                    lstid[i] = lstid[j]
                    lstid[j] = aux

                    aux = lstdesc[i]
                    lstdesc[i] = lstdesc[j]
                    lstdesc[j] = aux

                    aux = lstcat[i]
                    lstcat[i] = lstcat[j]
                    lstcat[j] = aux

                    aux = lstprecio[i]
                    lstprecio[i] = lstprecio[j]
                    lstprecio[j] = aux

                    aux = lstmarca[i]
                    lstmarca[i] = lstmarca[j]
                    lstmarca[j] = aux
    print("ID\tDESCRIPCION\tCATEGORIA\tPRECIO\tSTOCK\tMARCA")
        # \t separa los datos en columnas mediante tabulaciones
    for i in range(len(lststock)):
        print(lstid[i], "\t", lstdesc[i], "\t", lstcat[i], "\t",
            lstprecio[i], "\t", lststock[i], "\t", lstmarca[i])





