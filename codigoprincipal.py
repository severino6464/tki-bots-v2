import subprocess
import os
from concurrent.futures import ThreadPoolExecutor

# Função para executar um código de sala em loop
def executar_sala(sala_codigo):
    while True:
        subprocess.run(["python3", os.path.join(base_path, sala_codigo)])

# Número total de salas
num_salas = 200

# Caminho para a pasta onde o código está sendo executado
base_path = os.path.dirname(os.path.abspath(__file__))

# Limitar o número máximo de threads ativas
max_threads = 10

# Criar ThreadPoolExecutor
executor = ThreadPoolExecutor(max_workers=max_threads)

# Loop para criar threads para cada sala e iniciar a execução em loop
for sala_numero in range(1, num_salas + 1):
    sala_codigo = "sala{}.py".format(sala_numero)
    executor.submit(executar_sala, sala_codigo)

# Aguardar a conclusão de todas as tarefas
executor.shutdown(wait=True)
