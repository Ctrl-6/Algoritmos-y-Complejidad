from math import *
import sympy as sp

def reglaDeSimpson(n, a, b, fun):
    h = (b - a)/n
    suma = float(0)
    for i in range(1, n): #Se suman las areas
        x = a + i * h
        if(i % 2 == 0):
            suma += 2 * fx(x, fun)
        else:
            suma +=  4 * fx(x, fun)
    suma += fx(a, f) + fx(b, f) # se suman el primer y la ultima area
    suma = (h / 3) * suma # se divide por 3 la suma del area
    final = suma + errorSimpson(n,a,b,f)[0] # Se suma la funcion con el error
    print("El error es: ", errorSimpson(n,a,b,f)[0])
    print("La expresion del error es: ", errorSimpson(n,a,b,f)[1])
    print("Resultado de la suma:", suma)
    print ("El n apropiado es: ", errorSimpson(n,a,b,f)[2])
    return ("Resultado: ", final)

def fx(x, f):
    return eval(f)


def errorSimpson(n,a,b,f):
    h = (b - a) / n
    x,n2 = sp.symbols('x n2')
    d4 = sp.diff(f,x,4) #Cuarta derivada
    d5 = sp.diff(f,x,5) #Quinta derivada
    start = sp.sympify(d5).subs(x,a)
    end =  sp.sympify(d5).subs(x,b)
    if start < end : #Funcion creciente o decreciente?
        der4 = float(sp.sympify(d4).subs(x,a)) #Si es creciente se evalua a
    else:
        der4 = float(sp.sympify(d4).subs(x,b)) #Si es decreciente se evalua b
    ex_error = ((b-a)**5)/(180*(n2**4)) *der4 #Expresion del error con n de incognita
    error = float(sp.sympify(ex_error).subs(n2,n)) # evualuamos el n en funcion del errro
    n_error = (sp.solve(sp.Eq(ex_error,0.0005),n2))[1] #Obtenemos el n apropiado
    return (-error, ex_error, int(n_error))



n = 4
a = 2
b = 3
f = '1/log(x)'


print("n,a,b,c =",n, a, b, f)
print(reglaDeSimpson(n, a, b, f))

owo = input("Presione tecla Enter para salir... ")





