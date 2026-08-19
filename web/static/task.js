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