'''
Escriba un programa que determine el nombre de una forma a partir de su número de lados.
 
Lea la cantidad de lados del usuario y luego informe el nombre apropiado como parte de un mensaje significativo. 

Su programa debe admitir formas con entre 3 y 10 lados (incluidos). 

Si se ingresa un número de lados fuera de este rango, su programa debería mostrar un mensaje de error apropiado.
'''

figura = int(input("Introduce un número de lados para averiguar de qué figura se trata: "))
def detector_formas(figura):
    figuras = {3:"triángulo",4:"cuadrado",5:"pentágno",6:"hexágono",7:"heptágono",8:"octágono",9:"nonágono",10:"decágono"}
    numeros = [3,4,5,6,7,8,9,10]
    if figura in numeros:
        return (f"Se trata de un {figuras[figura]}")
    else:
        return("El número introducido debe de estar comprendido entre el 3 y el 10 (ambos incluidos)")

print(detector_formas(figura))

