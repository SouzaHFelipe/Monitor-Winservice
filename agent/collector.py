import psutil
import time
from datetime import datetime , timezone , time
from config import *

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