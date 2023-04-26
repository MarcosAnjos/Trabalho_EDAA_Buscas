import numpy as np

max_elementos = 100000
num_arranjos = 10
intervalo = 100000

for i in range(num_arranjos):
    # Gerar o arranjo de números sem repetição
    arr = np.random.permutation(max_elementos)
    np.savetxt(f"./data/arranjo_{i+1}.txt", arr, fmt="%d")
    max_elementos += intervalo  # 100.000 +100.000 (cada interacao)
