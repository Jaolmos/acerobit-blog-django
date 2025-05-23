# Imagen base de Python
FROM python:3.12-slim

# Instalar dependencias del sistema para MySQL y Node.js
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalar Node.js LTS
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - \
    && apt-get install -y nodejs

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements primero (para aprovechar cache de Docker)
COPY requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Instalar dependencias de Tailwind
RUN python manage.py tailwind install

# Compilar Tailwind para producción
RUN python manage.py tailwind build

# Recopilar archivos estáticos
RUN python manage.py collectstatic --noinput

# Exponer puerto 8000
EXPOSE 8000

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000", "--insecure"]