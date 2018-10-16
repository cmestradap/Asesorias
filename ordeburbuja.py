#Ordenamiento por burbuja

def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp









def burbujaotraforma(unaLista):
    tamañolista = len(unaLista)
    for i in range(1,tamañolista):
        for k in range(0,tamañolista-i):
            if unaLista[k] > unaLista[k+1]:
                auxiliar = unaLista[k]  #Debo guardar el valor de unaLista[k] en una variable auxiliar, para no perder este valor
                unaLista[k] = unaLista[k+1]
                unaLista[k+1] = auxiliar



####----------------------------------------------------INICIO----------------------------------------------------------------######

unaLista = [5,3,2,1]   # Esta lista consta de 9 elementos

#burbujaotraforma(unaLista)             # Llama a la función para ordenar la lista
#print(unaLista)                           # Imprime la lista ordenada

def burbuja2(unaLista):
    tamañolista = len(unaLista)

    for i in range(1,tamañolista):                #   Verificación y ordenamiento.
        for k in range(0,tamañolista-1):          #   (4 ciclos)   Acceder a los indices y reemplazar
            if unaLista[k] > unaLista[k+1]:       #   unaLista[0] > unaLista[1]
                auxiliar = unaLista[k]            #   unaLista[0]   ----->     Guarda el 5
                unaLista[k] = unaLista[k+1]       #   unaLista[0] = unaLista[1]   -->    3 toma el valor de 5
                unaLista[k+1] = auxiliar          #   unaLista[1] = auxiliar = 5


burbuja2(unaLista)
print(unaLista)
print("Lo que debería mostrar: [1,2,3,5]")
 