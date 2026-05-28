from Funciones import *
from Inputs import *
from Prints import *


def mostrar_menu()-> None:
        
    opcion = -1    
    votos = []          
    hay_votos = False   #Valida si fueron cargados los votos para Opnción 2, ayuda de IA

    
    while opcion != 0:
        limpiar_consola()
        print("══════════ ELECCIONES UTN FRA ══════════")
        print("1. Cargar votos")
        print("2. Mostrar votos")
        print("3. Partidos con menos del 10 % de votos")
        print("4. Partidos con menos del 15 % de votos")
        print("5. Partidos con menos del 20 % de votos")
        print("6. Partidos con más de 500 votos")
        print("7. Partidos con más de 1000 votos")
        print("8. Partidos por encima del promedio")
        print("9. Partido menos votado")
        print("10. Verificar segunda vuelta")
        print("11. Hardcodear vector")
        print("12. Ordenar partidos políticos por nombre")
        print("0. Salir")
        print("════════════════════════════════════════")

        opcion = ingresar_entero("Ingrese una opción: ", "❌Error. Los datos ingresados no son válidos.")

        match opcion:
            case 1:
                limpiar_consola()
                print("🗳️  *** CARGA DE VOTOS *** 🗳️")
                votos = cargar_votos()
                hay_votos = True
                esperar_enter()
            case 2:
                limpiar_consola()
                if hay_votos == True:
                    mostrar_resultados(votos)
                    esperar_enter()
                else:
                    print("⚠️  Los votos no fueron cargados")
                    esperar_enter()
            case 3:
                limpiar_consola()
                if hay_votos == True:
                    mostrar_porcentajes(votos, 10)
                    esperar_enter()
                else:
                    print("⚠️  Los votos no fueron cargados")
                    esperar_enter()
            case 4:
                limpiar_consola()
                if hay_votos == True:
                    mostrar_porcentajes(votos, 15)
                    esperar_enter()
                else:
                    print("⚠️  Los votos no fueron cargados")
                    esperar_enter()
            case 5:
                limpiar_consola()
                if hay_votos == True:
                    mostrar_porcentajes(votos, 20)
                    esperar_enter()
                else:
                    print("⚠️  Los votos no fueron cargados")
                    esperar_enter()
            case 6:
                limpiar_consola()
                if hay_votos == True:
                    mostrar_partidos_con_mas_votos(votos, 500)
                    esperar_enter()
                else:
                    print("⚠️  Los votos no fueron cargados")
                    esperar_enter()
            case 7:
                limpiar_consola()
                if hay_votos == True:
                    mostrar_partidos_con_mas_votos(votos, 1000)
                    esperar_enter()
                else:
                    print("⚠️  Los votos no fueron cargados")
                    esperar_enter()
            case 8:
                limpiar_consola()
                if hay_votos == True:
                    mostrar_partidos_con_mayor_promedio(votos)
                    esperar_enter()
                else:
                    print("⚠️  Los votos no fueron cargados")
                    esperar_enter()



            case 0:
                print("Hasta luego!! ✌️")
            case _:
                print("❌  Opción Inválida. Vuelva a intentarlo")
                esperar_enter()

        
        