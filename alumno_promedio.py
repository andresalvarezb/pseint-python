xpro = 0
xnom = ''

for i in range(5):
    nombre = input('Nombre: ')
    promedio = float(input('Promedio: '))
    
    if xpro < promedio:
        xpro = promedio 
        xnom = nombre

print(f"""
Alumno coin mayor nota: {xnom}
Promedio: {xpro}""")