from fractions import Fraction
from math import ceil



def egipciosVoraces(frac):
   arr = [] #Contiene los denominadores
   if frac.numerator == 1: #Comprobamos si el denominador es 1
       arr.append(str(frac.denominator))
       return arr
   else:
        rev_frac = Fraction(frac.denominator,frac.numerator) #invertimos la fraccion
        result= ceil(rev_frac) 
        fin_frac = Fraction(1,result) #Fraccion resultante
        new_frac = frac - fin_frac #nueva fraccion por descomponer
        arr.append(str(fin_frac.denominator)) #se agrega la fraccion final al arreglo
        return arr + egipciosVoraces(new_frac) #repetimos el proceso para la fraccion nueva.
        
#Manejamos input y output
w = int(input())
for i in range(w):
    x = (input()).split(" ")
    n = int(x[0])
    d = int(x[1])
    frac = Fraction(n, d)
    print((str(n) +"/"+ str(d) + ": " + ",".join(egipciosVoraces(frac))))
    
    

 
