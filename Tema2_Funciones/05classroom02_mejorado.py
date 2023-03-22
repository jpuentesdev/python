figura = int(input("Dame un número de lados: "))
def detector_formas(figura):
    figuras = {3:"tríangulo",4:"Cuadrado",5:"pentágono",6:"hexágono",7:"heptágono",8:"octágono",9:"nanógano",10:"decágono"}
    if figura in figuras:
        return (f"El número de lados {figura} corresponde a la figura: {figuras[figura]}")
    else:
        return("El número introducido debe de estar comprendido entre 3 y 10, y comprendido también por su novia ave o no")

print (detector_formas(figura))







