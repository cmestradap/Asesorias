#REPASO CONCEPTOS BÁSICOS

listaNumeros = [2,4,8]

#METODO MANUAL PARA CALCULAR LA SUMA
def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

#print(sumalista([1,3,5,7,9]))



#DEF-- > ES UNA FUNCIÓN, LE ENTRAN DATOS Y DEBE DEVOLVER (return) ALGO

#METODO FÁCIL PARA CALCULAR LA SUMA
def sumafacil(listaNumeros):
    return sum(listaNumeros)



#PROMEDIO DE UNA LISTA 

def promedio(listaNumeros):
    #Necesito el número de elementos ¿Cómo lo hago?
    #Python ofrece una función que lo hace automáticamente len()

    n = len(listaNumeros)  #Número de elementos de la lista
    suma = sum(listaNumeros)

    promedio = suma/n

    return promedio


def funcionamientowhile():
    b=2

    while b > 0:
        print("hola", b)

        b = b-1



print(funcionamientowhile())


