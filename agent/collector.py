import psutil
import time
from datetime import datetime, timezone
from agent.config import *

class MetricsCollector:
    
    def __init__(self):
        self.disk_path = DISK_PATH
    
    def get_cpu(self):    
        return psutil.cpu_percent(interval=1)
    
    def get_memory(self):
        return psutil.virtual_memory().percent
    
    def get_disk(self):
        return psutil.disk_usage("C:\\").percent
    
    def get_network(self):
        net = psutil.net_io_counters()
        return {
            "bytes_sent": net.bytes_sent,
            "bytes_recv": net.bytes_recv
        }
        

    def collect_all(self):
        
        """Coleta todas as métricas e junta em um único dicionário."""
        return {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cpu_percent": self.get_cpu(),
            "memory_percent": self.get_memory(),
            "disk_percent": self.get_disk(),
            "network": self.get_network()
        }

    def get_running_processes(self):
        """Retorna uma lista com os processos que mais consomem CPU/Memória."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                pinfo = proc.info
                processes.append({
                    "pid": pinfo['pid'],
                    "name": pinfo['name'],
                    "cpu_percent": pinfo['cpu_percent'] or 0.0,
                    "memory_percent": round(pinfo['memory_percent'] or 0.0, 2)
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        
        # Ordena pelos processos que mais gastam CPU e pega apenas os top 10
        processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
        return processes[:10]