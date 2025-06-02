# 📱 App Mobile com Expo & React Native

## 🧾 Visão Geral

Este aplicativo mobile foi desenvolvido utilizando **React Native**, **Expo** e **TypeScript**, com o objetivo de fornecer ao usuário uma plataforma para cadastro, monitoramento de sensores em tempo real, visualização de dashboards com gráficos, e acesso a dados por meio de um chatbot.

---

## 🚀 Funcionalidades

- **Cadastro e Login de Usuário**
  - Tela inicial para criação de conta ou acesso à aplicação.

- **Dashboard**
  - Visualização de dados diários e mensais.
  - Barras de aproveitamento.
  - Gráfico representando os dados do mês.

- **Monitoramento**
  - Exibição de informações dos sensores.
  - Leituras de entradas e saídas com data e hora atualizadas em tempo real.

- **Chatbot**
  - Interface onde usuários podem buscar por qualquer dado da aplicação de forma interativa.

---

## 📁 Estrutura de Pastas

```
app/
│
├── (tabs)/
│   ├── _layout.tsx         # Componente de layout para navegação entre abas
│   ├── chatbot.tsx         # Tela do Chatbot
│   ├── dashboard.tsx       # Tela de Dashboard
│   └── monitoring.tsx      # Tela de Monitoramento
│
├── _layout.tsx             # Layout principal da aplicação
├── +not-found.tsx          # Tela padrão para rotas inexistentes
└── index.tsx               # Tela principal (login e cadastro)

├── interfaces/
│   ├── device.ts           # Interface para dispositivos
│   ├── Message.ts          # Interface para mensagens
│   ├── PartError.ts        # Interface para erros de peças
│   └── State.ts            # Interface para a estação

├── services/
│   ├── api.ts              # Configuração do Axios para chamadas HTTP
│   └── AuthContext.tsx     # Serviço de autenticação
```

---

## 🧰 Tecnologias Utilizadas

- [React Native](https://reactnative.dev/)
- [Expo](https://expo.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- [Axios](https://axios-http.com/)

---

## 💻 Requisitos

Antes de iniciar, certifique-se de ter:

- [Node.js](https://nodejs.org/pt/download) instalado
- Conta no [Expo](https://expo.dev/)
- App **Expo Go** instalado no seu celular (Android/iOS)
- [Visual Studio Code](https://code.visualstudio.com/) ou outro editor de código

---

## 🛠️ Como Instalar e Rodar o Projeto

### 1. Clone o repositório

```bash
git clone <https://github.com/GabrielPerosa/ProjetoReciclagem.git>
cd mobile/appMobile
```

### 2. Instale as dependências

```bash
npm install
```

### 3. Execute o projeto

```bash
npx expo start
```

- Pressione a tecla **W** para abrir no navegador.
- Para rodar no celular:
  - Abra o app **Expo Go** no seu dispositivo.
  - Clique em **Scan QR Code** e escaneie o código QR que aparece no terminal do VSCode.

---

