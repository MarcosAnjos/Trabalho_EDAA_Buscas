import os
import time

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

def save_result_to_file(result, search_time, comparisons, file_path):
    with open(file_path, 'w') as file:
        if result is None:
            file.write("A chave não foi encontrada na árvore.")
        else:
            file.write(f"A chave foi encontrada na árvore.")
        file.write(f"Tempo de busca: {search_time:.6f} segundos.")
        file.write(f"Número de comparações: {comparisons}")

# Diretório de entrada
input_directory = './data/'

# Diretório de saída
output_directory = './result/busca_arv/'

# Lista de arquivos de entrada
input_files = ['arranjo_1.txt', 'arranjo_2.txt', 'arranjo_3.txt', 'arranjo_4.txt', 'arranjo_5.txt',
               'arranjo_6.txt', 'arranjo_7.txt', 'arranjo_8.txt', 'arranjo_9.txt', 'arranjo_10.txt']

# Valor a ser buscado
key_to_search = 1000000

# Loop para cada arquivo de entrada
for input_file in input_files:
    # Caminho completo do arquivo de entrada
    input_file_path = os.path.join(input_directory, input_file)
    
    # Caminho do diretório de saída para o arquivo específico
    output_subdirectory = os.path.join(output_directory, os.path.splitext(input_file)[0])
    os.makedirs(output_subdirectory, exist_ok=True)
    
    # Caminho completo do arquivo de saída
    output_file_path = os.path.join(output_subdirectory, 'resultado_busca_arv.txt')
    
    # Construir a árvore binária
    root = build_tree_from_file(input_file_path)
    
    # Realizar a busca e calcular o tempo
    start_time = time.time()
    result, comparisons = search(root, key_to_search)
    time.sleep(1)  # Atraso de 1 segundo
    end_time = time.time()
    search_time = end_time - start_time
    
    # Salvar o resultado no arquivo de saída
    save_result_to_file(result, search_time, comparisons, output_file_path)
