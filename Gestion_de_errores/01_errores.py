'''
En una aplicación nunca puede haber un error que la invalide: para ésto sirve la gestión de errores
TIPOS:
try:
except:
else:
finally:
'''
#
try:
    1/0                                              #si falla se ejecuta la línea de abajo
except Exception as e:
    print("¡¡¡QUÉ FALLO!!!")


def division(numerador,divisor):
    result = None
    try:
        result= numerador / divisor
    except ZeroDivisionError:
        print("0 DIVISION ERROR\nPrueba con otro divisor")
    return result
    
print(division(1,0)) 



# función que divida y que funcione siempre


def division(numerador,divisor):
    result = None
    try:
        result= numerador / divisor
    except (ZeroDivisionError,TypeError):
        print("0 DIVISION ERROR\nPrueba con otro divisor")
    return result
    
print(division(1,0)) 


def pide_numero():
    num = input("Dame un numero: ")
    for i in (int, float):
        try:
            return num
        except ValueError:
            pass
    

print(pide_numero())

