# Etapa de build: Instalar dependências e gerar o binário
FROM python:3.12 AS build
WORKDIR /app
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Instala o PyInstaller para gerar o binário
RUN pip install pyinstaller

# Gera o executável (ajuste conforme seu script principal)
RUN pyinstaller --onefile main.py

# Verifica o conteúdo do diretório dist
RUN ls /app/dist

# Etapa de execução: Usando uma imagem mais leve
FROM alpine:latest AS run
WORKDIR /app

# Copia o binário gerado para a imagem final
COPY --from=build /app/dist/main /app

# Expõe a porta
EXPOSE 8085

# Comando para rodar o binário gerado
CMD ["/app/main"]
