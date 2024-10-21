from lecutra_de_datos import lectura_del_txt
from encriptar import desencriptar_contrasenia_ascii
def validar_usuario(user):
    """
        Esta función compara el usuario  ingresado con el usuario existente en el archivo de texto

    Args:
        user (str)): El nuevo usuario a ingresar

    Returns:
        bool: si  el usuario existe retornara True, de lo contrario  retornara False


    """
    lecutra_de_datos=lectura_del_txt()
    if user in lecutra_de_datos:
        print(f"El usuario {user} ya esta en uso, por favor ingrese un usuario valido o inicie secccion--> ")
        return True
    else: 

        return False
    
#Validar si el dui ya fue registrado
def validar_dui(dui:str):
    """ 
    obtienes una lista con todos los duis ingresados y la compara con  el dui ingresado por el usuario, dependiendo de si el dui ingresado ya fue registrado
    retornara un resultado u otro

    Returns:
        bool: True si el dui ya esta registrado, False si el dui no ha sido ingresado
    """
    lista_duis=[]
    informacion=lectura_del_txt()
    #añadimos todos los duis existentes a una lista
    for i,b in informacion.items():
        lista_duis.append((i))
        
    
    #if donde verifica si dui esta dentro de  la lista de duis registrados
    if dui in lista_duis:
        #retormnamos true indicando que el numero de dui ingresado ya esta registrado por otro usuario
        return True
    #de lo contrario procedera a solicitar el el saldo de la cuenta y posteriormente se añadiran sus datos a la base de datos
    else:
        return 

        
def valida_formato_dui(new_dui):
    """
    Esta función valida que el DUI contenga los elementos correctos, el largo y que no ingrese numeros negativos

    Args:
        new_dui (int): el nuevo DUI que se quiere ingresar a la base de datos

    Returns:
        Bool: si cumple con el formato retornara False, sino cumple con el formato retornara True
    """
    if len(str(new_dui)) == 8:
        return False
    else:
        return True

def validar_contrasenia(contrasenia):
    """
    Validamos que la contraseña ingresada por el usuario sea correcta

    Args:
        contrasenia (str): contraseña ingresada por el usuario

    Returns:
        bool: si la contraseña coincide retornara true
    """
    lista_contrasenias=[]
    informacion=lectura_del_txt()
    for i,b in informacion.items():
        contrasenia_des = desencriptar_contrasenia_ascii(str(b["CONTRASENIA"]))
        lista_contrasenias.append(contrasenia_des)

    if contrasenia in lista_contrasenias:
        return True
        
