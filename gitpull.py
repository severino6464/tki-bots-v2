import subprocess
import os
import time

# Obter o diretório atual do arquivo Python
current_directory = os.path.dirname(os.path.abspath(__file__))

while True:
    try:
        # Executa o comando git pull
        subprocess.run(["git", "pull"], cwd=current_directory, check=True)
        print("Git pull bem-sucedido.")
    except Exception as e:
        print(f"Erro ao executar git pull: {e}")


    time.sleep(10)
