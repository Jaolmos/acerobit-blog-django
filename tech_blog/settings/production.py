from .base import *

DEBUG = os.getenv('DEBUG', 'False') == 'True'

# Ruta al ejecutable de npm en producción
NPM_BIN_PATH = "/home/acerobitia/.nvm/versions/node/v20.18.1/bin/npm"

# Configuraciones de seguridad para producción
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'