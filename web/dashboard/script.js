document.addEventListener('DOMContentLoaded', function () {
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
            data: [5, 4, 5, 6, 7, 6, 5, 6, 5, 6, 7, 9],
            backgroundColor: 'rgba(65, 105, 225, 0.7)',
            borderColor: '#4169E1',
            borderWidth: 1,
            borderRadius: 4
          },
          {
            label: 'Plástico',
            data: [6, 5, 6, 7, 6, 7, 8, 6, 5, 6, 6, 7],
            backgroundColor: 'rgba(50, 205, 50, 0.7)',
            borderColor: '#32CD32',
            borderWidth: 1,
            borderRadius: 4
          },
          {
            label: 'Rejeitadas',
            data: [5, 6, 6, 5, 6, 5, 6, 5, 6, 5, 6, 7],
            backgroundColor: 'rgba(178, 34, 34, 0.7)',
            borderColor: '#B22222',
            borderWidth: 1,
            borderRadius: 4
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
              pointStyle: 'rectRounded'
            }
          }
        }
      }
    });
  }
});
