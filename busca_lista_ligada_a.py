import random
import sys
import time
import statistics
import numpy as np


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def create_linked_list(arr):
    head = None
    for data in arr:
        head = append(head, data)
    return head

def search(head, key):
    current = head
    position = 0
    while current:
        if current.data == key:
            return position
        elif current.data > key:
            return -1  # Valor não encontrado, a lista está ordenada
        current = current.next
        position += 1
    return -1

def busca_sequencial_lista_ligada(head, valor):
    comparacoes = 0  # variável contadora de comparações
    current = head
    position = 0
    while current:
        comparacoes += 1  # incrementa a cada comparação feita
        if current.data == valor:
            # retorna a posição do valor encontrado e o número de comparações feitas
            return position, comparacoes
        elif current.data > valor:
            break  # Valor não encontrado, a lista está ordenada
        current = current.next
        position += 1
    # retorna -1 se o valor não foi encontrado e o número de comparações feitas
    return -1, comparacoes

for i in range(1, 11):
    # for j in range(1, 2):
        arr = np.loadtxt(f'./data/arranjo_{i}.txt', dtype=int)

        # Convertendo o arr em uma lista
        lista = arr.tolist()
        # print(lista)

        # Ordenando a lista
        # lista.sort()
        # lista = sorted(lista)

        # Gerar 100 valores aleatórios para busca
        # valores_busca = random.sample(lista, 100)
        valores_busca = {1000000}

        # Criação da lista ligada
        linked_list = create_linked_list(lista)

        # Arr para guardar os tempos
        tempos = []
        # Arr para guardar as comparações
        comparacoes = []

        # Redireciona a saída padrão para o arquivo
        sys.stdout = open(
            f'./result/busca_ligada/case_a/resultado_buscaListaLigada_aleatorio_{i}.txt', 'w')

        # Realizar busca sequencial para cada valor
        for valor in valores_busca:
            inicio = time.time()  # registrar tempo de início
            posicao, num_comparacoes = busca_sequencial_lista_ligada(
                linked_list, valor)
            fim = time.time()  # registrar tempo de término

            tempo = fim - inicio  # calcular diferença entre tempos para obter o tempo total
            tempos.append(tempo)
            comparacoes.append(num_comparacoes)

            if posicao != -1:
                print(
                    f"O valor {valor} foi encontrado na posição {posicao} da lista ligada. Tempo de busca: {tempo} segundos. Número de comparações: {num_comparacoes}")
            else:
                print(
                    f"O valor {valor} não foi encontrado na lista ligada. Tempo de busca: {tempo} segundos. Número de comparações: {num_comparacoes}")

        print('\nCalcular tempo médio')
        tempo_medio = sum(tempos) / len(tempos)
        print(f"Tempo médio de busca: {tempo_medio} segundos.")

        print('\nCalcular o tempo total')
        print(f"Tempo das buscas: {tempos} segundos.")
        tempo_total = sum(tempos)
        print(f"Tempo total da busca: {tempo_total} segundos.")

        # print('\nCalcular desvio padrão')
        # desvio_padrao = statistics.stdev(tempos)
        # print(f"Desvio padrão (tempo): {desvio_padrao}")

        print('\nCalcular desvio padrão')
        if len(tempos) > 1:
            desvio_padrao = statistics.stdev(tempos)
        else:
            desvio_padrao = 0.0  # Definir desvio padrão como zero para apenas um elemento
        print(f"Desvio padrão (tempo): {desvio_padrao}")


        with open(f'./result/busca_ligada/case_a/resultado_buscaListaLigada_aleatorio_{i}.txt', 'w') as file:
            file.write(f"{tempo_medio}\n")
            file.write(f"{desvio_padrao}\n")

