

def lista_nomes(mensagem):
    """cria uma lista de nomes
    lista: variável que recebe os nomes
    while: loop que permite continuar adicionando nome na lista ou parar o loop
    returns: retorna uma lista de nomes
    """
    lista = []
    while True:
        nome = input(mensagem)
        if nome == "":
            break
        else:
            lista.append(nome)
    return lista
def ordenador(lista):
    """ordena a lista
    sort: método ordenador
    returns: retorna para lista
    """
    lista.sort()
    return lista

nomes = lista_nomes("Digite um nome ou aperte Enter para encerrar\n")
teste = ordenador(nomes)

print(teste)