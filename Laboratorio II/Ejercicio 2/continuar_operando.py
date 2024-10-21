def continuar():
    """
    funcion que consulta al usuario si decia continuar haciendo transacciones en el atm
    
    """
    while True:
        print(" ")
        print('Desea realizar otra operación "Si/No"? ')
        confirmacion=input((">"))
        if confirmacion.lower()=="no":
            return False
        elif confirmacion.lower()!="si":
            print("Opción no valida! ")
        else:
            return 