'''Esta función validará que la cantidad recibida (como una cadena) pueda cargarse en un tipo int. Sólo valdrán números positivos.
   Si la validación es correcta, devolverá la cantidad como un número, en caso contrario devolverá None.
   Si se introduce una N la devuelve ya que será la condición de no validar nada.'''
def valIntOrN(strNum):
    if strNum.upper() == "N":
        return strNum.upper()
    
    try:
        num = int(strNum)
        if num <= 0:
            num = None
    except:
        num = None

    return num

def solIntOrN(mensaje, **params):    
    num = None
    while num == None:
        num = valIntOrN(input(mensaje))
        if num == "N":
            return num
        elif num == None:
            print("\t\t\t\t\t\tIntroduce un valor entero positivo o una N.")
        elif 'minimo' in params and num < params['minimo']:
            num = None
            print("\t\t\t\t\t\tIntroduce un valor mayor que {}.".format(params['minimo']))
        elif 'maximo' in params and num > params['maximo']:
            num = None
            print("\t\t\t\t\t\tIntroduce un valor menor que {}.".format(params['maximo']))
    
    return num