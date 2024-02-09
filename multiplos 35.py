

def verificador_e_imprime(lista):
    num = []
    for i in lista:
        if i % 7 == 0 and i % 5 == 0:
            num.append(i)

    return num

lista = [i for i in range(501)]
num_list = verificador_e_imprime(lista)

print("Números divisíveis por 7 e múltiplos de 5 na lista:")
print(num_list)

