total = 0
descuento = 0

for i in range(10):
    consumo = int(input(f'Consumo: {i}: '))
    total += consumo
if total > 50:
    descuento = total + consumo

print(f"""
Consumo total: ${total}
Descuento: ${descuento}
Pago total: ${total - descuento}
""")