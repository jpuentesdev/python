'''
1. % de ventas de cada vendedor 
2. % sobre las ventas de cada cliente
3. 5 productos más vendidos
4. Ingresos mensuales generales
'''
import csv
import pprint
import os
ruta_base = "C:\\Users\\Tarde\\Downloads\\Python\\Tema2_Funciones\\Archivos\\"
archivo= ruta_base + "cust_orders_prods.csv" 

#PLAN DE ACCIÓN
'''
Descomponer la aplicación en bloques
Detallar cada bloque
Diseñar la interfaz de la aplicación y de cómo se muestran los resultados
Descomponer en tareas
Asignar tareas
Hacer las tareas
Integrar las soluciones de cada miembro
PROBAR QUE todo FUNCIONA
'''
'''
def leer_archivo(archivo):
    f = open(archivo,"r")
    lector_dict = csv.DictReader(f)
    lista_dict = list(lector_dict)
    f.close()
    pprint.pprint(lista_dict)
    

leer_archivo(archivo)
'''
dict={1:{
"customer_name":"Ming-Yang Xie","employee_name":"Nancy Freehafer","order_date":"2006-03-24","quantity":3000000,"unit_price":460000,"product_name":"Coffee"},	
2:{"customer_name":"Roland Wacker","employee_name":"Nancy Freehafer","order_date":"2006-03-24","quantity":36800,"unit_price":250000,"product_name":"Boysenberry Spread"},
3:{"customer_name":"Roland Wacker","employee_name":"Nancy Freehafer","order_date":"2006-07-24","quantity":40000,"unit_price":250000,"product_name":"Boysenberry Spread"},
4:{"customer_name":"Marie Cury","employee_name":"Nancy Freehafer","order_date":"2006-03-24","quantity":40000,"unit_price":250000,"product_name":"Boysenberry Spread"},
5:{"customer_name":"Marie Cury","employee_name":"Nancy Freehafer","order_date":"2006-05-24","quantity":42000,"unit_price":250000,"product_name":"Boysenberry Spread"}		
}

#print(dict[1]["quantity"] + dict[2]["quantity"])
'''
dict2 = {}
for n in dict:
    dict2[dict[n]["customer_name"]] = dict[n]["quantity"] 
print(dict2)
'''   


mes_marzo = 0
for n in dict:
    if dict[n]["order_date"][5:7] == "03":
        mes_marzo += dict[n]["quantity"] * dict[n]["unit_price"]
print(f"La facturación total del mes de Marzo es de {mes_marzo}€")   


dict_meses = {"01": 0,"02": 0,"03": 0,"04": 0,"05": 0,"06": 0,"07": 0,"08": 0,"09": 0,"10": 0,"11": 0,"12": 0}
for n in dict:
    for mes in dict_meses:
        if dict[n]["order_date"][5:7] in mes:
            dict_meses[mes] += dict[n]["quantity"] * dict[n]["unit_price"]
print(dict_meses)
'''
lista = []

for n in dict:
    if "Roland Wacker" in dict[n]["customer_name"]:
        lista.append(dict[n]["quantity"])
    
print(lista)


total_Roland = 0
for l in lista:
    total_Roland += l
print(total_Roland)

total_ventas = 3000000  #CANTIDAD DE PRUEBA: habría que calcular primero el total de ventas, cuando tengamos las cantidades de todos los empleados
porcentaje_Roland = 100 * total_Roland/total_ventas
print(f"El porcentaje de la cantidad vendida por Roland Wacker sobre el total es del {porcentaje_Roland}%")
'''