Billetes = [365,91,52,28,13,7,4,1]

#Funcion principal donde se realiza el calculo
def changePrincipal(billetes, n):
    minMon = 1000 #Nuestra cota que se va a ir reemplazando por los minimos
    totalMon = 0 #Total ded monedas necesarias
    arr = []

    if n == 0: #Si no se requiere cambio
        return 0, arr 

    if n in billetes: #Si el cambio basta con una moneda
        return 1, [n]

    for i in billetes: #Iterando las ramas y combinaciones posibles
        if i > n:   #Si la moneda exede el cambio se pasa a la siguiente iteracion
                pass
        else:  #La moneda no excede el cambio 
                totalMon = 1 + changePrincipal(billetes, n - i)[0] #Tomamos el primer billete, y vamos observando las combinacione junto a los otros. 
                if totalMon < minMon: #Comprobamos que el total de monedas sea menor al que habia antes.
                    minMon = totalMon #Reemplazamos si es menor
                    arr = changePrincipal(billetes, n - i)[1]+ [i] #Agregamos al arreglo la moneda utilizada
                else:
                    break #Esta parte de la funcion elimina ramas que no son eficientes
            
    return minMon, arr


#Funcion para retornar arreglo pedido
def change(billetes, n):
    minMon, arrMon = changePrincipal(billetes, n)
    arr2 = list()
    for i in range(len(billetes)):
        arr2.append(0)
    for i in set(arrMon):
        arr2[billetes.index(i)] = arrMon.count(i)

    return minMon, arr2
    

print("------------Money-------------")
print(Billetes)
print("------------------------------")
x = int(input("Cambio: "))
print(change(Billetes,x)[1])

