
#         equipo: 'xxx',
#         pj: 0, # # partidos jugados
#         pg: 0, # # partidos ganados
#         pp: 0, # # partidos perdidos
#         pe: 0, # # partidos empatados
#         gf: 0, # # Goles a favor
#         gc: 0, # # Goles en contra
#         tp: 0, # Total puntos


# def registroPartidos():
#     partidosJugados = []

#     print('REGISTRO DE PARTIDOS')
#     partidoNumero = 1

#     condicion = True
#     while condicion:
#         # variables locales
#         ganador = False

#         print(f"""
#         {'-'*10}
#         PARIDO {partidoNumero}
#         {'-'*10}""")

#         # registro de partidos
#         local = input('Equipo local: ').capitalize()
#         gol_local = int(input('Goles: '))
#         visitante = input('Equipo visitante: ').capitalize()
#         gol_visitante = int(input('Goles: '))

#         # Determinar quien es ganador
#         if gol_local > gol_visitante:
#             ganador = True
#             partidosJugados.append([local, gol_local, ganador])
#         else:
#             partidosJugados.append([visitante, gol_visitante, ganador])

#         opcion = int(input('Nota: Oprima 1 para agregar otro registo, de lo contrario cualquier tecla: '))
#         if opcion != 1:
#             condicion = False
#         partidoNumero += 1

#     return partidosJugados

def main():
    tablaPosiciones = []


    print("""
        Menú
    1 - Registrar una fecha
    2 - Consultar tabla de posiciones""")

    opcion = int(input('Opción: '))
    if opcion == 1:
        partidosJugados = []

    # REGISTRO DE PARTIDOS
    print('REGISTRO DE PARTIDOS')
    partidoNumero = 1

    condicion = True
    while condicion:
        ganador = False

        print(f"""
        {'-'*10}
        PARIDO {partidoNumero}
        {'-'*10}""")

        # registro de partidos
        local = input('Equipo local: ').capitalize()
        gol_local = int(input('Goles: '))
        visitante = input('Equipo visitante: ').capitalize()
        gol_visitante = int(input('Goles: '))

        # Determinar quien es ganador
        if gol_local > gol_visitante:
            ganador = True
            partidosJugados.append([local, gol_local, ganador])
        partidosJugados.append([visitante, gol_visitante, ganador])

        opcion = int(input('Nota: Oprima 1 para agregar otro registo, de lo contrario cualquier tecla: '))
        if opcion != 1:
            condicion = False
        partidoNumero += 1

        tablaPosiciones.append(partidosJugados)
        # for i in range(len(partidoFecha)):
        #     if i[0] in 
        # extracción del nombre de los equipos
        # for equipo in range(len(tablaPosiciones)):
        #     equiposParticipantes.append(equipo[0])
        print(tablaPosiciones)
    else:
        pass

#     # [equipo, pj, pg, pp, pe, gf, gc, tp]

if __name__ == '__main__':
    main()

#     'Estructura de las listas'


#     # Pedir información
#     """"
#         REGISTRO DE PARTIDOS
#         -----------------------
#         PERTIDO 1
#         -----------------------
#         Equipo local : xxxx
#         Goles: xxxx
#         Equipo Visistante: xxxx
#         Goles: xxxx
#     """

#     # Salida información
#     """
#     Equipo ganador xxx
#     Equipo perdedor xxx
#     """

#     # Para los reportes
#     # A
