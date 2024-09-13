
mi_libreria={}
libros=[]

def simulador(libreria):
    print ("NOMBRE DE LIBRERIA".center(30,"*"))
    keynombre= input("INGRESE EL NOMBRE DE LA LIBRERIA: ").title().replace(" ", "")
    value_nombre= input("INGRESE EL VALUE DEL NOMBRE DE LA LIBRERIA: ").title().replace(" ", "")
    
    #AGREGAR CODIGO+
    
    
    print ("CODIGO DE LIBRERIA".center(30,"*"))
    keycodigo= input("INGRESE LA KEY QUE CONTENDRA EL CODIGO DE LA LIBRERIA: ").title().replace(" ", "")
    value_codigo= input("INGRESE EL CODIGO DE LIBRERIA: ").title().replace(" ", "")
    
    libreria[keynombre]= value_nombre
    
    agregar_libros(libreria)
    
    libreria [keycodigo]= value_codigo
         
def agregar_libros (libreria):
    print ("AGREGAR LIBRO".center(30,"*"))
    
    libreria["Libros"]={}

    
    while True:
        nombre_libro= input( "INGRESE EL NOMBRE DE SU LIBRO: ").title()
        
        while True:
            try:
                copias=int (input ("INGRESE LAS COPIAS DEL LIBRO: "))
                
                if copias>0:
                    break
                else:
                    print("ERROR IGRESE UN NUMERO MAYOR A 0")
                
            except ValueError:
                print ("error ingresate un numero")
        autor=input ("INGRESE EL NOMBRE DEL AUTOR: ").title()
        
        libro= {
            "TITULO": nombre_libro,
            "COPIAS": copias,
            "AUTOR": autor  
        }
        
        libros.append(libro)
        respuesta= input ("Ingresa n para parar: ").lower()
        
        if respuesta== "n":
            libreria["Libros"]=libros
            break
        else:
            "JUEGUE JUEGUE, agrega más agrega más"
            
def buscar_libros(libreria):
    print ("BUSQUEDA DE LIBROS".center(30,"*"))
    
    nombre_libro= input("INGRESE EL NOMBRE DEL LIBRO QUE BUSCARA: ")
    
    #GET ES COMO DECIR "DE ESTA CLAVE SOLO ME BUSCARAS LOS VALORES, OSEA LIBROS"
    encontrado= False
    
    for libro in libreria.get ("Libros",[]):
        if libro["TITULO"].lower()== nombre_libro.lower():
            encontrado=True
            if libro["COPIAS"]>0:
                copias= libro["COPIAS"]
                print(f"LIBRO ENCONTRADO! | COPIAS DISPONIBLES: {copias}")
            else:
                print(f"LIBRO ENCONTRADO! | NO HAY COPIAS DISPONIBLES")

    #esto es como decir que encontrado sigue siendo falso
    if not encontrado:
        print("LIBRO NO ENCONTRADO!")
        
        
        

def prestar_libro (libreria):
    print ("BUSQUEDA DE LIBROS".center(30,"*"))
    
    nombre_libro= input("INGRESE EL NOMBRE DEL LIBRO QUE BUSCARA: ") 
    
    #GET ES COMO DECIR "DE ESTA CLAVE SOLO ME BUSCARAS LOS VALORES, OSEA LIBROS"
    encontrado= False
    
    for libro in libreria.get ("Libros",[]):
            if libro["TITULO"].lower()== nombre_libro.lower():
                encontrado=True
                if libro["COPIAS"]>0:
                    copias= libro["COPIAS"]
                    print(f"LIBRO ENCONTRADO! | COPIAS DISPONIBLES: {copias}")
                else:
                    print(f"LIBRO ENCONTRADO! | NO HAY COPIAS DISPONIBLES")

    
    #esto es como decir que encontrado sigue siendo falso
    if not encontrado:
        print("LIBRO NO ENCONTRADO!")




def menu ():
    #simulador(mi_libreria)
    
    while True:
        try:
            print("""
                  1-BUSCAR LIBRO
                  2-PRESTAR LIBRO
                  3- MOSTRAR DICCIONARIO
                  4-AGREGAR LIBRO
                  5-SALIR
                  """)
            opcion= int(input("INGRESE UNA DE LAS OPCIONES ANTERIORES:"))
            if opcion==1:
                buscar_libros(mi_libreria)
            elif opcion==2:
                prestar_libro(mi_libreria)
            elif opcion==3:
                print (mi_libreria)
            elif opcion==4:
                agregar_libros(mi_libreria)
            elif opcion==5:
                print("USTED A SALIDO! ")
                break
            else:
                "ERROR, INGRESE UNA OPCIÓN VALIDA!"
        
        except ValueError:
            print ("INGRESE SOLO VALORES NUMERICOS")


menu()