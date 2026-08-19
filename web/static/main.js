// Configuração do Gráfico Chart.js
const ctx = document.getElementById('metricsChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [
            { label: 'CPU (%)', borderColor: '#60a5fa', backgroundColor: 'rgba(96, 165, 250, 0.1)', data: [], tension: 0.3, fill: true },
            { label: 'RAM (%)', borderColor: '#c084fc', backgroundColor: 'rgba(192, 132, 252, 0.1)', data: [], tension: 0.3, fill: true },
            { label: 'DISCO (%)', borderColor: '#fbbf24', backgroundColor: 'rgba(251, 191, 36, 0.1)', data: [], tension: 0.3, fill: true }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
            x: { ticks: { color: '#94a3b8' }, grid: { color: '#334155' } },
            y: { min: 0, max: 100, ticks: { color: '#94a3b8' }, grid: { color: '#334155' } }
        },
        plugins: {
            legend: { labels: { color: '#f8fafc' } }
        }
    }
});


function atualizarProcessos() {
    fetch('/api/processes')
        .then(response => response.json())
        .then(data => {
            const tbody = document.getElementById('process-table-body');
            tbody.innerHTML = ''; // Limpa a tabela
            
            data.forEach(proc => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${proc.pid}</td>
                    <td>${proc.name}</td>
                    <td>${proc.cpu_percent}%</td>
                    <td>${proc.memory_percent}%</td>
                `;
                tbody.appendChild(tr);
            });
        });
}

// Atualiza a cada 3 segundos
setInterval(atualizarProcessos, 3000);
atualizarProcessos(); // Executa logo de cara

// Função para buscar dados da API Flask
async function fetchMetrics() {
    try {
        const response = await fetch('/api/metrics');
        const data = await response.json();

        if (data.length === 0) return;

        // Pega a métrica mais recente
        const latest = data[data.length - 1];
        document.getElementById('cpu-value').innerText = `${latest.cpu_percent}%`;
        document.getElementById('ram-value').innerText = `${latest.memory_percent}%`;
        document.getElementById('disk-value').innerText = `${latest.disk_percent}%`;

        // Atualiza o gráfico
        // Extrai um rótulo de tempo legível a partir do timestamp ISO
        chart.data.labels = data.map(m => new Date(m.timestamp).toLocaleTimeString());
        chart.data.datasets[0].data = data.map(m => m.cpu_percent);
        chart.data.datasets[1].data = data.map(m => m.memory_percent);
        chart.data.datasets[2].data = data.map(m => m.disk_percent);
        chart.update();

    } catch (error) {
        console.error("Erro ao carregar métricas:", error);
    }
}

// Atualiza a cada 3 segundos
setInterval(fetchMetrics, 3000);
fetchMetrics();
lucide.createIcons();