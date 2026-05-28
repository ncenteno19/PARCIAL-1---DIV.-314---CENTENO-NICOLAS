from Funciones import *

def mostrar_resultados(votos: list, mensaje_error: str = "❌ Se cargaron CERO votos") -> None:
    
    """
    Muestra en pantalla los resultados de la votación por partido político.

    Para cada partido se informa la cantidad de votos obtenidos y el
    porcentaje que representa sobre el total de votos. Si no hay votos
    cargados, se muestra un mensaje de error.

    Args:
        votos (list): Lista con la cantidad de votos por partido.
        mensaje_error (str): Mensaje a mostrar si no hay votos cargados.

    Returns:
        None
    """
 
    suma = sumar_votos(votos)
    if suma == 0:
        print(mensaje_error)
    else:
        print("══════════ 📝📊 RESULTADOS DE LA VOTACIÓN 📊 📝 ══════════\n")

        for i in range(len(votos)):
            print("────────────────────────────────")
            print(f"Partido {i+1}°")
            print(f"Cantidad de votos  : {votos[i]}")
            print(f"Porcentaje         : {calcular_porcentaje(votos[i],suma):.2f} %")
        
        print("══════════════════════════════════════════════════════════")
        print(f"En esta elección se presentaron: {i+1} partidos político")
        print(f"Votaron un total de: {suma} alumnos")

def mostrar_porcentajes(votos: list, porcentaje: int,
                        mensaje_error1: str = "❌ Se cargaron CERO votos",
                        mensaje_error2: str = "❌ No hay partidos con esas características") -> None:
    """
    Muestra los partidos políticos cuyo porcentaje de votos es menor
    al valor indicado.

    Args:
        votos (list): Lista con la cantidad de votos por partido.
        porcentaje (int): Porcentaje límite para filtrar los partidos.
        mensaje_error1 (str): Mensaje a mostrar si no hay votos cargados.
        mensaje_error2 (str): Mensaje a mostrar si ningún partido cumple la condición.

    Returns:
        None
    """

   
    suma = sumar_votos(votos)
    if suma == 0:
        print(mensaje_error1)
    else:

        print(f"*** 📉 PARTIDOS CON MENOS DE {porcentaje}% 📉 ***\n")

        acumulado = 0
        for i in range(len(votos)):
            porcentaje_parcial = calcular_porcentaje(votos[i],suma)
            if porcentaje_parcial < porcentaje:
                acumulado += porcentaje_parcial
                print("────────────────────────────────")
                print(f"Partido {i+1}°")
                print(f"Cantidad de votos  : {votos[i]}")
                print(f"Porcentaje         : {porcentaje_parcial:.2f} %")
        
        print("══════════════════════════════════════════════════════════")
        if acumulado == 0:
            print(mensaje_error2)
        else:
            print(f"El porcentaje acumulado en la búsqueda: {acumulado:.2f} %")

#Nombre de función recomendado por IA, en mi opinión largo pero entendible
# Yo había puesto mostrar_votos pero me corrigió indicando que no muestra todos lo votos.
def mostrar_partidos_con_mas_votos(votos: list, cantidad_votos: int,
                        mensaje_error1: str = "❌ Se cargaron CERO votos",
                        mensaje_error2: str = "❌ No hay partidos con esas características") -> None:
    """
    Muestra los partidos políticos que superan una cantidad mínima de votos.

    Para cada partido que cumple la condición se informa la cantidad de votos
    obtenidos y el porcentaje que representan sobre el total. Al finalizar,
    se muestra un resumen con la suma de votos, la cantidad de partidos
    encontrados y el promedio de votos.

    Args:
        votos (list): Lista con la cantidad de votos por partido.
        cantidad_votos (int): Cantidad mínima de votos para filtrar los partidos.
        mensaje_error1 (str): Mensaje a mostrar si no hay votos cargados.
        mensaje_error2 (str): Mensaje a mostrar si ningún partido cumple la condición.

    Returns:
        None
    """
   
    suma = sumar_votos(votos)
    if suma == 0:
        print(mensaje_error1)
    else:

        print(f"*** 📈 PARTIDOS CON MÁS DE {cantidad_votos} 📈 ***\n")

        acumulado = 0
        cantidad_partidos = 0
        for i in range(len(votos)):            
            if cantidad_votos < votos[i]:
                porcentaje_parcial = calcular_porcentaje(votos[i],suma)
                acumulado += votos[i]
                cantidad_partidos += 1 
                print("────────────────────────────────")
                print(f"Partido {i+1}°")
                print(f"Cantidad de votos  : {votos[i]}")
                print(f"Porcentaje         : {porcentaje_parcial:.2f} %")
        
        print("═══════════════════════════════════════════════════════")
        if acumulado == 0:
            print(mensaje_error2)
        else:
            print("══════════ 🔢 SUMA TOTALES DE LA BUSQUEDA 🔢 ══════════")
            print(f"(1) La suma de los votos    : {acumulado}")
            print(f"(2) Cantidad de partidos    : {cantidad_partidos}")
            print(f"(3) Promedio de votos       : {(acumulado / cantidad_partidos):.2f}")
            print("═══════════════════════════════════════════════════════")    


def mostrar_partidos_con_mayor_promedio(votos: list, 
                        mensaje_error1: str = "❌ Se cargaron CERO votos",
                        mensaje_error2: str = "❌ No hay partidos con esas características") -> None:
    """

    """
   
    suma = sumar_votos(votos)
    if suma == 0:
        print(mensaje_error1)
    else:

        print(f"*** 📈 PARTIDOS POR ENCIMA DEL PROMEDIO 📈 ***\n")
        promedio = calcular_promedio(suma)
        print(f"(1) Promedio general de votos: {promedio}")


        porcentaje_acum = 0
        
        for i in range(len(votos)):            
            if promedio < votos[i]:
                porcentaje_parcial = calcular_porcentaje(votos[i],suma)
                porcentaje_acum += porcentaje_parcial 
                print("────────────────────────────────")
                print(f"Partido {i+1}°")
                print(f"Cantidad de votos  : {votos[i]}")
                print(f"Porcentaje         : {porcentaje_parcial:.2f} %")
        
        print("═══════════════════════════════════════════════════════")
        
        if porcentaje_acum == 0:
            print(mensaje_error2)
        else:
            print(f"(2) Procentaje acumulado de los resultados: {porcentaje_acum:.2f} %")

    