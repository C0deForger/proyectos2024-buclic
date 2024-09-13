mi_libreria = {}
libros=[]
def simulador(libreria):
    print("NOMBRE DE LIBRERIA".center(40, "*"))
    keynombre = input("INGRESE LA KEY QUE CONTENDRA EL NOMBRE DE LA LIBRERIA: ").title().replace(" ", "")
    value_nombre = input("INGRESE EL NOMBRE DE LA LIBRERIA: ").title().replace(" ", "")
    
    print("CODIGO DE LIBRERIA".center(40, "*"))
    keycodigo = input("INGRESE LA KEY QUE CONTENDRA EL CODIGO DE LA LIBRERIA: ").title().replace(" ", "")
    value_codigo = input("INGRESE EL CODIGO DE LA LIBRERIA: ").title().replace(" ", "")
    
    libreria[keynombre] = value_nombre
    
    agregar_libros(libreria)
    
    libreria[keycodigo] = value_codigo

def agregar_libros(libreria):
    print("AGREGAR LIBRO".center(40, "*"))
    
    libreria["Libros"] = {}
    
    while True:
        nombre_libro = input("INGRESE EL NOMBRE DE SU LIBRO: ").title()
        
        while True:
            try:
                copias = int(input("INGRESE LAS COPIAS DEL LIBRO: "))
                if copias > 0:
                    break
                else:
                    print("ERROR: INGRESE UN NÚMERO MAYOR A 0")
            except ValueError:
                print("ERROR: Ingresaste un valor no numérico.")
        
        autor = input("INGRESE EL NOMBRE DEL AUTOR: ").title()
        
        libro = {
            "TITULO": nombre_libro,
            "COPIAS": copias,
            "AUTOR": autor  
        }
        
        libros.append(libro)
        respuesta = input("¿Deseas agregar otro libro? (n para parar): ").lower()
        
        if respuesta == "n":
            libreria["Libros"] = libros
            break
        else:
            print()

def buscar_libros(libreria):
    print("BUSQUEDA DE LIBROS".center(40, "*"))
    
    nombre_libro = input("INGRESE EL NOMBRE DEL LIBRO QUE BUSCARA: ")
    
    encontrado = False
    
    for libro in libreria.get("Libros", []):
        if libro["TITULO"].lower() == nombre_libro.lower():
            encontrado = True
            if libro["COPIAS"] > 0:
                copias = libro["COPIAS"]
                print(f"LIBRO ENCONTRADO! | COPIAS DISPONIBLES: {copias}")
            else:
                print(f"LIBRO ENCONTRADO! | NO HAY COPIAS DISPONIBLES")
    
    if not encontrado:
        print("LIBRO NO ENCONTRADO!")

def prestar_libro(libreria):
    print("PRESTAMO DE LIBROS".center(40, "*"))
    
    nombre_libro = input("INGRESE EL NOMBRE DEL LIBRO QUE BUSCARA: ") 
    
    encontrado = False
    
    for libro in libreria.get("Libros", []):
        if libro["TITULO"].lower() == nombre_libro.lower():
            encontrado = True
            if libro["COPIAS"] > 0:
                libro["COPIAS"] -= 1  # Reducir el número de copias disponibles
                copias = libro["COPIAS"]
                print(f"LIBRO PRESTADO! | COPIAS RESTANTES: {copias}")
            else:
                print(f"LIBRO ENCONTRADO! | NO HAY COPIAS DISPONIBLES")
    
    if not encontrado:
        print("LIBRO NO ENCONTRADO!")

def menu():
    #simulador(mi_libreria)
    
    while True:
        try:
            print("""
                  1 - BUSCAR LIBRO
                  2 - PRESTAR LIBRO
                  3 - MOSTRAR DICCIONARIO
                  4 - AGREGAR LIBRO
                  5 - SALIR
                  """)
            opcion = int(input("INGRESE UNA DE LAS OPCIONES ANTERIORES: "))
            
            if opcion == 1:
                buscar_libros(mi_libreria)
            elif opcion == 2:
                prestar_libro(mi_libreria)
            elif opcion == 3:
                print(mi_libreria)
            elif opcion == 4:
                agregar_libros(mi_libreria)
            elif opcion == 5:
                print("USTED HA SALIDO!")
                break
            else:
                print("ERROR: INGRESE UNA OPCIÓN VÁLIDA!")
        
        except ValueError:
            print("ERROR: INGRESE SOLO VALORES NUMÉRICOS")
