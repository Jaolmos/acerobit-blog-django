# AceroBit IA - Blog de Tecnología e IA

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.1.4-green.svg)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0+-blue.svg)

AceroBit IA es un Blog tecnológico enfocado en Inteligencia Artificial y desarrollo de software, optimizado para SEO, con diseño responsive y un completo sistema de gestión de contenidos que incluye categorías y tags

## 🚀 Características Principales

### Sistema de Contenidos
- Sistema de publicación de posts con categorías y etiquetas
- Editor visual TinyMCE para la creación de contenido (panel de administración)
- FileBrowser integrado para subir e insertar imágenes en el contenido de los posts
- Soporte para imágenes destacadas en posts
- Buscador integrado para todo el contenido
- URLs amigables y optimizadas para SEO

### Interfaz de Usuario
- Diseño responsive con TailwindCSS
- Interfaz moderna y minimalista enfocada en la lectura
- Barra lateral dinámica con categorías y tags más populares
- Sistema de navegación intuitivo
- Diseño optimizado para la experiencia de lectura

### Optimización y SEO
- Meta tags dinámicos para cada página
- Generación automática de `sitemap.xml`
- Configuración de `robots.txt`
- URLs semánticas y amigables
- Imágenes optimizadas con lazy loading

## 📸 Capturas de Pantalla

### Interfaz de Usuario

#### Página Principal
![Página Principal](screenshots/home.png)
*Vista de la página principal con los posts más recientes*

#### Detalle de Post
![Detalle de Post](screenshots/post_detail.png)
*Vista detallada de un artículo con contenido completo*

#### Categorías
![Lista de Categorías](screenshots/categories_list.png)
*Página de navegación por categorías*

#### Etiquetas
![Lista de Tags](screenshots/tag_list.png)
*Página de navegación por etiquetas*

#### Resultados de Búsqueda
![Resultados de Búsqueda](screenshots/search_results.png)
*Interfaz de resultados de búsqueda*

### Panel de Administración

#### Dashboard Principal
![Dashboard Admin](screenshots/admin_dashboard.png)
*Panel principal de administración de Django*

#### Gestión de Posts
![Listado de Posts](screenshots/admin_posts_list.png)
*Listado y gestión de artículos en el panel de administración*

#### Editor de Contenido
![Editor de Post](screenshots/admin_post_edit.png)
*Editor visual TinyMCE para la creación y edición de contenido*

#### Gestión de Categorías
![Gestión de Categorías](screenshots/admin_categories.png)
*Administración de categorías para organizar el contenido*

#### Gestión de Tags
![Gestión de Tags](screenshots/admin_tags.png)
*Administración de etiquetas para clasificar los artículos*

## 🛠 Requisitos Previos

### Python y Django
- Python 3.10 o superior
- pip (gestor de paquetes de Python)

### Node.js y npm
- Node.js 18.0 o superior
- npm 8.0 o superior (necesario para Tailwind CSS)

### Base de Datos
- MySQL

## 🛠 Stack Tecnológico

### Backend
- Python 3.10+
- Django 5.1.4
- MySQL
- TinyMCE
- FileBrowser

### Frontend
- TailwindCSS 3.0+
- HTML5
- JavaScript
- Google Fonts (Nunito)

### Herramientas de Desarrollo
- django-browser-reload (desarrollo en tiempo real)
- python-dotenv (variables de entorno)
- django-tailwind (estilos)
- Pillow (manejo de imágenes)
- django-filebrowser-no-grappelli (gestión de archivos)
- Docker (containerización - opcional)

## 📦 Estructura del Proyecto

```
proyecto/
├── blog/ # Aplicación principal
├── media/ # Archivos multimedia subidos (creada automáticamente)
│   └── uploads/ # Directorio para imágenes gestionadas por FileBrowser
├── staticfiles/admin/ # Archivos estáticos del admin
├── tech_blog/ # Configuración del proyecto
├── theme/static_src/ # Archivos fuente de Tailwind
├── screenshots/ # Capturas de pantalla de la aplicación
├── .env.example # Ejemplo de variables de entorno
├── .gitignore # Configuración de Git ignore
├── Dockerfile # Configuración de imagen Docker
├── .dockerignore # Archivos excluidos del build Docker
├── manage.py # Script de gestión de Django
├── requirements.txt # Dependencias del proyecto
```

*Nota: La carpeta `media` se crea automáticamente cuando se sube la primera imagen a través del panel de administración.*

## 🚀 Instalación

### Opción 1: Instalación Local Tradicional

1. Asegúrate de tener instalados Python y Node.js:

```bash
python --version # Debe ser 3.10 o superior
node --version   # Debe ser 18.0 o superior
npm --version    # Debe ser 8.0 o superior
```

2. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/acerobit-blog-django.git
cd acerobit-blog-django
```

3. Crear y activar entorno virtual:

```bash
python -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate # Windows
```

4. Instalar dependencias de Python:

```bash
pip install -r requirements.txt
```

5. Instalar y configurar Tailwind CSS:

```bash
python manage.py tailwind install
```

6. Configurar variables de entorno:
   - Copiar `.env.example` a `.env`:
   ```bash
   cp .env.example .env
   ```
   - Actualizar las credenciales en el archivo `.env`:
   ```bash
   # Django
   SECRET_KEY='tu_clave_secreta'
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DJANGO_ENV=development

   # Database MySQL
   DB_ENGINE='django.db.backends.mysql'
   DB_NAME='nombre_base_datos'
   DB_USER='usuario'
   DB_PASSWORD='contraseña'
   DB_HOST='localhost'
   DB_PORT='3306'
   ```


7. Realizar migraciones:

```bash
python manage.py migrate
```

8. Crear superusuario para el panel de administración:

```bash
python manage.py createsuperuser
```

9. Iniciar el compilador de Tailwind:

```bash
python manage.py tailwind start
```

10. En otra terminal, iniciar servidor de desarrollo:

```bash
python manage.py runserver
```

### Opción 2: Instalación con Docker 🐳

**Requisitos:**
- Docker instalado en tu sistema
- MySQL ejecutándose localmente en el puerto 3306

**Configuración de variables de entorno:**
- Asegúrate de que tu archivo `.env` use `DB_HOST=host.docker.internal` para conectar con MySQL local

**Comandos básicos:**

```bash
# 1. Construir la imagen Docker
docker build -t acerobit-blog .

# 2. Ejecutar el contenedor (desarrollo - con proyecto completo sincronizado)
docker run -p 8000:8000 -v .:/app acerobit-blog

# 3. Comandos útiles de gestión
docker ps                    # Ver contenedores en ejecución
docker stop CONTAINER_ID     # Parar contenedor
docker images                # Ver imágenes disponibles
docker logs CONTAINER_ID     # Ver logs del contenedor
```

**¿Por qué el volumen `-v .:/app`?**
- Conecta todo el proyecto de tu PC con el contenedor
- Permite que las imágenes del blog se vean correctamente
- Los archivos se sincronizan en tiempo real
- Tu archivo `.env` está disponible para la configuración
- Los cambios en código se reflejan inmediatamente (ideal para desarrollo)

**Archivos Docker incluidos:**
- `Dockerfile`: Configuración de la imagen (Python 3.12, Node.js, Tailwind, dependencias)
- `.dockerignore`: Archivos excluidos del build

**Consideraciones para despliegue en producción:**
- **Archivos media**: En producción, usa servicios en la nube como:
  - AWS S3 (más popular)
  - Cloudinary (especializado en imágenes, 10GB gratis)
  - Google Cloud Storage
  - DigitalOcean Spaces
- **Base de datos**: Usar base de datos gestionada en lugar de MySQL local
- **Variables de entorno**: Configurar `DEBUG=False` y `ALLOWED_HOSTS` apropiados

### Docker Avanzado - Entornos Dinámicos 🎯

El Dockerfile está configurado para **cambiar automáticamente** entre desarrollo y producción usando variables de entorno:

**Variable clave: `DJANGO_ENV`**
- `DJANGO_ENV=development` (por defecto) → Usa `runserver` (desarrollo)
- `DJANGO_ENV=production` → Usa `gunicorn` (producción)

**Comandos según entorno:**

```bash
# Desarrollo (por defecto) - con proyecto completo sincronizado
docker run -p 8000:8000 -v .:/app acerobit-blog

# Producción - con variables de entorno
docker run -p 8000:8000 \
  -e DJANGO_ENV=production \
  -e DEBUG=False \
  -e DB_HOST=tu-base-datos-produccion.com \
  -e ALLOWED_HOSTS=tudominio.com,www.tudominio.com \
  acerobit-blog

# Producción con archivo .env
docker run -p 8000:8000 --env-file .env.production acerobit-blog
```

**¿Qué cambia automáticamente?**
- **Desarrollo**: Django runserver con `--insecure` (sirve archivos estáticos)
- **Producción**: Gunicorn con 3 workers optimizado para producción

**Ejemplo de `.env.production`:**
```bash
DJANGO_ENV=production
DEBUG=False
ALLOWED_HOSTS=tudominio.com,www.tudominio.com
DB_HOST=production-database.amazonaws.com
DB_NAME=acerobit_production
# ... resto de variables
```

## 🔧 Configuración

El proyecto utiliza variables de entorno para la configuración. Principales variables a configurar:

```bash
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=mysql://user:password@localhost:3306/database
```

## 📝 Uso del Editor

### Insertar imágenes en posts
1. Desde el panel de administración, al editar un post:
   - Haz clic en el botón de imagen en el editor TinyMCE
   - Haz clic en "Browse" para abrir FileBrowser
   - Navega o sube una nueva imagen
   - Selecciona la imagen y ajusta sus propiedades
   - Haz clic en "Insert" para añadirla al contenido del post

### Gestión de archivos
1. Accede a `/admin/filebrowser/browse/` para gestionar todas tus imágenes
2. Funciones disponibles:
   - Subir nuevas imágenes
   - Crear directorios para organizar tus archivos
   - Renombrar, borrar o editar imágenes existentes

## 🔒 Características de Seguridad

- Configuración segura para producción
- Manejo seguro de archivos media
- Variables de entorno para datos sensibles
- Configuración de seguridad Django por defecto

## 🔄 Futuras Mejoras Planificadas

- Sistema de comentarios
- Newsletter para suscriptores
- Sistema de autenticación de usuarios
- Panel de usuario
- Formulario de contacto




