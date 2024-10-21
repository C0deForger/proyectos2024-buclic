from Validacion import validar_usuario,validar_dui,valida_formato_dui
from lecutra_de_datos import lectura_del_txt
import encriptar

def crear_usuario():
    """
    funcion para crear un nuevo usuario y añadirlo a la base de datos
    Returns:
        Bool: False si hubo algun error en el proceso de  creacion del usuario
    """ 
    while True:

        nombreuser = input("Ingrese su nombre completo--> ")
        list_name = nombreuser.split()
        for name in list_name:
            if not name.isalpha():
                print("Error -- Nombre de usuario invalido. \nNo utilize  caracteres especiales")
                return 
        else:
            break
           
    password = input("Cree una contrasenia  --> ")
    password = encriptar.encriptar_contrasenia_ascii(password)
            
    while True:
        documento_unico_identidad = input("ingrese su numero de dui por favor sin '-' --> ")
  
        #valida que el usuario ingrese  un dui valido
        try:
            
            if len (documento_unico_identidad)==9:
                int(documento_unico_identidad)
                break
            else:
                print("Error -- El dui ingresado no es valido")
                
        except ValueError:
            print("Numero de DUI no valido!")

    #verificamos  si el dui ya existe en la base de datos
    if validar_dui(documento_unico_identidad):
        print("ERROR! numero de DUI ya esta registrado!")
        return False
    #si el dui no fue encontrado procedera a solicitar el el saldo de la cuenta y posteriormente se añadiran sus datos a la base de datos
    else:
        while True:
            try:
            #try para validar que el usuario ingrese un saldo valido           
                saldo = float(input("Ingrese la cantidad de saldo que agregara a su cuenta--> "))
                if saldo<=0:
                    print("Cantidad no valida!")
                else:
                    break
            except ValueError: 
                print("Error, se esperaba una cantidad numerica")
        #en esta parte se lleva acabo el ingreso de información al txt                
        with open ("Ejercicio 2/usuario_database.txt", 'a') as file:
            file.write(f"{documento_unico_identidad},")
            file.write(f"{nombreuser},")
            file.write(f"{password},")
            file.write(f"{saldo}\n")
            
