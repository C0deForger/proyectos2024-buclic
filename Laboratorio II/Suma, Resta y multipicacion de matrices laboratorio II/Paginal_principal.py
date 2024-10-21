#Importamos las funciones que nos serviran más adelante

import database.validaciones as fun_val

import operaciones_matrices.operacion_suma as fun_sum

import operaciones_matrices.operacion_resta as fun_res

import operaciones_matrices.operacion_multiplicacion as fun_mul



control_while = True

mensaje_operaciones = """

--------------------  Importante  ----------------------------

Para realizar una suma o resta de matrices:
-Las matrices deben tener el mismo numero de filas y columnas.
==============================================================
Ejemplo:
-Si la matriz A tiene dimension 
2 x 3 y la matriz B también tiene dimension 
2 x 3, entonces se pueden sumar o restar.
==============================================================
Para realizar una multiplicacion de matrices:
- El número de columnas de la primera matriz debe ser igual 
al numero de filas de la segunda.
==============================================================
Ejemplo:
Si la matriz A tiene dimensión 
2 x 3 y la matriz B tiene dimensión 
3 x 2, entonces se puede efectuar la multiplicación.

"""

print(mensaje_operaciones)


#Definimos una variable con el nombre "controlador_bucle" como True la cual nos sirve para controlar el primer bucle while

controlador_bucle = True


