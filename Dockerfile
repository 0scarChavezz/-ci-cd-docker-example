# Imagen base de Python
FROM python:3.10-slim

# Crear y establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código
COPY . .

# Exponer el puerto
EXPOSE 5000

# Comando por defecto al iniciar el contenedor
CMD ["python", "app.py"]
