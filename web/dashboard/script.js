document.addEventListener('DOMContentLoaded', function () {

  async function PuxarDados() { 
    try {
      const pecas = ["metalicas", "plasticas", "descarte"];
      const requests = pecas.map(peca =>
        fetch(`https://ydsdpxj25l.execute-api.us-east-1.amazonaws.com/production-parts/by-type/${peca}`)
      );

      const responses = await Promise.all(requests);

      responses.forEach(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
      });

      const dados = await Promise.all(responses.map(res => res.json()));

      // Processar dados para totais mensais
      const monthlyData = {
        metalicas: Array(12).fill(0), // Inicializa 12 meses com 0
        plasticas: Array(12).fill(0),
        descarte: Array(12).fill(0)
      };

      let hojeMetal = 0;
      let hojePlastico = 0;
      let hojeDescarte = 0;
      const hoje = new Date().toISOString().slice(0, 10);

      // Processar os dados de cada tipo de peça
      dados.forEach((data, index) => {
        const partType = pecas[index];
        if (Array.isArray(data)) {
          data.forEach(item => {
            const date = new Date(item.timestamp);
            const month = date.getMonth(); // 0 = Jan, 1 = Fev, ..., 11 = Dez
            monthlyData[partType][month] += item.stored_quantity;
            const dataItem = item.timestamp.slice(0, 10);
            if (dataItem === hoje) {
              if (partType === 'metalicas') hojeMetal += item.stored_quantity;
              else if (partType === 'plasticas') hojePlastico += item.stored_quantity;
              else if (partType === 'descarte') hojeDescarte += item.stored_quantity;
            }
          });
        }
      });

      // Calcular totais gerais para exibição nos elementos HTML
      const quantidadeMetal = monthlyData.metalicas.reduce((sum, val) => sum + val, 0);
      const quantidadePlastico = monthlyData.plasticas.reduce((sum, val) => sum + val, 0);
      const quantidadeDescarte = monthlyData.descarte.reduce((sum, val) => sum + val, 0);
      const quantidadeTotal = quantidadeDescarte + quantidadeMetal + quantidadePlastico

      const totalhoje = hojeMetal + hojePlastico + hojeDescarte


      console.log(monthlyData);
      console.log(quantidadeMetal, quantidadePlastico, quantidadeDescarte);


      document.getElementById("rampa1").textContent = quantidadeMetal;
      document.getElementById("rampa2").textContent = quantidadePlastico;
      document.getElementById("descarte").textContent = quantidadeDescarte;
      document.getElementById("pecas_total").textContent = quantidadeTotal;

      document.getElementById("rampa1hoje").textContent = hojeMetal;
      document.getElementById("rampa2hoje").textContent = hojePlastico;
      document.getElementById("descartehoje").textContent = hojeDescarte;
      document.getElementById("pecas_totalhoje").textContent = totalhoje;
      
      const aproveitamento_mensal =((quantidadeTotal - quantidadeDescarte) / quantidadeTotal) * 100
      document.getElementById("aprov-mensal").textContent = aproveitamento_mensal.toFixed(2) + "%"
      document.getElementById("aprove-mensal").style.width = `${aproveitamento_mensal.toFixed(2)}%`;

      const aproveitamento_diario =((totalhoje - hojeDescarte) / totalhoje) * 100
      document.getElementById("aprov-diario").textContent = aproveitamento_diario.toFixed(2) + "%"
      document.getElementById("aprove-diario").style.width = `${aproveitamento_diario.toFixed(2)}%`;

      // ---------------- Gráfico ----------------
      const ctxPecas = document.getElementById('pecasChart')?.getContext('2d');
      if (ctxPecas) {
        new Chart(ctxPecas, {
          type: 'line',
          data: {
            labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
            datasets: [
              {
                label: 'Metal',
                data: monthlyData.metalicas,
                backgroundColor: 'rgba(65, 105, 225, 0.7)',
                borderColor: '#4169E1',
                borderWidth: 1,
                pointRadius: 4,
              },
              {
                label: 'Plástico',
                data: monthlyData.plasticas,
                backgroundColor: 'rgba(50, 205, 50, 0.7)',
                borderColor: '#32CD32',
                borderWidth: 1,
                pointRadius: 4,
              },
              {
                label: 'Descarte',
                data: monthlyData.descarte,
                backgroundColor: 'rgba(178, 34, 34, 0.7)',
                borderColor: '#B22222',
                borderWidth: 1,
                pointRadius: 4,
              }
            ]
          },
          options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
              y: {
                beginAtZero: true,
                ticks: { font: { size: 10 } },
                grid: { display: true }
              },
              x: {
                ticks: { font: { size: 10 } },
                grid: { display: false }
              }
            },
            plugins: {
              legend: {
                position: 'bottom',
                labels: {
                  font: { size: 12 },
                  usePointStyle: true,
                  pointStyle: 'circle'
                }
              }
            }
          }
        });
      }

    } catch (error) {
      console.error("Erro ao puxar dados:", error);
      document.getElementById("teste1").textContent = "Erro ao carregar";
      document.getElementById("teste2").textContent = "Erro ao carregar";
      document.getElementById("teste3").textContent = "Erro ao carregar";
    }
  }

  PuxarDados();

  // ---------------- Chatbot ----------------
  const chat = document.getElementById("chatbot");
  const input = document.getElementById("chat-input");
  const chatBody = document.getElementById("chatbot-body");

  function toggleChat() {
    chat.style.display = chat.style.display === "flex" ? "none" : "flex";
  }

  function sendMessage() {
    const message = input.value.trim();
    if (!message) return;

    const userMsg = document.createElement("div");
    userMsg.className = "chatbot-message user";
    userMsg.textContent = message;
    chatBody.appendChild(userMsg);

    input.value = "";

    // Simula resposta do bot
    setTimeout(() => {
      const botMsg = document.createElement("div");
      botMsg.className = "chatbot-message";
      botMsg.textContent = "Estou analisando sua mensagem...";
      chatBody.appendChild(botMsg);
      chatBody.scrollTop = chatBody.scrollHeight;
    }, 500);
  }

  input.addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
      sendMessage();
    }
  });

  const chatButton = document.querySelector(".chatbot-button");
  if (chatButton) {
    chatButton.addEventListener("click", toggleChat);
  }

  // ---------------- Sidebar e Overlay ----------------
  const btnHamburger = document.getElementById('hamburger-btn');
  const sidebar = document.querySelector('.sidebar');
  const overlay = document.querySelector('.overlay');

  function toggleMenu() {
    sidebar.classList.toggle('active');
    overlay.classList.toggle('active');
  }

  btnHamburger.addEventListener('click', toggleMenu);
  overlay.addEventListener('click', toggleMenu);
});