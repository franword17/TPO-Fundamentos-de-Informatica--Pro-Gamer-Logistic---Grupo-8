import functionsTPO

def main():
    lstID = ["MON001" , "STL245" , "RGB120"]
    lstdesc = ["Monitor Gamer 240Hz", "Teclado Mecánico RGB" , "Silla Ergonómica Pro"]
    lstcat = ["Monitores" , "Periféricos" , "Sillas"]
    lstprecio = [350.99 , 55.99 , 499.99]
    lststock = [4, 2 , 8]
    lstmarca = ["ASUS" , "HyperX" , "Corsair"]

    op = functionsTPO.menu()
    while op != 8: 
        
        if op == 1:
            lstID,lstdesc,lstcat,lstprecio,lststock,lstmarca = functionsTPO.nuevoproducto(lstID,lstdesc,lstcat,lstprecio,lststock,lstmarca)
            #regristrar nuevo prducto
        elif op == 2:
            #eliminar producto del sistema
        elif op == 3:
            #modifica el stock
        elif op == 4:
            functionsTPO.informe(lstID,lstdesc,lstcat,lstprecio,lststock,lstmarca)
            #informe general del sistema
            
        op = functionsTPO.menu()
        
    print ("usted finalizo la ejecucion del sistema")
main()
