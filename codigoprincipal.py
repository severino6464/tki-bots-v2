import subprocess
import os
import threading


# Função para executar um código de sala em loop
def executar_sala(sala_codigo):
    while True:
        subprocess.run(["python3", os.path.join(base_path, sala_codigo)])

# Número total de salas
num_salas = 200

# Caminho para a pasta onde o código está sendo executado
base_path = os.path.dirname(os.path.abspath(__file__))

# Lista para armazenar as threads
threads = []

# Loop para criar threads para cada sala e iniciar a execução em loop
for sala_numero in range(1, num_salas + 1):
    sala_codigo = "sala{}.py".format(sala_numero)"


    
    thread = threading.Thread(target=executar_sala, args=(sala_codigo,))
    threads.append(thread)
    thread.start()
    

# Aguardar todas as threads terminarem (que não acontecerá nesse caso)
for thread in threads:
    thread.join()
