import random


tamanho_lista = 10

lista_numeros_aleatorios = [random.randint(-100, 100) for _ in range(tamanho_lista)]


def neg_or_positive(lista):
    """Separa valores negativos e positivos da lista para duas listas
    """
    negativos = []
    positivos = []

    for i in lista:
        if i > 0:
            positivos.append(i)
        else:
            negativos.append(i)



    print(positivos)
    print(negativos)


neg_or_positive(lista_numeros_aleatorios)