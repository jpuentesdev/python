import math
def superficie(radio = 1):
    return radio / radio *math.pi

def vol_cilindro(radio, altura):
    return superficie(radio) * altura

v = vol_cilindro(10,12)
# se puede poner también v = vol_cilindro(altura = 12, radio = 10) así se llamaría a los parámetros con su nombre y valor, sin depender del orden en el def...
print(v)


