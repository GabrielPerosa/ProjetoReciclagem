document.addEventListener('DOMContentLoaded', function () {

    async function carregarMonitoramento() {
      try {
        const pecas = ["metalicas", "plasticas", "descarte"];
        const requests = pecas.map(tipo =>
          fetch(`https://ydsdpxj25l.execute-api.us-east-1.amazonaws.com/production-parts/by-type/${tipo}`)
        );
  
        const responses = await Promise.all(requests);
        responses.forEach(response => {
          if (!response.ok) {
            throw new Error(`Erro na API: ${response.status}`);
          }
        });
  
        const dados = await Promise.all(responses.map(res => res.json()));
        const hoje = new Date().toISOString().slice(0, 10);
  
        const tabelaSensores = document.querySelector('.table-container:nth-child(1) tbody');
        const tabelaSaidas = document.querySelector('.table-container:nth-child(2) tbody');
  
        // Limpa as tabelas antes de popular
        tabelaSensores.innerHTML = '';
        tabelaSaidas.innerHTML = '';
  
        // Exemplo: Preencher sensores
        const sensores = [
          { nome: "Sensor Indutivo", tipo: "metalicas" },
          { nome: "Sensor Capacitivo", tipo: "plasticas" },
          { nome: "Sensor Óptico", tipo: "descarte" },
        ];
  
        sensores.forEach(sensor => {
          const tipoIndex = pecas.indexOf(sensor.tipo);
          const registros = dados[tipoIndex].filter(item => item.timestamp.slice(0, 10) === hoje);
          const status = registros.length > 0 ? 'Ativado' : 'Desativado';
  
          const linha = `
            <tr>
              <td>${sensor.nome}</td>
              <td>${hoje}</td>
              <td><span class="status ${status.toLowerCase()}">${status}</span></td>
            </tr>
          `;
          tabelaSensores.insertAdjacentHTML('beforeend', linha);
        });
  
        // Exemplo: Preencher saídas
        const saidas = [
          { nome: "Atuador 1", tipo: "metalicas" },
          { nome: "Atuador 2", tipo: "plasticas" },
          { nome: "Esteira", tipo: "descarte" },
        ];
  
        saidas.forEach(saida => {
          const tipoIndex = pecas.indexOf(saida.tipo);
          const registros = dados[tipoIndex].filter(item => item.timestamp.slice(0, 10) === hoje);
          const status = registros.length > 0 ? 'Ativado' : 'Desativado';
  
          const linha = `
            <tr>
              <td>${saida.nome}</td>
              <td>${hoje}</td>
              <td><span class="status ${status.toLowerCase()}">${status}</span></td>
            </tr>
          `;
          tabelaSaidas.insertAdjacentHTML('beforeend', linha);
        });
  
      } catch (error) {
        console.error("Erro ao carregar monitoramento:", error);
        alert("Erro ao buscar dados da API!");
      }
    }
  
    carregarMonitoramento();
  
    // Sidebar Menu
    const btnHamburger = document.getElementById('hamburger-btn');
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.overlay');
  
    function toggleMenu() {
      sidebar.classList.toggle('active');
      overlay.classList.toggle('active');
    }
  
    if (btnHamburger) btnHamburger.addEventListener('click', toggleMenu);
    if (overlay) overlay.addEventListener('click', toggleMenu);
  });
  