# Etapa de build: Instalar dependências e gerar o binário
FROM python:3.12-slim 

WORKDIR /
COPY . .
# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# Comando para rodar o binário gerado
