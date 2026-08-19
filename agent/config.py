import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(BASE_DIR, "metrics.log")

COLLECT_INTERVAL = 60
#LOG_FILE_PATH = "agent/metrics.log"
DISK_PATH = "C:\\"

# Limites para alertas (%)
CPU_THRESHOLD = 80.0
RAM_THRESHOLD = 85.0
DISK_THRESHOLD = 90.0

# --- CONFIGURAÇÕES DE E-MAIL (SMTP) ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "seu_email@gmail.com"
EMAIL_PASSWORD = "sua_senha_de_app"
EMAIL_RECEIVER = "seu_email@gmail.com"