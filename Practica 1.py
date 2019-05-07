import random,math

def simulacion():
    cara=0
    sello=0
    utilidad= 0
    while(abs(cara-sello)!= 3):
        a= float(random.random())
        if(a < 0.5):
            cara +=1
        elif(a >= 0.5):
            sello +=1
        utilidad -=1
    utilidad +=8
    return [cara+sello,utilidad]

def probGanar(lista):
    probaG=0
    for i in range(len(lista)):
        if(lista[i]>=0):
            probaG += 1
    return probaG/len(lista)

def probPerder(lista):
    probaP=0
    for i in range(len(lista)):
        if(lista[i]<0):
            probaP += 1
    return probaP/len(lista)
    
    
    

numJuegos= int(input("Cuantos Juegos desea realizar"))
numeroLanz=[]
lUtilidad=[]
for i in range(numJuegos):
    valores= simulacion()
    numeroLanz.append(valores[0])
    lUtilidad.append(valores[1])
    #print("numero de lanzamientos ",valores[0])
    #print("La utilidad obtenida fue: ",valores[1])

numeroLanz.sort()
lUtilidad.sort()

utilidadProm= sum(lUtilidad)/len(lUtilidad)
print("Utilidad Promedio es :", utilidadProm)
numLanz= float(sum(numeroLanz)/numJuegos)
print("Media de lanzamientos: ",numLanz)
print("Probabilidad de obtener una ganancia >=0:", probGanar(lUtilidad))
print("Probabilidad de obtener una ganancia < 0:", probPerder(lUtilidad))
