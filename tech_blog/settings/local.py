from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Añadir django_browser_reload a las apps instaladas
INSTALLED_APPS += ['django_browser_reload']
MIDDLEWARE += ['django_browser_reload.middleware.BrowserReloadMiddleware']

# Ruta al ejecutable de npm en Windows
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

# IPs permitidas para desarrollo
INTERNAL_IPS = [
    "127.0.0.1",
]