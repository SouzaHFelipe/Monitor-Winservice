# 🖥️ Monitor-Winservice

Monitoramento de recursos de máquinas **Windows** utilizando Python.

O **Monitor-Winservice** é um projeto desenvolvido para monitorar recursos do sistema em tempo real, coletando métricas de CPU, memória RAM, disco e rede.

O projeto possui um agente responsável pela coleta das métricas e uma aplicação web desenvolvida com Flask para visualização dos dados.

> 🚧 Projeto em desenvolvimento — novas funcionalidades e melhorias estão sendo implementadas.

---

## 📌 Funcionalidades

* 📊 Monitoramento de CPU
* 🧠 Monitoramento de memória RAM
* 💾 Monitoramento de utilização do disco
* 🌐 Monitoramento de tráfego de rede
* 📝 Registro das métricas em arquivo de log
* 🚨 Detecção de métricas acima dos limites configurados
* 📧 Envio de alertas por e-mail
* 🌐 Dashboard web para visualização das métricas
* 🔌 API REST para disponibilização dos dados

---

## 🏗️ Arquitetura

O projeto é dividido em duas partes principais:

```text
Monitor-Winservice/
│
├── agent/
│   ├── collector.py
│   ├── config.py
│   ├── data_class.py
│   ├── main.py
│   ├── notifier.py
│   ├── reader.py
│   └── metrics.log
│
├── web/
│   ├── app.py
│   ├── templates/
│   └── static/
│
└── README.md
```

### Agent

O agente é responsável por coletar as informações da máquina utilizando a biblioteca `psutil`.

As principais métricas coletadas são:

```text
CPU
RAM
DISCO
REDE
```

As informações são armazenadas em formato JSON no arquivo `metrics.log`.

### Web

A aplicação web utiliza **Flask** para disponibilizar o dashboard e uma API responsável por retornar as métricas coletadas.

Endpoint disponível:

```text
GET /api/metrics
```

A API retorna as últimas métricas registradas pelo agente.

---

## ⚙️ Tecnologias

* 🐍 Python
* 🌐 Flask
* 📊 Psutil
* 🟨 JavaScript
* 🎨 HTML / CSS
* 📦 JSON
* 📝 File Logging

---

## 🚀 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/SouzaHFelipe/Monitor-Winservice.git
```

Entre na pasta:

```bash
cd Monitor-Winservice
```

---

### 2. Crie um ambiente virtual

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```bash
venv\Scripts\activate
```

---

### 3. Instale as dependências

Caso o projeto possua um `requirements.txt`:

```bash
pip install -r requirements.txt
```

Ou instale as principais dependências:

```bash
pip install flask psutil
```

---

## ▶️ Executando o projeto

O projeto possui dois componentes principais: o **Agent** e o **Web Dashboard**.

### 1. Inicie o Agent

A partir da raiz do projeto:

```bash
python -m agent.main
```

O agente começará a coletar as métricas da máquina e registrá-las no arquivo:

```text
agent/metrics.log
```

Exemplo de dados coletados:

```json
{
    "timestamp": "2026-08-18T17:00:00+00:00",
    "cpu_percent": 22.1,
    "memory_percent": 61.7,
    "disk_percent": 95.0,
    "network": {
        "bytes_sent": 66998510,
        "bytes_recv": 470760394
    }
}
```

---

### 2. Inicie o Web Dashboard

Em outro terminal:

```bash
python -m web.app
```

A aplicação será iniciada na porta:

```text
5001
```

Acesse no navegador:

```text
http://localhost:5001
```

---

## 🔔 Sistema de alertas

O agente possui um mecanismo de verificação de limites.

Os valores podem ser configurados no arquivo:

```text
agent/config.py
```

Exemplo de limites:

```python
CPU_THRESHOLD = 80
RAM_THRESHOLD = 80
DISK_THRESHOLD = 90
```

Quando uma métrica ultrapassa o limite configurado, o sistema pode gerar um alerta por e-mail.

As configurações de e-mail devem ser definidas através das variáveis correspondentes no arquivo de configuração.

> ⚠️ Nunca publique senhas ou credenciais diretamente no código ou no repositório.

---

## 📡 API

O dashboard disponibiliza uma API para consulta das métricas:

```http
GET /api/metrics
```

Exemplo:

```bash
curl http://localhost:5001/api/metrics
```

Resposta:

```json
[
    {
        "timestamp": "2026-08-18T17:00:00+00:00",
        "cpu_percent": 22.1,
        "memory_percent": 61.7,
        "disk_percent": 95.0,
        "network": {
            "bytes_sent": 66998510,
            "bytes_recv": 470760394
        }
    }
]
```

---

## 🎯 Objetivo do projeto

O objetivo do projeto é explorar, na prática, conceitos relacionados a:

* Monitoramento de infraestrutura
* Desenvolvimento em Python
* Coleta de métricas
* APIs REST
* Desenvolvimento Web
* Automação
* Observabilidade
* Alertas de infraestrutura
* Integração entre backend e frontend

A ideia é evoluir o projeto gradualmente, aproximando sua arquitetura de ferramentas de monitoramento utilizadas em ambientes reais.

---

## 🔮 Próximos passos

Algumas funcionalidades planejadas:

* [ ] Monitoramento de serviços do Windows
* [ ] Monitoramento de processos
* [ ] Histórico de métricas
* [ ] Banco de dados para armazenamento
* [ ] Dashboard em tempo real
* [ ] Sistema de alertas configurável
* [ ] Docker
* [ ] API mais completa
* [ ] Autenticação
* [ ] Exportação de métricas
* [ ] Integração com ferramentas de observabilidade
* [ ] Execução do Agent como Windows Service

---

## 📚 Conceitos utilizados

Este projeto também serve como laboratório para estudar conceitos de:

```text
Python
   │
   ├── System Monitoring
   ├── Automation
   ├── File Logging
   └── Exception Handling
        │
        ▼
     Flask
        │
        ├── REST API
        └── Web Dashboard
        │
        ▼
     Metrics
        │
        ├── CPU
        ├── RAM
        ├── Disk
        └── Network
```

---

## 👨‍💻 Autor

**Felipe Henrique de Souza**

Projeto desenvolvido para estudos e evolução prática em:

**Python • Cloud • Infrastructure • Monitoring • Automation • AWS**

---

## 📄 Licença

Este projeto está disponível para fins de estudo e desenvolvimento.
