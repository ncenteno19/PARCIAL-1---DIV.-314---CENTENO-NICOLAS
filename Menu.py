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

        opcion = ingresar_entero("Ingrese una opción: ", "❌ Error. Los datos ingresados no son válidos.")

        if (opcion > 1 and opcion < 11) and hay_votos == False:
            print("⚠️  Los votos no fueron cargados")
            esperar_enter()

        else:    
            match opcion:
                case 1:
                    limpiar_consola()
                    print("🗳️  *** CARGA DE VOTOS *** 🗳️")
                    votos = cargar_votos()
                    hay_votos = True
                    esperar_enter()
                case 2:
                    limpiar_consola()
                    mostrar_resultados(votos)
                    esperar_enter()
                case 3:
                    limpiar_consola()
                    mostrar_porcentajes(votos, 10)
                    esperar_enter()
                case 4:
                    limpiar_consola()
                    mostrar_porcentajes(votos, 15)
                    esperar_enter()  
                case 5:
                    limpiar_consola()
                    mostrar_porcentajes(votos, 20)
                    esperar_enter()
                case 6:
                    limpiar_consola()
                    mostrar_partidos_con_mas_votos(votos, 500)
                    esperar_enter()
                case 7:
                    limpiar_consola()
                    mostrar_partidos_con_mas_votos(votos, 1000)
                    esperar_enter()
                case 8:
                    limpiar_consola()
                    mostrar_partidos_con_mayor_promedio(votos)
                    esperar_enter()
                case 9:
                    limpiar_consola()
                    mostrar_partidos_menos_votados(votos)
                    esperar_enter()
                case 10:
                    limpiar_consola()
                    verificar_segunda_vuelta(votos)
                    esperar_enter()
                case 11:
                    limpiar_consola()
                    votos = [888,555,333,1850,999,777,1400,180,2500,60]
                    hay_votos = True
                    print("*** 🧾 DATOS HARDCODEADOS 🧾 ***")
                    print("✅ Los votos fueron hardcodeados")
                    print(f"📊 Nuevo valores de los votos: {votos}")
                    print("")
                    esperar_enter()
                case 12:
                    limpiar_consola()
                    lista_nombres = ["frente hola mundo","alianza Scarafilo",
                                    "La libertad de Baus","unidad de Python","Frente de Java"]
                    mostrar_lista_nombres_ordenada(lista_nombres)
                    esperar_enter()  
                case 0:
                    print("Hasta luego!! ✌️")
                case _:
                    print("❌  Opción Inválida. Vuelva a intentarlo")
                    esperar_enter()
