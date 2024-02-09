import pandas as pd

def carrinho(lista):
    while True:
        try:
            item = input("Digite um novo item ou pressione Enter para sair:\n ")
            if not item:
                print("Fechando carrinho.")
                break
            description = input(f"Digite a descrição do {item}:\n ")
            value = float(input(f"Digite o valor do {item}:\n "))
            new_item = {"item": item, 'description': description, 'valor': value}
            lista.append(new_item)
        except ValueError:
            print("Digite um valor válido para o preço.")
    return lista

carrinho_compras = []
carrinho_compras = carrinho(carrinho_compras)

df = pd.DataFrame(carrinho_compras)
statistic = df['valor'].agg(['max', 'min', 'sum'])

print(f"O produto de maior valor é R$ {statistic['max']}\n"
      f"E o de menor valor é R$ {statistic['min']}\n"
      f"E o total é R$ {statistic['sum']}")

print("Lista total:")
print(df)
