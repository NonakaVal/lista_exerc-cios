import calendar

def contar_meses_sexta_feira(inicio, fim):
    total_meses_sexta = 0

    for ano in range(inicio, fim + 1):
        for mes in range(1, 13):
            primeiro_dia_do_mes = calendar.weekday(ano, mes, 1)
            if primeiro_dia_do_mes == calendar.FRIDAY:
                total_meses_sexta += 1

    return total_meses_sexta

# Defina o intervalo de anos desejado
ano_inicio = 1990
ano_fim = 2024

resultado = contar_meses_sexta_feira(ano_inicio, ano_fim)
print(f"O número de meses que começam em sexta-feira no intervalo de {ano_inicio} a {ano_fim} é: {resultado}")
