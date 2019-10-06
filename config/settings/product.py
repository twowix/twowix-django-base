from config.settings.base import *
import json
from termcolor import colored

DEBUG = False

env_json = os.path.join(BASE_DIR, 'common/env.json')

with open(env_json) as f:
    env_json = json.loads(f.read())['product']

# APP
INSTALLED_APPS.append('backend.user')
INSTALLED_APPS.append('frontend.manager')
INSTALLED_APPS.append('frontend.landing')

# ETC
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.JSONRenderer')
DATABASES = env_json['DATABASES']

SECRET_KEY = env_json['SECRET_KEY']
JWT_AUTH['JWT_SECRET_KEY'] = SECRET_KEY

print(colored('Run ', 'blue'), colored('Product', 'green'), colored('Server', 'red'))
