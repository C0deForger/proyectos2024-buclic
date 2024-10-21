def actualizar_saldo(dui:str,nuevo_saldo:float):
        """Con este metodo actualizo el saldo, solo necesita recibir el nombre del usuario y el nuevo saldo
        Args:
            nombre (str): El nombre del usuario
            nuevo_saldo (float): el saldo del usuario a actualizar

        Returns:
            bool: retorna un true indicando el exito de la operacion
        """
        #lista donde almacenare la información a actualizar
        usuarios=[]
        #leo el archivo
        with open("Ejercicio 2/usuario_database.txt", 'r') as archivotxt:
            #recorro el lo elementos del txt
            for i in archivotxt:
                #elimino espacios, y hago una sola lista que se almacena en informacion
                informacion=i.strip().split(",")
                #si el dato en 0 que seria el nombre es == al nombre ingresado por el usuario entonces
                if informacion[0]==dui:
                    #la informacion del dato 3 se modifica a la del nuevo saldo, pero como texto y no como float
                    informacion[3]=float(nuevo_saldo)
                #y aqui se agrega cada dato a la lista de usuarios    
                usuarios.append(informacion)
        
        #abro de nuevo el archivo, ahora como escritura para remodificar la base de datos        
        with open("Ejercicio 2/usuario_database.txt", 'w') as txt_modificar:
            #recorro los elementos en la lista anteriormente llenada
            for datos in usuarios:
                #esta variable almacenara los datos que hay en la lista de cad ausuario + salto de linea
                info=f"{datos[0]},{datos[1]},{datos[2]},{datos[3]}\n"
                #linea = datos[0] + ',' + datos[1] + ',' + datos[2] + ',' + datos[3] + '\n'
                #aca la variable se escribe en el texto y esto se hara hasta que bucle ford se cierre
                txt_modificar.write(info)


def actualizar_saldo_tk(nombre:str,nuevo_saldo:float,dui:str):
        """Con este metodo actualizo el saldo, solo necesita recibir el nombre del usuario y el nuevo saldo
        Args:
            nombre (str): El nombre del usuario
            nuevo_saldo (float): el saldo del usuario a actualizar

        Returns:
            bool: retorna un true indicando el exito de la operacion
        """
        #lista donde almacenare la información a actualizar
        usuarios=[]
        #leo el archivo
        with open("Ejercicio 2/usuario_database.txt", 'r') as archivotxt:
            #recorro el lo elementos del txt
            for i in archivotxt:
                #elimino espacios, y hago una sola lista que se almacena en informacion
                informacion=i.strip().split(",")
                #si el dato en 0 que seria el nombre es == al nombre ingresado por el usuario entonces
                if informacion[0]==dui and informacion[2] == nombre:
                    #la informacion del dato 3 se modifica a la del nuevo saldo, pero como texto y no como float
                    informacion[3]=float(nuevo_saldo)
                #y aqui se agrega cada dato a la lista de usuarios    
                usuarios.append(informacion)
        
        #abro de nuevo el archivo, ahora como escritura para remodificar la base de datos        
        with open("Ejercicio 2/usuario_database.txt", 'w') as txt_modificar:
            #recorro los elementos en la lista anteriormente llenada
            for datos in usuarios:
                #esta variable almacenara los datos que hay en la lista de cad ausuario + salto de linea
                info=f"{datos[0]},{datos[1]},{datos[2]},{datos[3]}\n"
                #linea = datos[0] + ',' + datos[1] + ',' + datos[2] + ',' + datos[3] + '\n'
                #aca la variable se escribe en el texto y esto se hara hasta que bucle ford se cierre
                txt_modificar.write(info)