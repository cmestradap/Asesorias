#ALGORITMOS DE ORDENAMIENTO



#ORDENAMIENTO POR SELECCIÓN

lista = [8,4,5]

def ord_seleccion(lista):
    # n = posicion final del segmento a tratar
    n = len(lista)-1
    print(n)

    while n > 0 :
        mayorindice = buscar_max(lista,0,n)   # = 6
        
        
        lista[mayorindice],lista[n]= lista[n],lista[mayorindice]
        

        
        print ("PASOS: ", mayorindice, n, lista)
        
        # reduce el segmento en 1
        n = n - 1
 
#BUSQUEDA DEL MAYOR ELEMENTO EN UN ARREGLO
def buscar_max(lista,inicio,fin):

    pos_max = inicio

    for i in range(inicio+1, fin+1):
        if lista[i] > lista [pos_max]:
            pos_max = i
    return pos_max

#print(ord_seleccion(lista))


def buscar_mayor(lista, inicio):

        pos_max = inicio
        fin = len(lista)

        for i in range(inicio+1, fin): 
                if lista[i] > lista[pos_max]:
                        pos_max = i
        return pos_max

print (buscar_mayor(lista,0))

