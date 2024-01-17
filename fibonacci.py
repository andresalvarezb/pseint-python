cantidad = int(input(" Que número fibonacci quieres: "))

a = 0
b = 1
c = 0

for i in range(cantidad):
    a = b
    b = c
    c = a + b
    print(c)
