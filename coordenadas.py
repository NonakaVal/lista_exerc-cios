


def movimento(mensagem):
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

# Exemplo de uso
movimento("Escolha a direção ('cima', 'baixo', 'direita' ou 'esquerda'): ")


