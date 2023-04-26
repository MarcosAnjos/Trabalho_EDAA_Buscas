import numpy as np
import random
import sys
import time
import statistics
import math

def busca_binaria(lista, valor):
    esquerda, direita = 0, len(lista) - 1
    comparacoes = 0
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        comparacoes += 1
        if lista[meio] == valor:
            # retorna o índice do valor encontrado e o número de comparações feitas
            return meio, comparacoes
        elif lista[meio] > valor:
            direita = meio - 1
        else:
            esquerda = meio + 1
        time.sleep(0.001)
    # retorna -1 se o valor não foi encontrado e o número de comparações feitas
    return -1, comparacoes


for i in range(1, 11):
    for j in range(1, 4):
     
        arr = np.loadtxt(f'./data/arranjo_{i}.txt', dtype=int)

        # Convertendo o arr em uma lista
        lista = arr.tolist()
        # print(lista)

        # Ordenar a lista (REQUESITO DO JUMP SEARCH)
        lista = sorted(lista)

        # Gerar 100 valores aleatórios para busca
        valores_busca = random.sample(lista, 100)
        #valores_busca = {1000000}
        # Arr para guardar os tempos
        tempos = []
        # Arr para guardar as comparacao
        comparacoes = []

        # Redireciona a saída padrão para o arquivo
        sys.stdout = open(
            f'./result/busca_bin/case_b/resultado_buscaBin_aleatorio_{i}_{j}.txt', 'w')

        # Realizar busca sequencial para cada valor
        for valor in valores_busca:
            inicio = time.time()  # registrar tempo de início
            indice, num_comparacoes = busca_binaria(
                lista, valor)
            fim = time.time()  # registrar tempo de término

            tempo = fim - inicio  # calcular diferença entre tempos para obter o tempo total
            tempos.append(tempo)
            comparacoes.append(num_comparacoes)

            if indice != -1:
                print(
                    f"O valor {valor} foi encontrado na posicao {indice} da lista. Tempo de busca: {tempo} segundos. Numero de comparacoes: {num_comparacoes}")
            else:
                print(
                    f"O valor {valor} nao foi encontrado na lista. Tempo de busca: {tempo} segundos. Numero de comparacoes: {num_comparacoes}")
        
        # print('\n\n\nVetor de busca dos numeros')
        # print(f"{valores_busca}")

        print('\nCalcular tempo medio')
        tempo_medio = sum(tempos) / len(tempos)
        print(f"Tempo medio de busca: {tempo_medio} segundos.")

        print('\nCalcular o tempo total')
        print(f"Tempo das buscas: {tempos} segundos.")
        tempo_total = 0
        for tempo in tempos:
            tempo_total += tempo

        print(f"Tempo total da busca: {tempo_total} segundos.")
      
        
        media_comparacao = statistics.mean(comparacoes)
        print(f'\n\nMedia comparacao = {media_comparacao}')

        print('\nCalcular desvio Padrao')
        desvio_padrao = statistics.stdev(tempos)
        print(f"Desvio Padrao (tempo): {desvio_padrao}")
        with open(f'./result/busca_bin/case_b/resultado_buscaBin_aleatorio_{i}_{j}.txt', 'w') as file:
            file.write(f"{tempo_medio}\n")
            #file.write(f"{desvio_padrao}\n")