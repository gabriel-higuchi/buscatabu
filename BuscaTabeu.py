def EstrategiaGulosa(itens, beneficio, peso, capacidade):
    custobenefico = []
    for i in range(len(itens)):
        aux = beneficio[i] / peso[i]
        custobenefico.append(round(aux, 2))

    # Criando uma lista de itens com todos os atributos e ordenando pela razão benefício/peso
    itens_completos = list(zip(itens, beneficio, peso, custobenefico))
    itens_completos.sort(key=lambda x: x[3], reverse=True)

    # Inicializando o vetor de escolhidos com 0
    escolhidos = [0] * len(itens)
    capacidade_atual = capacidade

    for item in itens_completos:
        index = item[0] - 1  # Ajustando o índice para a posição correta
        if capacidade_atual >= item[2]:  # Se ainda cabe na mochila
            escolhidos[index] = 1  # Marca o item como escolhido
            capacidade_atual -= item[2]  # Atualiza a capacidade disponível

    # Criando a matriz a ser retornada
    matrizGulosa = [
        ["Item"] + itens,
        ["Benefício"] + beneficio,
        ["Peso"] + peso,
        ["Custo-Benefício"] + custobenefico,
        ["Escolhido"] + escolhidos
    ]
    return matrizGulosa

def main():
    itens = []
    item = int(input("Digite a quantidade de itens: "))
    for i in range(1, item + 1):
        itens.append(i)

    beneficio = []
    for i in itens:
        aux = int(input(f"Digite o benefício do item {i}: "))
        beneficio.append(aux)

    peso = []
    for i in itens:
        aux = int(input(f"Digite o peso do item {i}: "))
        peso.append(aux)

    capacidade = int(input("Digite a capacidade da mochila: "))

    resultado = EstrategiaGulosa(itens, beneficio, peso, capacidade)

    # Imprimindo a matriz de forma tabular
    for row in resultado:
        print(" ".join(f"{elem:<15}" for elem in row))

if __name__ == "__main__":
    main()
