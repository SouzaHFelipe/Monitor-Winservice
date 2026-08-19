from flask import Flask, render_template, jsonify
import json
import os
from agent.collector import MetricsCollector


app = Flask(__name__)

collector_web = MetricsCollector()

# Descobre o caminho absoluto para a pasta do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FILE_PATH = os.path.join(BASE_DIR, "agent", "metrics.log")

def read_last_metrics(limit=20):
    metrics = []
    # Se o arquivo metrics.log ainda nao existir, retorna lista vazia sem quebrar
    if not os.path.exists(LOG_FILE_PATH):
        return metrics

    try:
        with open(LOG_FILE_PATH, "r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines[-limit:]:
                if line.strip():
                    metrics.append(json.loads(line.strip()))
    except Exception as e:
        print(f"Erro ao ler os logs: {e}")

    return metrics

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/metrics")
def get_metrics():
    data = read_last_metrics(limit=20)
    response = jsonify(data)
    return response

@app.route("/api/processes")
def api_processes():
    """Rota que retorna os processos atuais do computador."""
    try:
        procs = collector_web.get_running_processes()
        return jsonify(procs), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=5001)