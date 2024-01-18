
#         equipo: 'xxx',
#         pj: 0, # # partidos jugados
#         pg: 0, # # partidos ganados
#         pp: 0, # # partidos perdidos
#         pe: 0, # # partidos empatados
#         gf: 0, # # Goles a favor
#         gc: 0, # # Goles en contra
#         tp: 0, # Total puntos
def main():
    # CREACION DE EQUIPOS
    # LECTURA DE EQUIPOS (TABLA DE POSICIONES)
    # ACTUALIZACIÓN DE EQUIPOS
    # ELIMINACINACIÓN DE EQUIPOS (SALIDA DEL PROGRAMA)

    tablaEquipos = []


    print("""
    MENÚ
    1 - Registrar una fecha
    2 - Consultar tabla de posiciones
    3 - Salida del programa""")

    opcion = int(input('Opción: '))
    
    if opcion == 1:
        # TODO: Por cada fecha, ingresar los partidos jugados
        # * 1. ciclo para las diferentes fechas
        hayFecha = True
        fecha = 1
        while hayFecha:
            print(f'Fecha #{fecha}')
            # * 2. Ciclo para el registro de los diferentes partidos

            hayPartidos = True 
            partido = 1
            while hayPartidos:
                print(f"""
                {'-'*7}
                PARIDO {partido}
                {'-'*7}""")

                # ! RESGISTRO DE PARTIDOS
                # ? Optención de datos de un partido
                equipos_en_partido = []
                TIPOS_DE_EQUIPO = ['local', 'visitante']
                for i in range(len(TIPOS_DE_EQUIPO)):
                    equipo = input(f'Equipo {TIPOS_DE_EQUIPO[i]}: ').lower()
                    goles = int(input('Goles: '))
                    equipos_en_partido.append([equipo, goles])
                
                # TODO: Validar si alguno de los equipos ingresados ya existe en la tabla de posiciones
                    
                # ? Ingreso de los datos del partido a la tabla de equipos
                # Optención de la lista de equipos actuales en la tabla de equipos
                equiposActuales = []
                for equipo in range(tablaEquipos):
                    equiposActuales.append(tablaEquipos[equipo][0])

                
                # * 1. Agregar equipo a tabla en caso de no existir
                # verificación de la existencia de un equipo en la tabla de equipos
                for equipo in range(equiposActuales):
                    for i in range(len(equipos_en_partido)):
                        if  equipos_en_partido[i] in equiposActuales[equipo]:
                            # actualice valores
                            pass
                        else:
                            # agregue el equipo a la tabla con sus valores faltantes
                    # actualizar tabla
                    # lista de equipos actuales
                    for j
                    equiposActuales.append(tablaEquipos[equipo][0])
                    
                    if tablaEquipos[equipo][0]:
                        pass
                    else:
                        # agregar a la tabla
                        pass
                # * 2. Actualizar valores del equipo en caso de existir

                # continuacion del ciclo para el ingreso de partidos
                otroPartido = input('Agregar otro partido? [Y/N]: ')
                if otroPartido.lower() == 'y':
                    otroPartido = True
                else:
                    otroPartido = False    
            
            # continuación del ciclo para el ingreso de fechas
            otra_fecha = input('Agregar otra fecha? [Y/N]: ')
            if otra_fecha.lower() == 'y':
                hayFecha = True
            else:
                hayFecha = False

    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    else:
        pass

#     # [equipo, pj, pg, pp, pe, gf, gc, tp]

if __name__ == '__main__':
    main()



#     # Salida información
#     """
#     Equipo ganador xxx
#     Equipo perdedor xxx
#     """

#     # Para los reportes
#     # A
