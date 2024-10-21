from lecutra_de_datos import lectura_del_txt
from actualizar_saldo import actualizar_saldo
def Retiro_de_dinero(dui:str,cantidad_a_retirar:int):
    """
    Este metodo se encarga del retiro del dinero, a su vez trabaja con el metodo de modificacion de saldo
    si coinciden los datos de usuario procedera a restar el saldo que se tiene con la cantidad a retirar
    tambien procedera con el calculo de cuantos billetes retornara al usuario
    """
    #obtengo el saldo
    validar_retiro=cantidad_a_retirar%5
    if validar_retiro!=0:
        print(f"CANTIDAD NO VALIDA! no se puede dar billetes de $1")
        return 
    dict_users=lectura_del_txt()
    saldo=dict_users[dui]["SALDO"]
    if not isinstance(saldo, (int, float)):
        print(saldo)
        return
        
    elif saldo < cantidad_a_retirar:
        print("SU SALDO ES INSUFICIENTE PARA LLEVAR ACABO ESTA OPERACION!")
        return
    else:
        Nuevo_Saldo=saldo-cantidad_a_retirar
        actualizar_saldo(dui,Nuevo_Saldo)
        print(f"""SU RETIRO DE || ${cantidad_a_retirar} ||FUE HECHO CON EXITO! \nSU SALDO RESTANTE ES: {Nuevo_Saldo}\n""")
        
    #menor o igual a 15                  
    if cantidad_a_retirar <= 15:
        billetes_5=round(cantidad_a_retirar/5)
        print(f"Se daran ${billetes_5*5} como {billetes_5} billetes de $5")
            

    #mayor a 15 y menor o igual a 50               
    elif cantidad_a_retirar>15 and cantidad_a_retirar<=50:
        #75% EN DE $10
        billetes_10= round((cantidad_a_retirar/10)*0.75)
        Restante=cantidad_a_retirar-(billetes_10*10)
        print(f"Se daran ${billetes_10*10} como {billetes_10} billetes de $10")
        #EL RESTO EN DE A $5
        billetes_5=round(Restante/5)
        Restante=Restante-(billetes_5*5)
        print(f"Se daran ${billetes_5*5} como {billetes_5} billetes de $5")

    #mayor a 50 y menor o igual 100
    elif cantidad_a_retirar>50 and cantidad_a_retirar<=100:
        #50%  EN DE $20
        billetes_20=round((cantidad_a_retirar/20)*0.5)
        Restante=cantidad_a_retirar-(billetes_20*20)
        print(f"Se daran ${billetes_20*20} como {billetes_20} billetes de $20")
        #75% en de a $20
        billetes_10=round((Restante/10)*0.75)
        Restante=Restante-(billetes_10*10)
        print(f"Se daran ${billetes_10*10} como {billetes_10} billetes de $10")
        #el restante hago entrega en $5
        billetes_5=round(Restante/5)
        print(f"Se daran ${billetes_5*5} como {billetes_5} billetes de $5")
        
    #mayor de 100
    elif cantidad_a_retirar>100:
        #50% EN BILLETES DE $20
        billetes_20=round((cantidad_a_retirar/20)*0.5)
        Restante=cantidad_a_retirar-(billetes_20*20)
        print(f"Se daran ${billetes_20*20} como  {billetes_20} billetes de $20")
        #UN 40% EN DE $10, lo multiplico por %80, porque ya reste 50% inicialmente, por eso el 50% restan es un 100% ahora
        billetes_10 = round((cantidad_a_retirar / 10) * 0.4)
        Restante=Restante-(billetes_10*10)
        print(f"Se daran ${billetes_10*10} como {billetes_10} billetes de $10")
        #EL RESTANTE EN $5
        billetes_5=round((Restante/5))
        Restante=Restante-(billetes_5*5)
        print(f"Se daran ${billetes_5*5} como {billetes_5} billetes de $5")

