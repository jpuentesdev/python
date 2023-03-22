#saliendo todos los números hasta el último 
def fib(n):
    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)


#sale sólo el número en cuestión
def fib2(n):
    num1 = 0
    num2 = 1
    while resultado < n:
        resultado = num1+num2
    return resultado

fib2(200)
        
        