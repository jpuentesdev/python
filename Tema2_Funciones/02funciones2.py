# Los diferentes módulos de una aplicación tienen: Alta cohesión y bajo acoplamiento (funcionamineto de manera individual)
#La variable que se crea dentro de una función no se conoce fuera de ella: VARIABLE LOCAL, a menos que tú la saques fuera
def saluda(personas):
    for p in personas:
        print(f"Hola {p}")

gente = ["Manolo", "Migue", "Roberto"]
saluda(gente)

############################ SACANDO LA VARIABLE FUERA DE LA FUNCI

def saluda(personas):
    salida = []
    for p in personas:
        salida.append(f"Hola {p}")
    return salida

gente = ["Manolo", "Migue", "Roberto"]
saludos =saluda(gente)

print(saludos)

#######################


def suma(num1,num2):
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    else:
        return int(num1) + int(num2)

result = suma(4,"5")
print(result)

