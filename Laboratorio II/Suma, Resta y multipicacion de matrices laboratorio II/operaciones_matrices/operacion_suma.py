#Suma de matrices
def suma_de_matrices(matriz, diccionario_matriz):
    """
    Realiza la suma de matrices contenidas en un diccionario.

    Parametros:
    matriz (list): Lista de listas que representa una matriz (usada para obtener las dimensiones).
    diccionario_matriz (dict): Diccionario que contiene matrices a sumar, donde las claves representan 
                            el nombre de cada matriz y los valores son las matrices como listas de listas.

    Retorno:
    None: Imprime la matriz resultante de la suma de todas las matrices.

    Funcionamiento:
    - Se obtienen las dimensiones (filas y columnas) de la primera matriz en la lista para crear una matriz de ceros
    del mismo tamanio.
    - Luego, se recorre el diccionario de matrices para sumar los valores correspondientes de cada matriz en la 
    matriz resultante (`matriz_suma`).
    - Se utiliza un bucle for anidado: el bucle exterior recorre cada fila y el bucle interior recorre cada columna.
    - Los valores se suman de manera acumulativa en la matriz de ceros (`matriz_suma`).
    - Al final, se imprime la matriz resultante.

    Excepciones:
    - Si ocurre un error de indice (por ejemplo, si las matrices tienen dimensiones diferentes), se obtiene un 
        `IndexError` y se retorna False.
    """
    try:
        # Obtiene la cantidad de filas y columnas de la primera submatriz
        filas = len(matriz[0])
        columnas = len(matriz[0][0])
        
        # Crea una matriz inicializada en cero con las mismas dimensiones que las matrices a sumar
        matriz_suma = [[0 for k in range(columnas)] for l in range(filas)]
        
        # Itera sobre cada submatriz en el diccionario de matrices
        for sub_matriz in diccionario_matriz.values():
            # Itera sobre cada fila de la submatriz
            for fila in range(filas):
                # Itera sobre cada columna de la fila actual
                for columna in range(columnas):
                    # Suma el valor de la submatriz a la matriz acumulada
                    matriz_suma[fila][columna] += sub_matriz[fila][columna]
        
        # Imprime la matriz resultante de la suma
        print("\nLa suma de matrices es: ")
        for filas in matriz_suma:
            print(filas)
    
    except IndexError:
        # Si hay un error en los índices (dimensiones no coinciden), retorna False
        return False
