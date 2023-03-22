
base = 5
altura = 4
veces=4

linea_base = "*\t" * base
linea_media = "*\t" + "\t" * (base-2) + "*"

print(linea_base)
for i in range(altura -2):
    print(linea_media)

print(linea_base)


