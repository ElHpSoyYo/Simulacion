import random, math

def lanzamiento():    
    listaLanzamiento=[]
    listaResultado=[]
    vali = True
    contador= 0
    contadorG=0
    while(vali):
        dadoA = random.randint(1,6)
        dadoB= random.randint(1,6)
        suma= dadoA+dadoB
        listaLanzamiento.append(suma)       
        if ((suma == 7 or suma == 11) and contador == 0):
            contadorG += 1
            vali = False            
        if ((suma == 2 or suma == 3 or suma == 12) and contador == 0):
            vali = False            
        if((suma in [4,5,6,8,9,10] and listaLanzamiento[0]== suma) and contador!= 0):
            contadorG += 1             
            vali = False             
        if (suma == 7 and contador !=0):                        
            vali = False     
        contador += 1        
    return([contadorG, contador])

def probabilidad(listaPro):
    ganar= 0
    perder=0
    for i in listaPro:
        a = i[0]
        if(a==1):
            ganar += 1
        else:
            perder +=1
    print('Probabilidad ganar: ',ganar/len(listaPro))
    print('Probabilidad perder: ',perder/len(listaPro))
 
def lanzGanar(listaPro):
    lanza = 0
    gano=0
    for i in listaPro:
        g=i[0]
        l=i[1]
        if (g==1):
            gano += 1
            lanza += l
    print('Lanzamientos Promedio Para Ganar: ',math.ceil(lanza/gano))
    
            
numIntentos = int(input("Ingrese el numero de juegos que desea Simular"))
listaPro=[]
for i in range(numIntentos):
    listaPro.append(lanzamiento())
probabilidad(listaPro)
lanzGanar(listaPro)
    
    
    
