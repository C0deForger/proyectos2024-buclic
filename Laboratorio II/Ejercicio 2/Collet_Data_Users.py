def Collet_Data_User(User,list_transaccion,retiro_dinero, dinero_en_cuenta):
    import datetime
    current_time = datetime.datetime.now()
    current_time_good=current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-4]

    diccionario = {
        "Propetiario ATM: ": "Debuggin Ninja",
        "Cajero: ": "N_1 - San Miguel",
        "Nombre del Usuario: ":  User,
        "Transacciones Realizadas: " : list_transaccion, 
        "Saldo Retirado: ": f"{str(retiro_dinero) if retiro_dinero != 0 else 'No se realizo ninguna transacción'}",

        "Saldo total en cuenta: ": f"{str(dinero_en_cuenta) if dinero_en_cuenta != 0 else 'No se realizo ninguna transacción'}",

        
        "Fecha - Hora: ": current_time_good
    }
    diccionario[""] = ""
    
    with open("Ejercicio 2/Factura.txt","w") as archivo:
        #archivo.write(diccionario)
        for key, value in diccionario.items():
            archivo.write(f"{key}{value}\n")
            

def Mostrar_factura():
    with open ("Ejercicio 2/Factura.txt") as archivo:
        contenido = archivo.read()
        print(f"{contenido}")