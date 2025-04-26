# Usa imagem com TensorFlow já instalado (salva muito tempo!)
FROM tensorflow/tensorflow:2.12.0

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências de sistema extras
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libsasl2-dev \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copia o arquivo de dependências
COPY requirements.txt .

# Atualiza pip e instala as demais dependências
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Expõe a porta para o FastAPI
EXPOSE 8000

# Comando para rodar a API
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]