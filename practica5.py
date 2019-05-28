from random import random
import matplotlib.pyplot as plt

mos = [random()*1000 for _ in range(30000)]

#plt.title('Practica 4')
#plt.hist(mos, bins=60, alpha=1, edgecolor = 'black',  linewidth=1)
#plt.grid(True)
#plt.show()
#plt.clf()

def tiempoEntreLlegada():
    x= 2 + 3*random()
    return ((5*(x)**2 -12)/113)

def asignarAcumulada():
    r= random()
    if(r <= 15/90):
        return 1 +2*random()
    elif(r <=40/90):
        return 3 +2*random()
    elif(r <= 70/90):
        return 5+ 2*random()
    elif(r <= 90/90):
        return 7+ 2*random()

def tiempoDeServicio():
    pass

listaF=[]
for i in range(50):
    listaF.append([tiempoEntreLlegada(), asignarAcumulada()])
print(listaF)
