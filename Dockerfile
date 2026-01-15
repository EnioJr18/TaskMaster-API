# 1. Escolhemos a imagem base (Python leve)
FROM python:3.13-slim

# 2. Definimos a pasta de trabalho dentro do container
WORKDIR /app

# 3. Copiamos os requisitos e instalamos (para aproveitar o cache do Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiamos todo o resto do código para dentro do container
COPY . .

# 5. Rodamos o setup do banco de dados (para garantir que a tabela exista)
RUN python db_setup.py

# 6. Expomos a porta 5000 (onde o Flask roda)
EXPOSE 5000

# 7. O comando final para ligar o servidor
CMD ["python", "run.py"]