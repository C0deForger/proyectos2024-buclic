# Multiplicacion de matrices
def multiplicar_matrices(diccionario_matriz):
    """
    Realiza la multiplicacion secuencial de las matrices proporcionadas en el diccionario.

    La funcion toma un diccionario que contiene varias matrices y las multiplica en orden.
    La primera matriz se toma como base, y luego cada matriz subsecuente se multiplica
    con el resultado acumulado de las multiplicaciones anteriores. Si las dimensiones
    de las matrices no son compatibles para la multiplicacion, la funcion imprime un 
    mensaje de error y retorna None.

    Parametros:
    - diccionario_matriz: un diccionario donde cada clave es una matriz numerada 
        (por ejemplo, 'Matriz 1', 'Matriz 2', etc.) y el valor es una lista de listas 
        que representa la matriz correspondiente.

    Variables:
    - claves: una lista de las claves en el diccionario, que permite el acceso a las matrices.
    - resultado: inicialmente es la primera matriz en el diccionario y se actualiza
        despues de cada multiplicacion.

    Bucles:
    - El bucle principal itera sobre las matrices en el diccionario, verificando si sus 
        dimensiones son compatibles para la multiplicacion.
    - Se utiliza la funcion auxiliar `multiplicar_matriz` para realizar la multiplicacion
        entre dos matrices en cada iteracion.

    Retorno:
    - Retorna la matriz resultante de todas las multiplicaciones, o None si las 
        dimensiones no son compatibles.
    - Retorna False si ocurre un error de indexacion (cuando las dimensiones no coinciden).
    """
    try:
        # Obtenemos las claves (nombres) de las matrices en el diccionario
        claves = list(diccionario_matriz.keys())

        # Inicializamos el resultado con la primera matriz
        resultado = diccionario_matriz[claves[0]]

        # Recorremos el resto de matrices en el diccionario
        for i in range(1, len(claves)):
            matriz = diccionario_matriz[claves[i]]
            
            # Verificamos si las dimensiones son compatibles para multiplicacion
            if len(resultado[0]) != len(matriz):
                print("Error -- Las dimenciones de las matrices no son compatibles para multiplicarse")
                return None
            
            # Realizamos la multiplicacion de la matriz actual con el resultado acumulado
            resultado = multiplicar_matriz(resultado, matriz)
        
        # Retornamos el resultado final de la multiplicacion de todas las matrices
        return resultado
    
    except IndexError:
        # Retornamos False si ocurre un error de indexacion
        return False

def multiplicar_matriz(A, B):
    """
    Multiplica dos matrices A y B.

    La funcion toma dos matrices A y B, y realiza la multiplicacion de matrices, generando
    una nueva matriz que contiene el producto de A y B. Para que la multiplicacion sea 
    posible, el numero de columnas de A debe ser igual al numero de filas de B.

    Parametros:
    - A: una lista de listas (matriz) que representa la primera matriz a multiplicar.
    - B: una lista de listas (matriz) que representa la segunda matriz a multiplicar.

    Variables:
    - filasA: cantidad de filas en la matriz A.
    - columnasA: cantidad de columnas en la matriz A.
    - filasB: cantidad de filas en la matriz B.
    - columnasB: cantidad de columnas en la matriz B.
    - resultado: matriz que almacena el resultado de la multiplicacion, de tamaño
        filasA x columnasB, inicializada con ceros.

    Bucle:
    - Se utilizan tres bucles anidados: 
        1. El bucle exterior recorre las filas de la matriz A.
        2. El segundo bucle recorre las columnas de la matriz B.
        3. El tercer bucle realiza la suma del producto de los elementos correspondientes
            en las filas de A y las columnas de B.

    Retorno:
    - Retorna la matriz resultante de la multiplicacion.
    """
    # Obtenemos las dimensiones de las matrices A y B
    filasA = len(A)
    columnasA = len(A[0])
    filasB = len(B)
    columnasB = len(B[0])

    # Inicializamos una nueva matriz con ceros de tamaño filasA x columnasB
    resultado = [[0 for i in range(columnasB)] for j in range(filasA)]

    # Realizamos la multiplicacion de matrices
    for i in range(filasA):
        for j in range(columnasB):
            for k in range(columnasA):
                resultado[i][j] += A[i][k] * B[k][j]

    # Retornamos la matriz resultante
    return resultado

#Juan1234