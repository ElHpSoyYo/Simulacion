from random import random
from time import sleep
from collections import Counter
from copy import copy
import matplotlib.pyplot as plt

def tiempoEntreLlegadas():
  x = 2 + 3 * random()
  return 5*((x)**2) -12

def obtenerProbabilidad(lista):
  totalElementos = 0
  for i in lista:
    totalElementos += i[0]
  return [round(elemento[0]/totalElementos,2) for elemento in lista ]

def obtenerAcumulada(lista):
  probabilidadades = obtenerProbabilidad(lista)
  acumulada = [0]
  acumulado = 0
  for probabilidad in probabilidadades:
    acumulado += probabilidad 
    acumulado = round(acumulado,2)
    acumulada.append(acumulado)
  return acumulada

def obtenerIntervalo(lista, numero):
  for i in range(1, len(lista)):
    if (lista[i-1] <= numero < lista[i]):
      return i-1

def tiempoDeServicio(acumulada,lista):
  r1 = random()
  r2 = random()
  intervalo = obtenerIntervalo(acumulada, r1)
  limiteInferior, limiteSuperior = lista[intervalo][1]
  return limiteInferior + (limiteSuperior - limiteInferior)*r2

def obtenerTiempoEntreLlegadas(lista):
  resultado = [0]
  for i in lista:
    resultado.append(i + resultado[len(resultado)])

def simularCola(tLlegadas, tServicios):
    tiempoDeAtencion = []
    tiemposSalida = []
    numeroPersonas = [0]
    tSimulacion = [0]

    tSimulacion.append(tLlegadas[0])
    tiempoDeAtencion.append(tSimulacion[-1])
    numeroPersonas.append(1)
    tiemposSalida.append(tLlegadas.pop(0) + tServicios.pop(0))
    while tLlegadas or tServicios:
      if(tLlegadas):
          #Cuando ya atendieron una persona
          if(numeroPersonas[-1] > 0 and tLlegadas[0] > tiemposSalida[-1]):
              numeroPersonas.append(numeroPersonas[-1] - 1)
              if(numeroPersonas[-1] == 0):
                  tSimulacion.append(tiemposSalida[-1])
              else: 
                  tSimulacion.append(tiemposSalida[-1])
                  tiemposSalida.append(tSimulacion[-1] + tServicios.pop(0))
                  tiempoDeAtencion.append(tSimulacion[-1])
          #Cuando llega una persona
          else:
              tSimulacion.append(tLlegadas.pop(0))
              if(numeroPersonas[-1] == 0):
                  tiemposSalida.append(tSimulacion[-1] + tServicios.pop(0))
                  tiempoDeAtencion.append(tSimulacion[-1])
              numeroPersonas.append(numeroPersonas[-1] + 1)

      else:
          numeroPersonas.append(numeroPersonas[-1] - 1)
          if(numeroPersonas[-1] == 0):
              tSimulacion.append(tiemposSalida[-1])

          else: 
              tSimulacion.append(tiemposSalida[-1])
              tiemposSalida.append(tSimulacion[-1] + tServicios.pop(0))
              tiempoDeAtencion.append(tSimulacion[-1])

    return (tSimulacion,  numeroPersonas, tiemposSalida, tiempoDeAtencion)



lista = [(15,[1,3]),(25, [3,5]),(30,[5,7]),(20,[7,9])]
acumulada = obtenerAcumulada(lista)

tiemposDeLlegada = [tiempoEntreLlegadas() for i in range(50)]
tiemposDeServicios = [tiempoDeServicio(acumulada,lista) for i in range(50)]
tiemposDeLlegada.sort()


for i in tiemposDeLlegada:
    print(i)
print()

for i in tiemposDeServicios:
    print(i)
print()

resultados = simularCola(copy(tiemposDeLlegada),copy(tiemposDeServicios))
print(resultados)
print("Se obtuvieron", len(resultados[0]),"salidas en tiempos simulacion")
print("Se obtuvieron", len(resultados[1]),"salidas en personas")
print("Se obtuvieron", len(resultados[2]),"salidas en salidas")

print(resultados[2])
print("Tsim\t#P\tSALE")
salidas = 0
print(resultados[0][0], resultados[1][0], "-", sep="\t")
print(round(resultados[0][1],2), resultados[1][1], round(resultados[2][salidas],2), sep="\t")
imprimir = False


for i in range(2, len(resultados[0])):
    if imprimir:
        salidas +=1
        print(round(resultados[0][i],2), resultados[1][i], round(resultados[2][salidas],2), sep="\t")
        imprimir = False
    elif (resultados[0][i] == resultados[2][salidas]) :
        if (resultados[1][i] == 0):
            print(round(resultados[0][i],2), resultados[1][i], "-", sep="\t")
            imprimir = True
        else:
            salidas +=1
            print(round(resultados[0][i],2), resultados[1][i], round(resultados[2][salidas],2), sep="\t")
    else:
        print(round(resultados[0][i],2), resultados[1][i], "-", sep="\t")


tiempoEnElSistema = [resultados[2][i] - tiemposDeLlegada[i] for i in range(len(resultados[2]))]
media = sum(tiempoEnElSistema)/len(tiempoEnElSistema)
print(media)
desviacionEstandar = 0
for i in tiempoEnElSistema:
      desviacionEstandar = (i - media)**2
desviacionEstandar = desviacionEstandar/(len(tiempoEnElSistema) - 1)
desviacionEstandar = desviacionEstandar**(1/2)
print(desviacionEstandar)

#Para 49 datos con confianza 0,1, t(0,05,49) sera 1.6766
intervaloDeConfianza = ((1.6766)*desviacionEstandar)/((len(tiempoEnElSistema))**(1/2))
limiteSuperior = media + intervaloDeConfianza
limiteInferior = media - intervaloDeConfianza
print("Limites son: ", limiteSuperior, limiteInferior)

print(len(resultados[3]), len(tiemposDeLlegada))
tiempoDeEspera = [resultados[3][i] - tiemposDeLlegada[i] for i in range(len(resultados[3])) ]
print(tiempoDeEspera)
#for i in range(len(resultados[3])):
#  print(round(tiemposDeLlegada[i],2), round(resultados[3][i],2)) 

#Datos aleatorios para el ejemplo
plt.title('Tiempos De Espera')
plt.hist(tiempoDeEspera,alpha=1, edgecolor = 'black',  linewidth=1)
plt.ylabel('Número de Personas')
plt.xlabel('Tiempo de espera[min]')
plt.grid(True)
plt.show()
plt.clf()
#medias = [elementos/len(tiemposDeServicios) for elementos in tiemposDeServicios]
#for i in medias:
#  print(i)
#print(Counter(resultados[2]))
