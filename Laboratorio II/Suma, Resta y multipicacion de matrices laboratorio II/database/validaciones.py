import random

def creacion_Matriz(dimension):
    """
    Crea una matriz de dimensiones dadas por el usuario y valida la entrada.

    Parametros:
    dimension (str): Dimensiones de la matriz en formato 'filasxcolumnas' (ejemplo: '2x3').

    Retorno:
    lista: Una lista que contiene:
        - Una lista de listas representando la matriz con numeros aleatorios si la validacion es exitosa,
            o un mensaje de error si la entrada es invalida.
        - Un booleano indicando si hubo un error en la validacion (True si hubo error, False si no).

    Funcionamiento:
    - Se valida que el formato de la entrada solo contenga caracteres validos (números y 'x').
    - Si el formato es valido, se separan las filas y columnas, y se genera una matriz con numeros
        aleatorios entre 1 y 50.
    - Si el formato es invalido o la entrada es incorrecta, se devuelve un mensaje de error.
    """
    
    try:
        validaciones = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x"]
        condicion = None
        
        #Bucle para validar que cada caracter en la cadena es un numero o 'x'
        for char in dimension:
            if char not in validaciones:
                condicion = False
                break
            else:
                condicion = True
        try:
            if condicion == True:
                dimensiones = dimension.split("x")
                if len(dimensiones) == 1:
                    return "Error -- La entrada ingresada es inválida, intente nuevamente con una entrada valida. Ejemplo: (2x3)", True
                else:
                    columnas = int(dimensiones[1])
                    filas = int(dimensiones[0])
                    
                    #Crea la matriz de dimensiones dadas con numeros aleatorios
                    matriz = [[random.randrange(1, 50) for i in range(columnas)] for i in range(filas)]
                    return matriz, False
            else:
                return f"No se realiza ninguna operacion porque la matriz es invalida", True
        except ValueError:
            return f"No se realiza ninguna operacion porque la matriz es invalida", True
    except IndexError:
        return "Error -- La entrada ingresada es inválida, intente nuevamente con una entrada valida. Ejemplo: (2x3)", None


def acumulador_de_lista(lista_matrices, matriz_unitaria):
    """
    Acumula matrices en una lista para posteriores operaciones.

    Parámetros:
    lista_matrices (list): Lista donde se acumularán las matrices.
    matriz_unitaria (list): Matriz que será añadida a la lista.

    Retorno:
    list: La lista de matrices actualizada.
    
    Funcionamiento:
    - Agrega una matriz nueva a una lista de matrices, permitiendo que se acumulen para
    realizar operaciones posteriores.
    """
    lista_matrices.append(matriz_unitaria)
    return lista_matrices


def preparar_matriz(matriz):
    """
    Prepara una matriz y la estructura en un diccionario con un formato más claro.

    Parámetros:
    matriz (list): Lista de listas que representa una matriz.

    Retorno:
    dict: Diccionario que mapea cada número de matriz con sus valores correspondientes.

    Funcionamiento:
    - Se toma una matriz y se convierte en un diccionario donde cada fila se asocia a una clave 
    con el formato 'Matriz X' (donde X es el número de fila).
    - Cada fila de la matriz original se añade como un valor de lista en el diccionario.
    """
    numero_matriz = 0
    dict_matriz = {}
    
    #Bucle que itera sobre cada fila de la matriz
    for fila in matriz:
        numero_matriz += 1
        dict_matriz[f"Matriz {numero_matriz}"] = []
        
        #Añade cada valor de la fila al diccionario bajo la clave 'Matriz N'
        for columna in fila:
            dict_matriz[f"Matriz {numero_matriz}"].append(columna)

    return dict_matriz


def controlador_decision():
    """
    Controla la entrada de decisión del usuario sobre qué operación realizar.

    Retorno:
    str: La operación seleccionada por el usuario ('Suma', 'Resta', 'Multiplicacion').

    Funcionamiento:
    - Muestra las opciones disponibles y recibe una entrada del usuario.
    - Valida que la entrada sea una operación válida ('Suma', 'Resta' o 'Multiplicación').
    - Si la entrada es invalida, solicita una nueva entrada hasta que se ingrese una opcion correcta.
    """
    controlar_while = True
    nume = ["Suma", "Resta", "Multiplicacion"]
    
    # Bucle que se repite hasta que el usuario ingrese una operación válida
    while controlar_while:
        print("¿Que operación desea efectuar? \n-Suma\n-Resta \n-Multiplicación ")
        decision_ecuacion = input(" ").capitalize()
        
        if decision_ecuacion not in nume:
            print("Inválido -- Ingrese solo operaciones válidas ")
        else:
            controlar_while = False
            return decision_ecuacion


def validar_tamanio_matrices(matriz):
    """
    Valida que todas las submatrices tengan el mismo tamanio.

    Parámetros:
    matriz (list): Lista de listas que representa una matriz o varias matrices.

    Retorno:
    bool: True si todas las submatrices tienen el mismo tamanio, False en caso contrario.

    Funcionamiento:
    - Verifica que todas las submatrices dentro de la matriz tengan la misma cantidad de columnas.
    - Además, verifica que todas las filas dentro de cada submatriz sean del mismo tamaño.
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    
    # Verifica que todas las columnas sean del mismo tamanio
    for submatriz in matriz:
        if len(submatriz) != columnas:
            return False
        
        # Verifica que cada fila dentro de la submatriz sea consistente en tamanio
        for fila in submatriz:
            if len(fila) != len(matriz[0][0]):
                return False
    
    return True


