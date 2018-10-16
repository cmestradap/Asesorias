#BUSQUEDA SECUENCIAL

def busqueda_lineal(lista, elementobuscado):
    """ Búsqueda lineal.
    Si x está en lista devuelve su posición en lista, de lo
    contrario devuelve -1.
    """
 
    # Estrategia: se recorren uno a uno los elementos de la lista
    # y se los compara con el valor x buscado.
    i=0 # i tiene la posición actual en la lista, comienza en 0
 
    # el ciclo for recorre todos los elementos de lista:
    for valoractualdelarreglo in lista:
        # estamos en la posicion i, z contiene el valor de lista[i]
 
        # si z es igual a x, devuelve i
        if valoractualdelarreglo == elementobuscado:
            return i
 
        # si z es distinto de x, incrementa i, y continúa el ciclo
        i=i+1
 
    # si salió del ciclo sin haber encontrado el valor, devuelve -1 
    return -1
#          0 1 2
milista = [4,5,9,45,12,10]

print(busqueda_lineal(milista,2))
#Me debería devolver el 1, que es el índice.