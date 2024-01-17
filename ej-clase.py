
"def main():
    print('INFORMACIÓN DE LOS PARTIDOS')
    for i in range(2):
        # informacion para cada equipo
        equipo = input('Equipo: ')
        goles = int(input('Goles: '))
        equipo_{i} = 'nombre'

    equipo_1 = {
        equipo: 'xxx',
        pj: 0, # # partidos jugados
        pg: 0, # # partidos ganados
        pp: 0, # # partidos perdidos
        pe: 0, # # partidos empatados
        gf: 0, # # Goles a favor
        gc: 0, # # Goles en contra
        tp: 0, # Total puntos
    }


def registroPartidos():
    partidos = []

    print('REGISTRO DE PARTIDOS')
    partido = 1
    while True:
        print(f"""
        {'-'*10}
        PARIDO {partido += 1}
        {'-'*10}""")
        local = input('Equipo local: ').capitalize()
        gol_local = int(input('Goles: '))
        visitante = input('Equipo visitante: ').capitalize()
        gol_visitante = int(input('Goles: '))
        
        # Determinar quien es ganador
        if gol_local > gol_visitante:
            ganador = True
            
        partidos.append([local, gol_local])
        partidos.append([visitante, gol_visitante])
        opcion = int(input('Nota: Oprima 1 para agregar otro registo, de lo contrario cualquier tecla: '))
        if opcion != 1:
            return False
    
    
def tablaPosiciones():
    pass

def main():
    print("""Menú
    1 - Registrar una fecha
    2 - Consultar tabla de posiciones""")
    
    opcion = int(input('Opción: '))
    if opcion == 1:
        registroPartidos()
    else:
        tablaPosiciones()


if __name__ == '__main__':
    main()

    'Estructura de las listas'
    # [equipo, pj, pg, pp, pe, gf, gc, tp]

    # Pedir información
    """"
        REGISTRO DE PARTIDOS
        -----------------------
        PERTIDO 1
        -----------------------
        Equipo local : xxxx
        Goles: xxxx
        Equipo Visistante: xxxx
        Goles: xxxx
    """

    # Salida información
    """
    Equipo ganador xxx
    Equipo perdedor xxx
    """

    # Para los reportes
    # Adef infoEquipo(nombre, goles):



def main():
    print('INFORMACIÓN DE LOS PARTIDOS')
    for i in range(2):
        # informacion para cada equipo
        equipo = input('Equipo: ')
        goles = int(input('Goles: '))
        equipo_{i} = 'nombre'

    equipo_1 = {
        equipo: 'xxx',
        pj: 0, # # partidos jugados
        pg: 0, # # partidos ganados
        pp: 0, # # partidos perdidos
        pe: 0, # # partidos empatados
        gf: 0, # # Goles a favor
        gc: 0, # # Goles en contra
        tp: 0, # Total puntos
    }

    





if __name__ == '__main__':
    main()


    # Pedir información
    """"
        REGISTRO DE PARTIDOS
        -----------------------
        PERTIDO 1
        -----------------------
        Equipo local : xxxx
        Goles: xxxx
        Equipo Visistante: xxxx
        Goles: xxxx
    """

    # Salida información
    """
    Equipo ganador xxx
    Equipo perdedor xxx
    """

    # Para los reportes
    # A
