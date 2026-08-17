import json
from config import LOG_FILE_PATH

def read_last_logs(limit=5):
    """Lê e retorna as últimas 'limit' linhas do arquivo de log."""
    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as file:
            # Lê todas as linhas do arquivo
            lines = file.readlines()
            
            # Pega apenas as últimas 'limit' linhas usando fatiamento de lista (slice)
            last_lines = lines[-limit:]
            
            # Converte cada linha de texto em JSON de volta para dicionário Python
            logs = [json.loads(line) for line in last_lines]
            return logs

    except FileNotFoundError:
        print("Arquivo de log ainda não existe. Inicie o main.py primeiro!")
        return []

if __name__ == "__main__":
    print("=== Lendo as últimas 5 métricas salvas ===")
    
    recent_logs = read_last_logs(limit=5)
    
    for log in recent_logs:
        timestamp = log['timestamp']
        cpu = log['cpu_percent']
        ram = log['memory_percent']
        print(f"[{timestamp}] -> CPU: {cpu}% | RAM: {ram}%")