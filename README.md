# AceroBit IA - Blog de Tecnología e IA

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-5.1.4-green.svg)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

AceroBit IA es un Blog tecnológico enfocado en Inteligencia Artificial y desarrollo de software, optimizado para SEO, con diseño responsive y un completo sistema de gestión de contenidos que incluye categorías y tags

## 🚀 Características Principales

### Sistema de Contenidos
- Sistema de publicación de posts con categorías y etiquetas
- Editor visual TinyMCE para la creación de contenido (panel de administración)
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

## 📦 Estructura del Proyecto

```
proyecto/
├── blog/ # Aplicación principal
├── media/ # Archivos multimedia subidos (creada automáticamente)
├── staticfiles/admin/ # Archivos estáticos del admin
├── tech_blog/ # Configuración del proyecto
├── theme/static_src/ # Archivos fuente de Tailwind
├── .env.example # Ejemplo de variables de entorno
├── .gitignore # Configuración de Git ignore
├── LICENSE # Licencia MIT
├── manage.py # Script de gestión de Django
├── requirements.txt # Dependencias del proyecto
```

*Nota: La carpeta `media` se crea automáticamente cuando se sube la primera imagen a través del panel de administración.*

## 🚀 Instalación

1. Asegúrate de tener instalados Python y Node.js:

```bash
python --version # Debe ser 3.10 o superior
node --version   # Debe ser 18.0 o superior
npm --version    # Debe ser 8.0 o superior
```

2. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/acerobit-ia.git
cd acerobit-ia
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

## 🔧 Configuración

El proyecto utiliza variables de entorno para la configuración. Principales variables a configurar:

```bash
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=mysql://user:password@localhost:3306/database
```

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

## 📝 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👤 Autor

- **Jose Antonio Olmos**
- Email: jose.a.olmosmartinez@gmail.com


