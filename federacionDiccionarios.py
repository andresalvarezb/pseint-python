import random
federacion = {}


num_equipo = 1
hayPartido = True
while hayPartido:
    nombre = input('Nombre del equipo: ')
    equipo = {
        'nombre' : nombre,
        'pj': 0,
        'pp': 0,
        'pe': 0,
        'pg': 0,
        'gf': 0,
        'gc': 0,
    }
    federacion.update({str(num_equipo): equipo})
    num_equipo += 1

    hayEquipo = input('Agregar otro equipo [Y/N]: ')
    if hayEquipo.lower() == 'y':
        hayPartido = True
    else:
        hayPartido = False

# organizar equipos
grupos = {
    '1': [],
    '2': []
}

# para el grupo
grupo = 1
numsAleatorios = []
for i in range(len(grupos)):
    buscar = True
    while buscar:
        numAleatorio = random.randint(1, len(federacion))
        if numAleatorio not in numsAleatorios:
            if len(grupos[str(grupo)]) < 4:
                numsAleatorios.append(numAleatorio)
                grupos[str(grupo)].append(federacion[str(numAleatorio)])
                buscar = True
            else:
                buscar = False
        if len(numsAleatorios) > 8:
            buscar = False
    grupo += 1


print(grupos)