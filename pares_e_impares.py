pares = 0
impares = 0

num_lim = int(input("Cuantos números: "))

for i in range(num_lim):
    num = int(input('Escriba un número: '))

    if num % 2 == 0:
        print(f'{num} es par')
        pares += 1
    else: 
        print(f'{num} es impar')
        impares += 1

print(f'Hubo {pares} pares y {impares} impares')