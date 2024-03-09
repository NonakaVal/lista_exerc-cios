
def obter_texto(mensagem):
    """Solicita o input de uma string
    returns: recebe a str fornecida
    """
    return input(mensagem)

def freq_counter(txt):
    """Conta a frequência de cada letra num texto.
    """
    n = {}
    for i in txt:
        if i.isalpha():
            i = i.lower()
            n[i] = n.get(i,0) + 1

    return n

txt_1 = obter_texto("digite ou copie o texto que deseja contar a frequência de caracteres\n")

c = freq_counter(txt_1)

sorted_f = sorted(c.items(), key=lambda x: x[1], reverse=True)

for i in range(min(3, len(sorted_f))):
    l, f = sorted_f[i]
    print(f"A letra '{l}' aparece {f} vezes.")