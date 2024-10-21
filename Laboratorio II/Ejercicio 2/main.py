from continuar_operando import continuar
from crear_cuenta import crear_usuario
from encriptar import encriptar_contrasenia_ascii
from atm import ATM
from Collet_Data_Users import Collet_Data_User,Mostrar_factura


dinero_total_retirado = 0
dinero_retirado = 0
saldo_en_cuenta = 0
collet_data_list = set()
#bucle que sera infinito, porque los ATM no paran de funcionar una vez el usuario termina de usarlo
while True:
    
    #lo primero que se hace es presentar al usuario la opcion de ingresar a su cuenta  o crear una cuenta
    print("\nBienvenido!")
    #Presentamos las opciones del atm al usuario
    print("1-Acceder a cuenta \n2-Crear cuenta\n")
    #le pedimos que seleccione la operación a realizar
    acces=input(">")
    #si el usuario ingreso 1 se procedera a pedir que ingrese los datos de su cuenta, tendra 3 intentos
    if acces=="1":
        for i in range(3):
            user=input("Ingrese su usuario:  ")
            contrasenia=input("Ingrese su contrasenia: ")
            dui = input("Ingrese su numero de DUI: ")
            contrasenia= encriptar_contrasenia_ascii(contrasenia)
            #damos los parametros a clase atm y se almacenaran en el objeto usuarioactual
            usuarioActual=ATM(user,contrasenia,dui)
            if  usuarioActual.buscar_usuario()==False:
                print("ERROR! Datos incorrectos")
                print("Intentos restantes: ",(3-(i+1)),"")
                #esto es para que no entre en el bucle para los usuarios que si estan registrados
                bucle=False
            #si el usuario ingresa un usuario y contrasenia valida  se le mostrara el menu de opciones
            else:
                #esto es para que entre en el bucle siguiente
                bucle=True
                break
    elif acces=="2":
        bucle=crear_usuario()
    else:
        print("Opcion no valida!")
        bucle=False
       



    #esto se repetira tantas veces como el usuario quiera seguir usando el atm
    while bucle:
        print("""
            Que operación desea realizar:
            1-Retiro de dinero
            2-Ingresar Dinero
            3-Consultar Saldo
            4-Consultar informacion personal

            """)
        op=input(">")

        if op=="1":
            #mientras que el usuario no ingrese un valor numerico se repetira
            dinero_retirado = usuarioActual.retirar_dinero()
            dinero_retirado = int(dinero_retirado)
            saldo_en_cuenta = usuarioActual.Obtener_saldo()
            dinero_total_retirado+=dinero_retirado
            #entrar en esta funcion presenta al usuario la opcion de continuar operando
            selct_user = "Retiro de dinero"
            collet_data_list.add(selct_user)
            if continuar() is False:
                break
                
                
        elif op=="2":

            usuarioActual.ingresar_dinero()
            
            saldo_en_cuenta = usuarioActual.Obtener_saldo()
            selct_user = "Ingresar Dinero"
            collet_data_list.add(selct_user)
            if continuar() is False:
                break 
        elif op=="3":
            #llama la funcion obtner saldo para poder retornarle el saldo del usuario
            print("Su saldo es de: $",usuarioActual.Obtener_saldo())
            saldo_en_cuenta =  usuarioActual.Obtener_saldo()

            selct_user = "Consultar Saldo"
            collet_data_list.add(selct_user)
            if continuar() is False:
                break
                
        elif op=="4":
            #Usamos el metodo que muestra la información del usuario
            usuarioActual.mostrar_informacion_del_usuario()
            #del metodo botener saldo, obtenemos el saldo del usuario
            saldo_en_cuenta = usuarioActual.Obtener_saldo()
            
            selct_user = "Consultar informacion personal"
            collet_data_list.add(selct_user)
            #funcion para validar si el usuario desea realizar otra operación 
            if continuar() is False:
                break 
        #si el usuario solicita hacer una operacion distintas de las presentadas o si ingresa un simbolo o caracter no valido    
        else:
            print("OPCION INVALIDA! ")
      
    
            
    #si el usuario entro en el bucle para realizar transacciones entonces se le presentara su respectiva factur y mensaje de despedida
    
    if bucle is True:            
        Collet_Data_User(user,collet_data_list,dinero_total_retirado,saldo_en_cuenta)
        Mostrar_factura()
        print("\nFeliz Día")
        print()  


