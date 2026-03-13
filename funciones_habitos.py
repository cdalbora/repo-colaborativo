lista_act =[]

def registrar_habitos():
    pregunta = input("¿Quiere ingresar una actividad? ")
    while pregunta == "si":
        actividad = input("¿Que actividad realizó? ")
        lista_act.append(actividad)
        pregunta = input("¿Quiere ingresar una actividad? ") 
        if pregunta == "no": 
            break 
        

    