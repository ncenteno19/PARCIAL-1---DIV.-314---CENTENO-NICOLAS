import subprocess
import os

from Inputs import *

def limpiar_consola():
    """
    Función que limpia consola vista en clase
    """
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

def esperar_enter() -> None:
    """
    Función para esperar un Enter para continuar vista en clase
    """
    print("")
    input("Ingresá ENTER para Volver al Menú...")

# El punto 1 b) indica que no se permiten Ceros, pero podría ser que un partido no reciba votos.
# Por dicho motivo no restringí la carga de Cero votos. 
# En caso de restringirlo se podría ingresar un declarar una variable y if 
# variable == 0 entonces realizar un mensaje de error 
def cargar_votos(partidos: int = 5) -> list:
    """
    Solicita y carga la cantidad de votos de cada partido político.

    Args:
        partidos (int): Cantidad de partidos a cargar.

    Returns:
        list: Lista con los votos ingresados para cada partido.
    """
    votos = []
    for i in range(partidos):
        votos.append(ingresar_entero(f"Ingrese los votos del {i+1}° partido: ",
                                   "❌ Error. El dato ingresado no es válido."))
    return votos

def sumar_votos(votos: list) -> int:
    """
    Calcula la suma total de los votos registrados.

    Args:
        votos (list): Lista de votos por partido.

    Returns:
        int: Total de votos acumulados.
    """
    suma = 0
    for i in range(len(votos)):
        suma += votos[i]
    return suma

# NOTA: VERIFICAR SI AL FINAL LA VALIDACION DE LA DIV. POR 0 NO ESTÁ DE MÁS
# YA QUE TAMBIEN SE VALIDA EN EL INPUT
def calcular_porcentaje(cantidad_votos: int, total_votos: int, 
                        mensaje_error: str = "❌ División por 0") -> float:
    """
    Calcula el porcentaje de votos de un partido sobre el total de votos.

    Args:
        votos (int): Cantidad de votos del partido.
        total (int): Total de votos emitidos.
        mensaje_error (str): Mensaje a mostrar si el total es cero.

    Returns:
        float: Porcentaje calculado o None si no es posible realizar la división.
    """
    if total_votos == 0:
        print(mensaje_error)
    else:
        return cantidad_votos / total_votos * 100
    
def calcular_promedio(total_votos: int, cantidad_partidos: int,
                      mensaje_error: str = "❌ División por 0") -> float:
    
    if cantidad_partidos == 0:
        print(mensaje_error)
    else:
        return  total_votos / cantidad_partidos 
  
def convertir_lista_en_titulos(lista_nombres: list) -> list:
    """
    Convierte una lista de nombres al formato título.

    Cada nombre se pasa primero a minúscula, luego a formato título
    (primera letra de cada palabra en mayúscula) y finalmente se ajusta
    la preposición "De" a "de" cuando corresponde.

    Args:
        lista_nombres (list): Lista de nombres de partidos políticos.

    Returns:
        list: Lista de nombres convertidos a formato título.
    """

    for i in range (len(lista_nombres)):
        nombre = convertir_a_minuscula(lista_nombres[i])
        nombre = convertir_en_titulo(nombre)
        nombre = convertir_De_en_de(nombre) # este punto puede omitirse si se desea

        lista_nombres[i] = nombre
    
    return lista_nombres
                       
def convertir_a_minuscula(nombre: str, mensaje_error: str = "❌ Error en tipo de dato") -> str:

    """
    Convierte una cadena de texto a minúsculas utilizando códigos ASCII.

    Args:
        nombre (str): Cadena a convertir.
        mensaje_error (str): Mensaje a mostrar si el dato no es una cadena.

    Returns:
        str: Cadena convertida a minúsculas.
    """
  
    if type(nombre) != str:
        print(mensaje_error)
    else:
        cadena_copia = ""
        for i in range(len(nombre)):
            caracter_ascii = ord(nombre[i])
            # Si están en Mayúscula las pasa a minúscula
            if caracter_ascii > 64 and caracter_ascii < 91:
                cadena_copia += chr(caracter_ascii + 32)
            else:
                cadena_copia += chr(caracter_ascii)
        return cadena_copia

def convertir_en_titulo(nombre:str, mensaje_error: str = "❌ Error en tipo de dato") -> str:
    #Debe recibir una cadena en minúscula

    """
    Convierte una cadena en minúscula al formato título.

    La primera letra del texto y la primera letra después de cada espacio
    se convierten a mayúscula, utilizando códigos ASCII.

    Args:
        nombre (str): Cadena en minúscula.
        mensaje_error (str): Mensaje a mostrar si el dato no es una cadena.

    Returns:
        str: Cadena convertida a formato título.
    """

    if type(nombre) != str:
        print(mensaje_error)
    else:
        cadena_copia = ""
        for i in range(len(nombre)):
            caracter_ascii = ord(nombre[i])

            if i == 0 or nombre[i-1] == " ": 
                cadena_copia += chr(caracter_ascii - 32) #Si recibe una cadena en Mayuscula escribiría caracteres del 33 al 58
            else:
                cadena_copia += chr(caracter_ascii)

        return cadena_copia

def convertir_De_en_de (nombre: str, mensaje_error: str = "❌ Error en tipo de dato") -> str:

    """
    Reemplaza la palabra "De" por "de" cuando se encuentra entre espacios.

    La conversión se realiza verificando manualmente los caracteres
    adyacentes, sin utilizar métodos de la clase string.

    Args:
        nombre (str): Cadena en formato título.
        mensaje_error (str): Mensaje a mostrar si el dato no es una cadena.

    Returns:
        str: Cadena con la corrección de "De" a "de".
    """

    if type(nombre) != str:
        print(mensaje_error)
    else:
        cadena_copia = ""
        for i in range(len(nombre)):
            caracter_ascii = ord(nombre[i])
            
            if (i >= 1 and 
                i + 2 < len(nombre) and 
                nombre[i-1] == " " and 
                nombre[i] == "D" and 
                nombre[i+1] == "e" and 
                nombre[i+2] == " "):

                cadena_copia += "d"

            else:
                cadena_copia += chr(caracter_ascii)


        return cadena_copia

def ordernar_menor_mayor(vector:list) -> bool:

    """
    Ordena una lista de valores numéricos de menor a mayor.

    El ordenamiento se realiza utilizando un algoritmo de comparación
    con intercambio de valores (tipo burbuja). La función modifica la
    lista original.

    Args:
        vector (list): Lista de valores a ordenar.

    Returns:
        bool: True si el parámetro es una lista y se intentó ordenar,
              False en caso contrario.
    """
    
    retorno = False
    if type(vector) == list:
        retorno = True
        for izq in range(len(vector) - 1):
            for der in range((izq + 1),len(vector)):
                if vector[izq] > vector[der]:
                    intercambiar_valores(vector,izq,der)

    return retorno

def intercambiar_valores(vector:list,izq:int,der:int) -> None:

    """
    Intercambia los valores de dos posiciones de una lista.

    Utiliza una variable auxiliar para realizar el intercambio
    entre los índices indicados.

    Args:
        vector (list): Lista en la que se realiza el intercambio.
        izq (int): Índice del primer elemento.
        der (int): Índice del segundo elemento.

    Returns:
        None
    """

    aux_izq = vector[izq]
    vector[izq] = vector[der]
    vector[der] = aux_izq
