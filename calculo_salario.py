
def calcular_horas(mensagem, multiplicador):
    """Calcula o total de horas trabalhadas.
    Tenta converter a entrada do usuário para um número inteiro.
    """
    while True:
        try:
            x = int(input(mensagem))
            total = x * multiplicador
            return total
        except ValueError:
            print("Digite um valor válido (número inteiro).")

def qualificador(valor1,valor2):
    """verifica se a pessoa se qualifica para receber horas extras
    j,y: valores por hora
    if: verifica os requisitos
    returns: recebe o total
    """
    y = valor1 * 29.11
    j = valor2 * 5
    if valor1 > 40:
        total = y + j
        answer = f"total de horas trabalhadas foi {valor1}, você pode receber pelas horas extras"
    else:
        total = y
        answer = f"total de horas trabalhadas foi {valor1}, não sera possível receber pelas horas extras"
    return total, answer


horas = calcular_horas("digite a quantidade de dias trabalhados\n", 8)
horas_extras = calcular_horas("digite total de horas extras acumuladas\n", 1)

total1, resposta = qualificador(horas, horas_extras)

print(f"{resposta}\n total a receber é R$ {total1}")