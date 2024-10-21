# Resta de matrices
def resta_de_matrices(matriz, diccionario_matriz):
    """
    Realiza la resta de las matrices proporcionadas.

    La funcion toma un diccionario de matrices y las resta en orden secuencial.
    La primera matriz se toma como la base, y luego las siguientes matrices se restan
    de la matriz base. El resultado es una nueva matriz que contiene la resta de todas las matrices.

    Parametros:
    - matriz: una lista de listas (matriz) que representa la matriz base para las operaciones de resta.
    - diccionario_matriz: un diccionario donde cada clave es una matriz numerada 
    (por ejemplo, 'Matriz 1', 'Matriz 2', etc.) y el valor es una lista de listas 
    que representa la matriz correspondiente.

    Variables:
    - filas: cantidad de filas de la matriz.
    - columnas: cantidad de columnas de la matriz.
    - matriz_resta: una nueva matriz inicializada en ceros, que se utilizara para almacenar el resultado de la resta.
    - primer_matriz: bandera para verificar si se esta procesando la primera matriz.

    Bucle:
    - El primer bucle inicializa la matriz_resta con los valores de la primera matriz.
    - Los bucles anidados recorren las filas y columnas para realizar la resta de cada elemento en las matrices 
    posteriores respecto a la primera matriz.

    Retorno:
    - Imprime la matriz resultante de la resta si las dimensiones coinciden.
    - Retorna False si ocurre un error de indexacion (cuando las dimensiones de las matrices no coinciden).
    """
    try:
        # Obtenemos las dimensiones de la primera matriz
        filas = len(matriz[0])
        columnas = len(matriz[0][0])

        # Inicializamos una nueva matriz en ceros con las mismas dimensiones que las matrices a restar
        matriz_resta = [[0 for i in range((columnas))] for j in range(filas)]

        #Variable para identificar si estamos recorriendo la primera matriz
        primer_matriz = True

        # Recorremos todas las matrices en el diccionario para realizar la resta
        for sub_matriz in diccionario_matriz.values():
            if primer_matriz:
                # La primera matriz se toma como base para la resta
                for i in range(filas):
                    for j in range(columnas):
                        matriz_resta[i][j] = sub_matriz[i][j]
                primer_matriz = False
            else:
                # A partir de la segunda matriz, se restan los elementos de la matriz base
                for i in range(filas):
                    for j in range(columnas):
                        matriz_resta[i][j] -= sub_matriz[i][j]

        # Imprimimos la matriz resultante de la resta
        for fila in matriz_resta:
            print(fila)

    except IndexError:
        # Retornamos False si las dimensiones de las matrices no coinciden
        return False
