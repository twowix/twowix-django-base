from config.settings.base import *
import json
from termcolor import colored

DEBUG = True

env_json = os.path.join(BASE_DIR, 'common/env.json')

with open(env_json) as f:
    env_json = json.loads(f.read())['development']

# APP
INSTALLED_APPS.append('backend.user')
INSTALLED_APPS.append('frontend.manager')
INSTALLED_APPS.append('frontend.landing')
INSTALLED_APPS.append('debug_toolbar')

# MIDDLEWARE
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

# ETC
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.JSONRenderer')
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')
DATABASES = env_json['DATABASES']
SECRET_KEY = env_json['SECRET_KEY']
JWT_AUTH['JWT_SECRET_KEY'] = SECRET_KEY


def custom_show_toolbar(self): return True

DEBUG_TOOLBAR_CONFIG = {'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar}

print(colored('Run', 'blue'), colored('Development', 'green'), colored('Server', 'red'))
