import time
import json
from collector import MetricsCollector
from config import LOG_FILE_PATH , COLLECT_INTERVAL , CPU_THRESHOLD
from notifier import send_email_alert
import config

collector = MetricsCollector()
LOG_FILE = LOG_FILE_PATH

print("=== Py-Monitor Agent Iniciado ===")
print("Pressione Ctrl+C para encerrar no terminal.\n")

def save_to_log(data):
    with open(LOG_FILE , "a" , encoding='utf-8') as file:
        file.write(json.dumps(data) + "\n")


def check_alerts(metrics):
    
    alerts = []
    
    if metrics['cpu_percent'] > config.CPU_THRESHOLD:
        alerts.append(f"- CPU em {metrics['cpu_percent']}% (Limite: {config.CPU_THRESHOLD}%)")
        
         
    if metrics['disk_percent'] > config.DISK_THRESHOLD:
       alerts.append(f"- RAM em {metrics['memory_percent']}% (Limite: {config.RAM_THRESHOLD}%)")
       
    if metrics['memory_percent'] > config.RAM_THRESHOLD:
        alerts.append(f"- DISCO em {metrics['disk_percent']}% (Limite: {config.DISK_THRESHOLD}%)")

    if alerts:
        subject = f" ALERTA DE SISTEMA: {len(alerts)} problema(s) detectado(s)"
        
        # Junta todos os alertas da lista em um texto com quebras de linha
        alert_text = "\n".join(alerts)
        body = (
            f"O Py-Monitor detectou métricas acima do limite em {metrics['timestamp']}:\n\n"
            f"{alert_text}\n\n"
            f"Por favor, verifique o servidor."
            
        )
        
    
    send_email_alert(
            subject=subject,
            body=body,
            sender=config.EMAIL_SENDER,
            password=config.EMAIL_PASSWORD,
            receiver=config.EMAIL_RECEIVER,
            smtp_server=config.SMTP_SERVER,
            smtp_port=config.SMTP_PORT
        )
    
    
try:
    while True:
        metrics = collector.collect_all()
        
        save_to_log(metrics)

        
        # Exibimos no terminal de forma organizada
        print(f"Timestamp: {metrics['timestamp']}")
        print(f"CPU      : {metrics['cpu_percent']}%")
        print(f"RAM      : {metrics['memory_percent']}%")
        print(f"DISCO    : {metrics['disk_percent']}%")
        print(f"REDE     : Enviados {metrics['network']['bytes_sent']} B | Recebidos {metrics['network']['bytes_recv']} B")
        
        check_alerts(metrics)
        
        time.sleep(config.COLLECT_INTERVAL)

except KeyboardInterrupt:
    print("Encerrado pelo user")
    
    
    