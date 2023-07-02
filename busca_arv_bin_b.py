import os
import time
import random
import statistics

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    return node

def build_tree_from_file(file_path):
    root = None

    with open(file_path, 'r') as file:
        for line in file:
            key = int(line.strip())
            root = insert(root, key)

    return root

def search(node, key):
    comparisons = 0  # Variável para contar as comparações

    while node is not None:
        comparisons += 1

        if node.key == key:
            return node, comparisons
        elif key < node.key:
            node = node.left
        else:
            node = node.right

    return None, comparisons

def save_result_to_file(result, search_time, comparisons, std_deviation, file_path):
    with open(file_path, 'w') as file:
        if result is None:
            file.write("A chave não foi encontrada na árvore.")
        else:
            file.write(f"A chave foi encontrada na árvore.")
        file.write(f"Tempo de busca: {search_time:.6f} segundos.")
        file.write(f"Número de comparações: {comparisons}")
        file.write(f"Desvio padrão do tempo de busca: {std_deviation:.6f} segundos.")

# Diretório de entrada
input_directory = './data/'

# Diretório de saída
output_directory = './result/busca_arv/case_b/'

# Lista de arquivos de entrada
input_files = ['arranjo_1.txt', 'arranjo_2.txt', 'arranjo_3.txt', 'arranjo_4.txt', 'arranjo_5.txt',
               'arranjo_6.txt', 'arranjo_7.txt', 'arranjo_8.txt', 'arranjo_9.txt', 'arranjo_10.txt']

# Número de valores aleatórios a serem buscados
num_values = 100

# Loop para cada arquivo de entrada
for input_file in input_files:
    # Caminho completo do arquivo de entrada
    input_file_path = os.path.join(input_directory, input_file)
    
    # Caminho do diretório de saída para o arquivo específico
    output_subdirectory = os.path.join(output_directory, os.path.splitext(input_file)[0])
    os.makedirs(output_subdirectory, exist_ok=True)
    
    # Construir a árvore binária
    root = build_tree_from_file(input_file_path)
    
    # Lista para armazenar os resultados da busca para os valores aleatórios
    search_results = []
    
    # Realizar a busca para os valores aleatórios
    for _ in range(num_values):
        # Valor aleatório a ser buscado
        key_to_search = random.randint(1, 1000000)
        
        # Realizar a busca e calcular o tempo
        start_time = time.time()
        result, comparisons = search(root, key_to_search)
        time.sleep(1)  # Atraso de 1 segundo
        end_time = time.time()
        search_time = end_time - start_time
        
        # Adicionar o resultado da busca à lista
        search_results.append((key_to_search, result, search_time, comparisons))
    
    # Calcular a média de comparações e tempo
    mean_comparisons = sum(comparisons for _, _, _, comparisons in search_results) / num_values
    mean_search_time = sum(search_time for _, _, search_time, _ in search_results) / num_values
    
    # Calcular o desvio padrão dos tempos de busca
    search_times = [search_time for _, _, search_time, _ in search_results]
    std_deviation = statistics.stdev(search_times)
    
    # Caminho completo do arquivo de saída
    output_file_path = os.path.join(output_subdirectory, 'resultado_busca_arv.txt')
    
    # Salvar os resultados no arquivo de saída
    with open(output_file_path, 'w') as file:
        for key_to_search, result, search_time, comparisons in search_results:
            if result is None:
                file.write(f"A chave {key_to_search} não foi encontrada na árvore.\n")
            else:
                file.write(f"A chave {key_to_search} foi encontrada na árvore.\n")
            file.write(f"Tempo de busca: {search_time:.6f} segundos.\n")
            file.write(f"Número de comparações: {comparisons}\n")
        
        file.write(f"Média de comparações: {mean_comparisons}\n")
        file.write(f"Média de tempo de busca: {mean_search_time:.6f} segundos.\n")
        file.write(f"Desvio padrão do tempo de busca: {std_deviation:.6f} segundos.\n")