lista_matrices = []
#Inicializamos un bucle while el cual nos sirve para que el usuario agregue las dimensiones de las matrices 
while controlador_bucle:
    
    #Definimos una lista vacia en la cual se almaceneran las matrices que el usuario cree
    #Importante que este dentro del bucle para evitar posibles poblemas
    
    
    #Bucle while el cual nos sirve para controlar la entrada de datos del usuario 
    while True:
        
        #try except el cual sirve por si el usuario agrega dimensiones incorrectas, tal como str o float y para que el programa no se cierre 
        try:
            
            #Variable la cual sirve para almacenar la cantidad de matrices que el usuario quiere crear 
            num_matriz = int(input("\nIngrese el numero de matrices a sumar/restar/multiplicar --> "))
            
            #Condicion que nos sirve para validar si el usuario agregar numeros negativos o el numero 1 (el cual no nos sirve para llevar a cabo ninguna operacion )
            
            if num_matriz <= 1 :
                
                print("\nError -- Por favor ingrese datos numericos enteros positivos y mayores que 1")
            else:
                break
            
        except ValueError:
            
            #Error personalizado por si el usuario agrega un str 
            print("\nError -- Ingrese solo datos numericos enteros mayores a 1 ")
    
    #Bucle for el cual se repite el numero veces que el usuario veces que el usuario creara matrices  
    for i in range(num_matriz):
        while control_while:
            #Entrada de datos con un ejemplo de como deben ser las dimensiones de las matrices
            matriz_Usuario = input(f"\nIngrese las dimensiones de la matriz {i+1} formato (filas)x(columnas).\nEjemplo: 2x3 --> ").lower()
            
            #fun_val.creacion_Matriz(matriz_Usuario): funcion que creara la matriz con las dimensiones dadas por el usuario 
                #Variable "mensaje" la cual guardan el mensaje de error o la matriz creada con las dimensiones que el usuario agrego
                #Variable "repetidor" la cual sera True o False, segun sea el caso o el retorno de la variable menseaje 
                # (mas informacion sobre "fun_val.creacion_Matriz()" en el paquete "database")
            mensaje,repetidor = fun_val.creacion_Matriz(matriz_Usuario)
            #Funcion fun_val.creacion_Matriz(matriz_Usuario) retorna un "mensaje", el cual puede ser una lista (matriz) si la entrada de datos es valida, 
            # o puede ser un mensaje para el usuario de error si ha enviado una entrada invalida
            
            #Condicion la cual maneja el ciclo del bucle for segun sea la salida de datos de la funcion fun_val.creacion_Matriz(matriz_Usuario) 
            # guardada en la variable "repetidor"
            if repetidor == True:
                print("\nPor favor ingrese dimeniones validas.\n ")
            else:
                break
        
        #Variable que segun sea el caso, si el retorno de la variable mensaje es una lista (la cual contiene las dimensiones y datos de las matrices) se iran 
        #guardando en la funcion fun_val.acumulador_de_lista() la cual sera de mucha ayuda para la ejecucion de las operaciones con matrices
        if type(mensaje) == list:
            
            
            #fun_val.acumulador_de_lista: funcion que sirve para acumular las matrices que el usuario ha creado
            
            #Entrada de datos en la funcion "fun_val.acumulador_de_lista(lista_matrices,mensaje)".
                
                #lista_matrices: Utilizamos la lista antes creada y la igualamos al retorno de la funcion "fun_val.acumulador_de_lista" la cual toma
                
                #como parametro la lista "vacia lista_matrices" y las listas unitarias segun el rango de listas que el usuario creara. 
                
                #mensaje: utilizamos la variable mensaje, la cual si la condicion se cumplio, sera una lista con la matriz con las dimensiones dadas por el usuario.
                
            #Mas informacion de la funcion "fun_val.acumulador_de_lista(lista_matrices,mensaje)" en paquete "database".
            
            lista_matrices = fun_val.acumulador_de_lista(lista_matrices,mensaje)
            
            #La funcion retornara una lista con todas las matrices creadas por el usuario si y solo si la condicion "if type(mensaje) == list" se cumple.
            
    #Condicion "if type(mensaje) == list:": sirve para cerrar el bucle "while controlador_bucle:" si la salida de datos en la variables "mensaje" es la esperada (una lista (matriz) ). 
    if type(mensaje) == list:
        break
    
    #Condicion "if type(mensaje) == str:": sirve para enviarle un mensaje en caso de que la salida de datos haya sido un mensaje de errorr por entrada de datos inavalida
    #al momento que el usuario haya enviado unas dimensiones incorrectas a la hora de crear la matriz.
    if type(mensaje) == str:
        #repetidor: variable en la cual antes mencionabamos que puede tener 2 varoles boolenas (True / False) segun sea la salida de la valiable "mensaje" de la funcion "fun_val.creacion_Matriz(matriz_Usuario)"
        #en este caso, como la variable mensaje es un str (cadena de texto) el cual es un mensaje de error para el usuario por haber escrito una entrada de datos invalida.
        if repetidor == True:
            #mensaje: como las dimensiones que el usuario ingreso, son invalidas, la variable "mensaje" en un mensaje de error para el usuario. 
            #Mas informacion en la funcion "fun_val.creacion_Matriz()" en el paquete "database").
            print(f"\n{mensaje}")
            
            #Bucle while: el cual se inicializa como True, para que se repita infinitamente hasta que el usuario ingrese una opcion valida.   
            while True:
                #Variable decision: guarda la entrada de datos o decision que el usuario haya decidido (valga la redundancia), la cual se espera que sea si o no.
                decision = input("\nDesea volver a intentarlo (Si/No) ").lower()
                print()
                
                #Condicion "if decision == "si" ": sirve para que el bucle vuelva inicializarse desde 0 y el usuario puede crear nuevas matrices.
                if decision == "si":
                    #Controlador_bucle: Si usuario el desea volver a intenatlo (si el usuario agrego si) el bucle al principio y el usuario puede agregar nuevos datos. 
                    controlador_bucle = True
                    break
                #Condicion "if decision == "no":" sirve para cerrar el bucle "while controlador_bucle:" si el usuario agrega "no" en la variable decision.

                if decision == "no":
                    #Controlador_bucle: si el usuario no desea volver a intentarlo el bucle toma el valor booleano "False" el cual cerraria el bucle "while controlador_bucle:" y se acabaria el proceso del codigo.
                    controlador_bucle = False
                    break
                else:
                    #Mensaje que se le muestra al usuario si no agrego una condision valida.
                    print("\nParace que ha ocurrido un error, intente nuevamente y procure escribir solo si o no ")
                    print()
        #"if repetidor == False: (dentro del bucle "while controlador_bucle:")": variable ya antes mensionada la cual toma el valor boolena "False" si la variable "mensaje" es una lista.
        #Funcionalidad en el codigo: sirve para acabar con el bucle "while controlador_bucle:"
        if repetidor == False:
            break
