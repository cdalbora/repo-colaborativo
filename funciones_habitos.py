

def registrar_habitos():
    """
    Pregunta si quiere ingresar actividad. Si quiere se guarda en una lista
    
    

    Returns
    -------
    lista_act: lista 
    Lista de actividades ingresadas por el usuario 
    """
    lista_act =[]
    pregunta = input("¿Quiere ingresar una actividad? ")
    while pregunta == "si":
        actividad = input("¿Que actividad realizó? ")
        lista_act.append(actividad)
        pregunta = input("¿Quiere ingresar una actividad? ") 
        if pregunta == "no": 
            break 
    return lista_act 

    