num = int(input('Número: '))

pro = 1

for i in range(num):
    print((i+1),  end=' ')
    pro = pro * (i+1)

print(pro)
