
class Carro:
    def __init__(self, marca, modelo, ano, cor, valor):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
        self.__cor = cor
        self.__valor = valor

    def __str__(self):
        return f"Carro(marca={self.__marca}, modelo={self.__modelo}, ano={self.__ano}, cor={self.__cor}, valor={self.__valor})"

carro1 = Carro("vw", "gol", 1997, "preto", 10000)
print(carro1)
