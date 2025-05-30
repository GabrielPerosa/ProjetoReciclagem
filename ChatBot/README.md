# Chatbot

## Overview

Este projeto é um chatbot simples com processamento de linguagem natural (NLP), construído em Python. Usamos o framework FastAPI para premitir expor o serviço na Web. Ele identifica intenções e entidades em mensagens do usuário e responde com base em uma base de dados vinda de uma API devidamente configurada.

##  Estrutura do Projeto

```
├── Dockerfile              # Configuração do container
├── README.md               # Documentação principal do 
├── app                     
│   ├── README.md           # Doc principal
│   ├── __init__.py         # Instância da aplicação
│   ├── controllers         # Definição do controller
│   ├── data                # Resposta, entidades e intenção
│   ├── nlp                 # Processador de linguagem natural
│   ├── routes              # Definição das rotas
│   ├── services            # Serviço do chatbot
│   └── utils               # Métodos e classes auxiliares  
├── main.py                 # Ponto de entrada da aplicação
└── requirements.txt        # Dependências do projeto


```

##  Executando o Projeto

Localmente
```bash
export API_URL=<endpoint-da-api>
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
python main.py
```

Via Docker
```bash
docker run -d -p 8001:8001 --name chatbot chatbot:latest -e API_URL=<endpoint-da-api>
```

##  Funcionamento do NLP

1. O módulo `app/nlp` processa a mensagem do usuário.
2. Ele tenta identificar:

   * A **intenção** (com base em palavras-chave).
   * As **entidades** (com expressões regulares ou padrões).
3. Se não encontrar correspondência, uma resposta padrão é retornada.

## Dados pré-definidos

* Localizado em `app/data`.
* Contém:

  * Intenções e palavras-chave
  * Respostas padrão e específicas
  * Padrões de entidades

##  Utilitários

Localizados em `app/utils`, fornecem funções para:

* Carregamento de dados de arquivos JSON
* Tratamento e limpeza de texto vindo da API
* Processamento de dados e transformação deles Explicação dos Componentes
