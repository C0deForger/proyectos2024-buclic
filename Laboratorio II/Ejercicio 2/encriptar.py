def encriptar_contrasenia_ascii(contrasenia):
    """
    Funcion que recibe la contraseña y la vuelve  a codificar en ASCII.


    Args:
        contrasenia (str): contraseña ingresada por  el usuario

    Returns:
        str: contraseña encriptada
    """
    desplazamiento = 3
    contrasenia_encriptada = ""
    for char in contrasenia:
        # Usar ord() para obtener el valor ASCII y sumar el desplazamiento
        nuevo_valor_ascii = ord(char) + desplazamiento
        # Convertir de nuevo a carácter usando chr() con el nuevo valor
        contrasenia_encriptada += chr(nuevo_valor_ascii)
    return contrasenia_encriptada

def desencriptar_contrasenia_ascii(contrasenia_encriptada):
    """
    recibe la contraseña encriptada y la desencriptada

    Args:
        contrasenia_encriptada (str): contraseña encriptada

    Returns:
        str: desencriptada
    """
    desplazamiento = 3
    contrasenia_desencriptada = ""
    for char in contrasenia_encriptada:
        # Usar ord() para obtener el valor ASCII y restar el desplazamiento
        nuevo_valor_ascii = ord(char) - desplazamiento
        # Convertir de nuevo a carácter usando chr() con el nuevo valor
        contrasenia_desencriptada += chr(nuevo_valor_ascii)
    return contrasenia_desencriptada