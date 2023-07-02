import os
import time
import psutil

def sort_numbers(file_path):
    # Carrega os números do arquivo TXT
    with open(file_path, 'r') as file:
        numbers = [int(line.strip()) for line in file]

    # Inicia a contagem do tempo
    start_time = time.time()

    # Realiza a ordenação dos números
    numbers.sort()

    # Calcula o tempo gasto em segundos
    execution_time = time.time() - start_time

    # Obtém o consumo de memória RAM em bytes
    process = psutil.Process()
    memory_usage = process.memory_info().rss

    # Converte o consumo de memória para megabytes (MB)
    memory_usage_mb = memory_usage / (1024 * 1024)

    # Salva as informações em um arquivo TXT
    output_file_path = file_path.replace('./data/', './result/ordenacao/')
    with open(output_file_path, 'w') as output_file:
        output_file.write(f"Tempo de execução: {execution_time} segundos\n")
        output_file.write(f"Consumo de memória: {memory_usage_mb} MB\n")

    print(f"Ordenação do arquivo '{file_path}' concluída. Resultados salvos em '{output_file_path}'.")

# Pasta que contém os arquivos de entrada
input_folder = './data/'

# Percorre todos os arquivos na pasta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith(".txt"):
        input_file_path = os.path.join(input_folder, filename)
        sort_numbers(input_file_path)