#"if repetidor == False: (fuera del bucle "while controlador_bucle:")": sirve para mostrar la informacion de las matrices creadas.
#Funcionalida en el codigo: Sirve para evitar posible errores, si el usuario agrego n cantidades de matrices buenas, pero, si agrego una mala, el programa mandaria un error de sistema.
if repetidor == False:
    #Mostrar las matrices unitariamente (mas estetico)
    print()
    print("=======================================================")
    
    print("Sus matrices son:")
    for matrices in lista_matrices:
        print(matrices)
    print()
    
    #if type(mensaje) == list:
        #Funcionalidad en el codigo: Enviara un apartado al usuario para que decida una operacion con las matrices creadas. 
    
    if type(mensaje) == list:
        
        #desicion_ecuacion: sirve para guardar la decision sobre que operacion matematica quiere realizar el usuario con las matrices.
        #fun_val.controlador_decision(): sirve para enviar un apartado al usuario para que desida que ecuacion quiere realizar con 
        #las matrices antes creadas.
        print(F"{mensaje_operaciones}")
        
        desicion_ecuacion =fun_val.controlador_decision()
        
        #variable "matriz": sirve para guardar todas las matrices antes creadas y guardas en las lista "lista_matrices". 
        #Funcionalidad en el codigo: sirve para tener mayor comodidad al momento de guardar las matrices en cual funcion mas adelante.
        matriz = lista_matrices

    #if desicion_ecuacion == "Suma":
        #Funcionalidad en el codigo: realizar y verificar si las matrices son validas para realizar la suma
    if desicion_ecuacion == "Suma":
        #"condicion = fun_val.validar_tamanio_matrices(matriz)"
            #Funcionalidad en el codigo: llamar a la funcion "fun_val.validar_tamanio_matrices(matriz)" para validar si las dimensiones de las matrices
            #son validadas para realizar la suma
        #Variable "condicion": sirve para guardar el retorno de la funcion "fun_val.validar_tamanio_matrices(matriz)" la cual sera True o False si cumple las condiciones para la suma de matrices.  
        condicion = fun_val.validar_tamanio_matrices(matriz)
        
        #if condicion == True: 
            #Funcionalidad en el codigo: Si el retorno de la funcion "fun_val.validar_tamanio_matrices(matriz)" es de tipo "True" se podra realizar la operacion matematica seleccionada.
        if condicion == True: 
            #"fun_val.preparar_matriz(matriz)" : toma como parametro la funcion "matriz" con la cual se creara un diccionario que se necesitara para realizar la operacion seleccionada.
            fun_val.preparar_matriz(matriz)
            #diccionario_matriz: Guardar el diccionario con todas las matrices, creado en la funcion "fun_val.preparar_matriz(matriz)".
            diccionario_matriz = fun_val.preparar_matriz(matriz)
            
            #Variable "retorno" : sirva para guardar la salida de datos boolena de la funcion "fun_sum.suma_de_matrices(matriz,diccionario_matriz)".
            
            #Funcion "fun_sum.suma_de_matrices(matriz,diccionario_matriz)": Sirve para realizar la suma de matrices:
                #Funcionalida en el codigo: toma como parametro las variables "matriz" y "diccionario_matriz", con la cual realizara la suma de matrices (mas informacion en el paquete "operaciones_matrices" en el archivo "operacion_suma")
            print("=======================================================")
            retorno = fun_sum.suma_de_matrices(matriz,diccionario_matriz)
            
            #if retorno == False:
                #Funcionalida en el codigo: sirve para enviarle al usuario un mensaje de error si la variable "retorno" es == "False"
            if retorno == False:
                print("=======================================================")
                print("No se pudo realizar la operacion, ya que las dimensiones de las matrices no son compatibles para realizar una suma")
        
        if condicion == False:
            print("No se pudo realizar la operacion, ya que las dimensiones de las matrices no son compatibles para realizar una suma")
    #if desicion_ecuacion == "Resta":
        #Funcionalidad en el codigo: realizar y verificar si las matrices son validas para realizar la resta
    
    if desicion_ecuacion == "Resta":
        #"condicion = fun_val.validar_tamanio_matrices(matriz)"
            #Funcionalidad en el codigo: llamar a la funcion "fun_val.validar_tamanio_matrices(matriz)" para validar si las dimensiones de las matrices
            #son validadas para realizar la suma
        #Variable "condicion": sirve para guardar el retorno de la funcion "fun_val.validar_tamanio_matrices(matriz)" la cual sera True o False si cumple las condiciones para la suma de matrices.  
        condicion = fun_val.validar_tamanio_matrices(matriz)
        
        #if condicion == True: 
            #Funcionalidad en el codigo: Si el retorno de la funcion "fun_val.validar_tamanio_matrices(matriz)" es de tipo "True" se podra realizar la operacion matematica seleccionada.
        if condicion == True:
            #"fun_val.preparar_matriz(matriz)" : toma como parametro la funcion "matriz" con la cual se creara un diccionario que se necesitara para realizar la operacion seleccionada.
            fun_val.preparar_matriz(matriz)
            #diccionario_matriz: Guardar el diccionario con todas las matrices, creado en la funcion "fun_val.preparar_matriz(matriz)".
            
            diccionario_matriz = fun_val.preparar_matriz(matriz)
            
            #Variable "retorno" : sirva para guardar la salida de datos boolena de la funcion "fun_sum.suma_de_matrices(matriz,diccionario_matriz)".
            
            #Funcion "fun_res.resta_de_matrices(matriz,diccionario_matriz)": Sirve para realizar la suma de matrices:
                #Funcionalida en el codigo: toma como parametro las variables "matriz" y "diccionario_matriz", con la cual realizara la suma de matrices (mas informacion en el paquete "operaciones_matrices" en el archivo "operacion_resta")
            print("=======================================================")
            retorno = fun_res.resta_de_matrices(matriz,diccionario_matriz)
            
            #if retorno == False:
                #Funcionalida en el codigo: sirve para enviarle al usuario un mensaje de error si la variable "retorno" es == "False"
            if retorno == False:
                print("=======================================================")
                print("No se pudo realizar la operacion, ya que las dimensiones de las matrices no son compatibles para realizar una resta")
        if condicion == False:
            print("No se pudo realizar la operacion, ya que las dimensiones de las matrices no son compatibles para realizar una resta")
    
    #if desicion_ecuacion == "Multiplicacion":
        #Funcionalidad en el codigo: realizar y verificar si las matrices son validas para realizar la multiplicacion
    if desicion_ecuacion == "Multiplicacion":
        #diccionario_matriz: Guardar el diccionario con todas las matrices, creado en la funcion "fun_val.preparar_matriz(matriz)".
        diccionario_matriz = fun_val.preparar_matriz(matriz)
        
        #Funcion "fun_mul.multiplicacion_de_matrices(matriz,diccionario_matriz)": Sirve para realizar la multiplicacion de matrices:
                #Funcionalida en el codigo: toma como parametro la variable "diccionario_matriz", con la cual realizara la multiplicacion de matrices (mas informacion en el paquete "operaciones_matrices" en el archivo "operacion_multiplicacion")
        print("=======================================================")
        retorno = fun_mul.multiplicar_matrices(diccionario_matriz)
        #if retorno == False:
                #Funcionalida en el codigo: sirve para enviarle al usuario un mensaje de error si la variable "retorno" es == "False"
        if retorno == False:
            print("Las dimenciones de las matrices no son compatibles para multiplicarse")
        else:
            print("El resultado de la multiplicacion es ")
            print(retorno)
#Limpiar lista con las matrices anteriormente trabajadas
lista_matrices.clear()