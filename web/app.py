from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

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
    # Impede que o navegador guarde cache da chamada de API
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=5001)