

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

    
def analizar_habitos(lista):
    '''
    Analiza la lista de actividades y cuenta cuántas veces aparece cada una.

    Parameters
    ----------
    lista : list
        Lista de actividades ingresadas por el usuario.

    Returns
    -------
    dict
    Diccionario con cada actividad y la cantidad de veces que aparece.

    '''
    
    resultado = {}
    for actividad in lista:
        if actividad in resultado:
            resultado[actividad] += 1
        else:
            resultado[actividad] = 1
            
    return resultado
