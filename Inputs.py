def ingresar_entero(mensaje: str, mensaje_error: str) -> int:
    """
    Solicita al usuario el ingreso de un número entero positivo y valida
    que la cadena ingresada represente un número entero válido.

    Args:
        mensaje (str): Texto que se muestra al usuario para solicitar el ingreso del número.
        mensaje_error (str): Texto que se muestra cuando el dato ingresado no es válido.

    Returns:
        int: Número entero válido ingresado por el usuario.
    """

    numero = input(mensaje)

    while validar_cadena_entero(numero) == False:
        print(mensaje_error)
        numero = input(mensaje)

    numero = int(numero)
    return numero
   

def validar_cadena_entero(cadena: str) -> bool:
    """
    Verifica si una cadena representa un número entero válido.
    Utilizando código ASCII

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si la cadena contiene solo dígitos, False en caso contrario.
    """
    if len(cadena) > 0:
        retorno = True
        for i in range(len(cadena)):
            caracter = cadena[i]
            caracter_ascii = ord(caracter)
            if caracter_ascii > 57 or caracter_ascii < 48:
                retorno = False
                break
    else:
        retorno = False

    return retorno
