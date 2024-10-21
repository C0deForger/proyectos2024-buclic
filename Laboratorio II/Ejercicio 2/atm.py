from lecutra_de_datos import lectura_del_txt
from retirar_dinerio import Retiro_de_dinero
from actualizar_saldo import actualizar_saldo
from crear_cuenta import crear_usuario
from encriptar import desencriptar_contrasenia_ascii,encriptar_contrasenia_ascii

class ATM:
    def __init__(self,usuario:str,password:str,dui:str):
        self.usuario = usuario
        self.password = password
        self.dui = dui 
    #en este metodo nos aseguramos de que las credenciales sean correctas
    def buscar_usuario(self):
        """Esta función nos ayuda a validar que el usuario ingrese correctamente su usuario o contrasenia

        Args:
            user (str): El usuario con el que esta registrado 
            password (str): La contrasenia que guardo el usuario para poder usar su cuenta

        Returns:
            bool: Si el usuario es correcto imprimira un mensaje de bienvenida, de lo contrario retornara False 
        """
        condicional_contra = False
        condicional_dui = False
        lecutra_de_datos = lectura_del_txt()
        #print(f"Contraseña ingresada: {self.password}")
        #print(f"DUI ingresado: {self.dui}")

        # Bandera que indica si hemos encontrado una coincidencia completa
        acceso_conseguido = False

        # Recorremos todas las entradas en la base de datos
        for dui, datos in lecutra_de_datos.items():
        # Si el DUI ingresado coincide con el DUI de la base de datos
            if self.dui == dui:
                # Comparamos la contraseña
                if self.password == datos["CONTRASENIA"]:
                    # Verificamos si el DUI también coincide
                    if self.usuario == datos["NOMBRE"]:
                        acceso_conseguido = True  # Marcamos que encontramos una coincidencia completa
                        break# Salimos del bucle ya que hemos encontrado el usuario correcto
        # Verificar si se encontró una coincidencia completa
        if acceso_conseguido == True:
            print("Acceso conseguido")
            return True
        else:
            print("Usuario, contraseña o DUI incorrectos")
            return False
    #Metodo en donde el usuario podra  retirar dinero de su cuenta
    def retirar_dinero(self):
        total_retirado = 0
        #mientras que el usuario no ingrese un valor numerico se repetira
        while True:
            try:
                cantidad_retirar=int(input("Ingrese la cantidad que desea retirar: "))
                #si esto no da un error continuara sin llegar al except, de lo contrario se repetira
                if cantidad_retirar >= 5:
                    break
                else:
                    print("Invalido, Solo puede retirar una suma mayor o igual de 5 dolares")
            except ValueError:
                print("Ingrese una cantidad numerica!")
            
                
        Retiro_de_dinero(self.dui,cantidad_retirar)
        if  cantidad_retirar%5 == 0:
            return cantidad_retirar
        else:
            cantidad_retirar = 0
            return cantidad_retirar
    
    
    #Metodo donde el usuario obtendra el saldo actual de su cuenta 
    def Obtener_saldo(self):
        """
        por medio de la informacion ingresada por el usuario obtendremos el saldo actual
        
        Returns:
            float: saldo aldo actual del usuario 
        """
        saldo = ""
        dict_users= lectura_del_txt()
        #unico cambio en  este metodo es que se obtiene el saldo del usuario
        
        saldo= dict_users[self.dui]["SALDO"] 
        return saldo 
    #Metodo para que el usuario puede  depositar dinero en su cuenta
    def ingresar_dinero(self):
        """
        Este metodo se apoyar en los metodos de actualizar saldo y obtener saldo
        con el saldo actual botenido se le agrega la cantidad que desea ingresar el usuario
        y se le actualiza en la base de datos
        Args:
            usuario (str): nombre ingresado por el usuario
            nuevo_ingreso (float): Cantidad a agregar
        """
        for i in range(3):
            try:
                nuevo_ingreso=float(input("Ingrese la cantidad de dinero que desea ingresar: "))
                break
            except ValueError:
                print("Ingrese una cantidad numerica entera! intentos restantes:" ,  (3-(i+1)) )

        dict_users=lectura_del_txt()
        
        saldoactual=dict_users[self.dui]["SALDO"] 

        
        if not isinstance(saldoactual, (int, float)):
            print(saldoactual)
            return
        
        if nuevo_ingreso<=0:
            print("CANTIDAD INVALIDA")
            return
            
        nuevo_saldo=saldoactual+nuevo_ingreso
        actualizar_saldo(self.dui,nuevo_saldo)
        print(f"SU DEPOSITO FUE HECHO CORRECTAMENTE! \nSU NUEVO SALDO ES DE {nuevo_saldo}\n")  
        return nuevo_saldo
        
    def mostrar_informacion_del_usuario(self):
        """
        Metodo que mediante la informacion  del usuario y la base de datos mostrara todos los datos que se tienen del usuario
        """
        datos=lectura_del_txt()
        
        
        contraseniadesc = desencriptar_contrasenia_ascii(datos[self.dui]["CONTRASENIA"])
        
        datos[self.dui]["CONTRASENIA"] = contraseniadesc
        
        print(f"""
            Nombre: {datos[self.dui]["NOMBRE"]} 
            Saldo: {datos[self.dui]["SALDO"]}
            DUI: {self.dui}
            CONTRASENIA: {datos[self.dui]["CONTRASENIA"]}
            """ )