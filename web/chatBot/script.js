async function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  const userMsg = document.createElement("div");
  userMsg.className = "chatbot-message user";
  userMsg.textContent = message;
  chatBody.appendChild(userMsg);
  input.value = "";
  chatBody.scrollTop = chatBody.scrollHeight;

  try {
    const response = await fetch("https://ydsdpxj25l.execute-api.us-east-1.amazonaws/chat/prompt", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: message })
    });

    if (!response.ok) throw new Error("Erro ao se comunicar com o servidor");

    const data = await response.json();

    const botMsg = document.createElement("div");
    botMsg.className = "chatbot-message";
    botMsg.textContent = data.resposta || "Não entendi sua pergunta.";
    chatBody.appendChild(botMsg);
    chatBody.scrollTop = chatBody.scrollHeight;

  } catch (error) {
    const botMsg = document.createElement("div");
    botMsg.className = "chatbot-message";
    botMsg.textContent = "Erro ao processar sua pergunta.";
    chatBody.appendChild(botMsg);
    chatBody.scrollTop = chatBody.scrollHeight;
    console.error(error);
  }
}
