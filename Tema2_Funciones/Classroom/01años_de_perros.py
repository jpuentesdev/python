'''
Comúnmente se dice que un año humano equivale a 7 años caninos. 

Sin embargo, esta simple conversión no reconoce que los perros alcanzan la edad adulta en aproximadamente dos años. 

Como resultado, algunas personas creen que es mejor contar cada uno de los dos primeros años humanos como 10,5 años caninos y luego contar cada año humano adicional como 4 años caninos.

Escriba un programa que implemente la conversión de años humanos a años caninos descrita en el párrafo anterior. 

Asegúrese de que su programa funcione correctamente para conversiones de menos de dos años humanos y para conversiones de dos o más años humanos. 

Su programa debería mostrar un mensaje de error apropiado si el usuario ingresa un número negativo.

'''

edad_humana = float(input("¿Qué edad tendría tu perro en relación a x años humanos? Introduce un número: "))
def conversor_perruno(edad_humana):
    num_perros1 = 2 * 10.5
    num_perros2 = num_perros1 + (edad_humana-2)*4
    if edad_humana <= 2 and edad_humana >0:
        return(edad_humana *10.5)
    else:
        return(num_perros2)

print(f"El perro tendría {conversor_perruno(edad_humana)} años ")


