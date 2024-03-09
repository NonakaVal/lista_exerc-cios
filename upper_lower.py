def obter_texto(mensagem):
    """Solicita o input de uma string
    returns: recebe a str fornecida
    """
    return input(mensagem)


def contar_maiusculas_minusculas(texto):
    """Conta a quantidade de letras maiúsculas e minúsculas na string recebida
    """
    u = 0
    l = 0
    for char in texto:
        if char.isupper():
            u += 1
        elif char.islower():
            l += 1
    return u, l


texto_input = obter_texto("Digite um texto:\n")
maiusculas, minusculas = contar_maiusculas_minusculas(texto_input)

print(f"O texto '{texto_input}' possui {maiusculas} letras maiúsculas e {minusculas} letras minúsculas.")
