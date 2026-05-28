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


def ordenar_lista(lista_nombres: list) -> list:
    for i in range (len(lista_nombres)):
        nombre = lista_nombres[i]
        for j in range(len(nombre[j])):
            if ord











