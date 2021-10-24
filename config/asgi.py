import os

from django.core.asgi import get_asgi_application

if os.environ.get('SERVER_ENV') == 'product':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.product')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.develop')

application = get_asgi_application()