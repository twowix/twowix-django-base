from config.settings.base import *
import json
from termcolor import colored

DEBUG = True

env_json = os.path.join(BASE_DIR, 'common/env.json')

if SERVER_ENV == 'local':
    with open(env_json) as f:
        env_json = json.loads(f.read())['local']

    try:
        INSTALLED_APPS.append('debug_toolbar')
        MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

        def custom_show_toolbar(self):
            return True

        DEBUG_TOOLBAR_CONFIG = {
            'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
            'RENDER_PANELS': True
        }
    except:
        pass
else:
    with open(env_json) as f:
        env_json = json.loads(f.read())['development']


# APP
INSTALLED_APPS.append('backend.user')
INSTALLED_APPS.append('frontend.manager')
INSTALLED_APPS.append('frontend.landing')

# ETC
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.JSONRenderer')
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')
DATABASES = env_json['DATABASES']
SECRET_KEY = env_json['SECRET_KEY']
JWT_AUTH['JWT_SECRET_KEY'] = SECRET_KEY

print(colored('Run', 'blue'), colored('Development', 'green'), colored('Server', 'red'))
