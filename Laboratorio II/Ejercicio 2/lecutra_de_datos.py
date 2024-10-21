def lectura_del_txt():
    """
    funcion para obtener toda la informacion acerca de los usuarios en forma de diccionario
    """
    dict_users = {}
    try:
        with open("Ejercicio 2/usuario_database.txt", 'r') as archivotxt:
            for i, line in enumerate(archivotxt):
                partes = line.strip().split(",")
                #print(f"Línea {i+1} procesada: {partes}")  # Depuración de la línea leída
                # Verifica si la línea tiene 4 partes
                if len(partes) == 4:
                    dui,nombre, password, saldo = partes
                    dict_users[dui] = {
                        "CONTRASENIA": password,
                        "NOMBRE": nombre,
                        "SALDO": float(saldo)
                    }
                #else:
                    #print(f"Advertencia: Línea {i+1} no válida (esperados 4 valores, encontrados {len(partes)}): {line.strip()}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
    
    return dict_users


