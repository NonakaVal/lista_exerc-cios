
def movimento(mensagem):
    """Movimenta a posição no plano cartesiano, começando no valor 0,0
    x, y: define a posição
    directions: define com base no texto informado quais números serão alterados
    choice: permite que o usuário escolha a direção em um loop que verifica se a entrada é válida
    """
    x, y = 0, 0
    directions = {'cima': (0, 1), 'baixo': (0, -1), 'direita': (1, 0), 'esquerda': (-1, 0)}

    while True:
        choice = input(mensagem)
        if choice in directions:
            dx, dy = directions[choice]
            x += dx
            y += dy
            print(f"Posição atual: ({x}, {y})")
        else:
            print("Escolha inválida. Use 'cima', 'baixo', 'direita' ou 'esquerda'.")


movimento("Escolha a direção ('cima', 'baixo', 'direita' ou 'esquerda'): ")


