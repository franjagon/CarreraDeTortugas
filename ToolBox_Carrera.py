'''Esta función validará que la cantidad recibida (como una cadena) pueda cargarse en un tipo int. Sólo valdrán números positivos.'''
def valIntOrN(strNum):
    '''Si recibe una N, la devuelve mayúscula, ya que será la condición para no validar nada.'''
    if strNum.upper() == "N":
        return strNum.upper()
    
    '''Si la validación es correcta, devolverá una cantidad como un número, en caso contrario devolverá None.'''
    try:
        num = int(strNum)
        if num <= 0:
            num = None
    except:
        num = None

    return num

'''Esta función solicitará la validación de una cantidad requerida. Podrá recibir un valor límite mínimo y/o un valor límite máximo.'''
def solIntOrN(mensaje, **params):    
    num = None
    
    '''La función solicitará una cantidad para ser validada mientras no reciba un valor que considere válido (para devolverlo).'''
    while num == None:
        num = valIntOrN(input(mensaje))
        
        '''Si recibe una N, la devuelve, ya que será la condición de salida.
           Si la validación es incorrecta (recibe None), da un mensaje de error.
           Si recibe un entero y tiene un limite mínimo/máximo parametrizado, comprueba que es mayor/menor (si no lo es lo descarta).'''
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